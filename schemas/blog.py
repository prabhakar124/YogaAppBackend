from pydantic import BaseModel, field_validator
from typing import List, Optional
from datetime import datetime

# Content section schema
class BlogSectionSchema(BaseModel):
    heading: str
    text: str
    image: Optional[str] = None
    imageAlt: Optional[str] = None

# Create/Update blog schema
class BlogCreateSchema(BaseModel):
    title: str
    excerpt: str
    category: str
    category_color: str
    author: str
    read_time: str
    image: str
    table_of_contents: List[str]
    content: List[BlogSectionSchema]
    published: Optional[bool] = True
    
    @field_validator('category')
    @classmethod
    def validate_category(cls, v):
        allowed_categories = ["Asanas", "Pranayam", "Disease Cure", "Meditation", "Philosophy", "YTT"]
        if v not in allowed_categories:
            raise ValueError(f'Category must be one of: {", ".join(allowed_categories)}')
        return v
    
    @field_validator('title')
    @classmethod
    def validate_title(cls, v):
        if len(v) < 10:
            raise ValueError('Title must be at least 10 characters long')
        if len(v) > 500:
            raise ValueError('Title must be less than 500 characters')
        return v

class BlogUpdateSchema(BaseModel):
    title: Optional[str] = None
    excerpt: Optional[str] = None
    category: Optional[str] = None
    category_color: Optional[str] = None
    author: Optional[str] = None
    read_time: Optional[str] = None
    image: Optional[str] = None
    table_of_contents: Optional[List[str]] = None
    content: Optional[List[BlogSectionSchema]] = None
    published: Optional[bool] = None

# Response schema (matches frontend structure)
class BlogResponseSchema(BaseModel):
    id: str
    slug: str
    title: str
    excerpt: str
    category: str
    categoryColor: str
    author: str
    date: str
    readTime: str
    image: str
    tableOfContents: List[str]
    content: Optional[List[dict]] = None  # Include full content only when needed
    published: bool
    created_at: Optional[str] = None
    updated_at: Optional[str] = None
    
    class Config:
        from_attributes = True

# List response (without full content for performance)
class BlogListResponseSchema(BaseModel):
    id: str
    slug: str
    title: str
    excerpt: str
    category: str
    categoryColor: str
    author: str
    date: str
    readTime: str
    image: str
    tableOfContents: List[str]
    
    class Config:
        from_attributes = True

class BlogListResponse(BaseModel):
    blogs: List[BlogListResponseSchema]
    total: int
    page: int
    per_page: int
    total_pages: int