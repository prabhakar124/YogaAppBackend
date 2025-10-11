from fastapi import APIRouter, Depends, HTTPException, status, Query
from sqlalchemy.orm import Session
from sqlalchemy import or_, and_
from typing import List, Optional
from datetime import datetime

from database import get_db
from models import Blog
from schemas.blog import (
    BlogCreateSchema, 
    BlogUpdateSchema, 
    BlogResponseSchema,
    BlogListResponseSchema,
    BlogListResponse
)
from middleware.auth import get_current_user  # For admin-only routes

router = APIRouter()

@router.get("/", response_model=BlogListResponse)
async def get_all_blogs(
    page: int = Query(1, ge=1),
    per_page: int = Query(10, ge=1, le=100),
    category: Optional[str] = None,
    search: Optional[str] = None,
    published_only: bool = True,
    db: Session = Depends(get_db)
):
    """
    Get all blogs with pagination, filtering, and search
    - page: Page number (default: 1)
    - per_page: Items per page (default: 10, max: 100)
    - category: Filter by category
    - search: Search in title, excerpt, and category
    - published_only: Show only published blogs (default: true)
    """
    query = db.query(Blog)
    
    # Filter by published status
    if published_only:
        query = query.filter(Blog.published == True)
    
    # Filter by category
    if category and category != "All Blogs":
        query = query.filter(Blog.category == category)
    
    # Search
    if search:
        search_term = f"%{search}%"
        query = query.filter(
            or_(
                Blog.title.ilike(search_term),
                Blog.excerpt.ilike(search_term),
                Blog.category.ilike(search_term)
            )
        )
    
    # Get total count
    total = query.count()
    
    # Pagination
    skip = (page - 1) * per_page
    blogs = query.order_by(Blog.created_at.desc()).offset(skip).limit(per_page).all()
    
    # Calculate total pages
    total_pages = (total + per_page - 1) // per_page
    
    # Convert to response format (without full content)
    blog_list = []
    for blog in blogs:
        blog_dict = blog.to_dict()
        # Remove content from list view for performance
        blog_dict.pop('content', None)
        blog_dict.pop('created_at', None)
        blog_dict.pop('updated_at', None)
        blog_dict.pop('published', None)
        blog_list.append(blog_dict)
    
    return {
        "blogs": blog_list,
        "total": total,
        "page": page,
        "per_page": per_page,
        "total_pages": total_pages
    }

@router.get("/{slug}", response_model=BlogResponseSchema)
async def get_blog_by_slug(
    slug: str,
    db: Session = Depends(get_db)
):
    """Get single blog by slug with full content"""
    blog = db.query(Blog).filter(Blog.slug == slug).first()
    
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    # Check if published (unless user is admin - add admin check if needed)
    if not blog.published:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    return blog.to_dict()

@router.get("/{blog_id}/related", response_model=List[BlogListResponseSchema])
async def get_related_blogs(
    blog_id: int,
    limit: int = Query(3, ge=1, le=10),
    db: Session = Depends(get_db)
):
    """Get related blogs (same category, excluding current blog)"""
    # Get current blog
    current_blog = db.query(Blog).filter(Blog.id == blog_id).first()
    
    if not current_blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    # Get related blogs (same category, published, exclude current)
    related_blogs = db.query(Blog).filter(
        and_(
            Blog.category == current_blog.category,
            Blog.id != blog_id,
            Blog.published == True
        )
    ).order_by(Blog.created_at.desc()).limit(limit).all()
    
    # Convert to response format
    blog_list = []
    for blog in related_blogs:
        blog_dict = blog.to_dict()
        blog_dict.pop('content', None)
        blog_dict.pop('created_at', None)
        blog_dict.pop('updated_at', None)
        blog_dict.pop('published', None)
        blog_list.append(blog_dict)
    
    return blog_list

@router.post("/", response_model=BlogResponseSchema, status_code=status.HTTP_201_CREATED)
async def create_blog(
    blog_data: BlogCreateSchema,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Admin only
):
    """Create new blog (Admin only)"""
    # Generate slug from title
    slug = Blog.generate_slug(blog_data.title)
    
    # Check if slug already exists
    existing_blog = db.query(Blog).filter(Blog.slug == slug).first()
    if existing_blog:
        # Add number suffix if slug exists
        counter = 1
        while db.query(Blog).filter(Blog.slug == f"{slug}-{counter}").first():
            counter += 1
        slug = f"{slug}-{counter}"
    
    # Convert content to dict format
    content_data = [section.dict() for section in blog_data.content]
    
    # Create blog
    new_blog = Blog(
        slug=slug,
        title=blog_data.title,
        excerpt=blog_data.excerpt,
        category=blog_data.category,
        category_color=blog_data.category_color,
        author=blog_data.author,
        read_time=blog_data.read_time,
        image=blog_data.image,
        table_of_contents=blog_data.table_of_contents,
        content=content_data,
        published=blog_data.published
    )
    
    db.add(new_blog)
    db.commit()
    db.refresh(new_blog)
    
    return new_blog.to_dict()

@router.put("/{blog_id}", response_model=BlogResponseSchema)
async def update_blog(
    blog_id: int,
    blog_data: BlogUpdateSchema,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Admin only
):
    """Update blog (Admin only)"""
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    # Update fields
    update_data = blog_data.dict(exclude_unset=True)
    
    # Handle content conversion if present
    if 'content' in update_data and update_data['content']:
        update_data['content'] = [section.dict() if hasattr(section, 'dict') else section 
                                   for section in update_data['content']]
    
    # Update slug if title changed
    if 'title' in update_data:
        new_slug = Blog.generate_slug(update_data['title'])
        if new_slug != blog.slug:
            # Check if new slug exists
            existing = db.query(Blog).filter(
                Blog.slug == new_slug,
                Blog.id != blog_id
            ).first()
            if existing:
                counter = 1
                while db.query(Blog).filter(Blog.slug == f"{new_slug}-{counter}").first():
                    counter += 1
                new_slug = f"{new_slug}-{counter}"
            update_data['slug'] = new_slug
    
    # Apply updates
    for key, value in update_data.items():
        setattr(blog, key, value)
    
    blog.updated_at = datetime.utcnow()
    
    db.commit()
    db.refresh(blog)
    
    return blog.to_dict()

@router.delete("/{blog_id}", status_code=status.HTTP_204_NO_CONTENT)
async def delete_blog(
    blog_id: int,
    db: Session = Depends(get_db),
    current_user: dict = Depends(get_current_user)  # Admin only
):
    """Delete blog (Admin only)"""
    blog = db.query(Blog).filter(Blog.id == blog_id).first()
    
    if not blog:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Blog not found"
        )
    
    db.delete(blog)
    db.commit()
    
    return None

@router.get("/categories/list")
async def get_categories():
    """Get list of all categories with their colors"""
    categories = [
        {"name": "Asanas", "color": "#ff6b35"},
        {"name": "Pranayam", "color": "#4ecdc4"},
        {"name": "Disease Cure", "color": "#95e1d3"},
        {"name": "Meditation", "color": "#a8e6cf"},
        {"name": "Philosophy", "color": "#ffd93d"},
        {"name": "YTT", "color": "#6c5ce7"}
    ]
    return {"categories": categories}