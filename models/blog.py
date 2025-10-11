from sqlalchemy import Column, Integer, String, Text, Boolean, DateTime, JSON
from datetime import datetime
from database import Base
import re

class Blog(Base):
    __tablename__ = "blogs"
    
    id = Column(Integer, primary_key=True, index=True)
    slug = Column(String(255), unique=True, index=True, nullable=False)
    title = Column(String(500), nullable=False)
    excerpt = Column(Text, nullable=False)
    category = Column(String(100), nullable=False)
    category_color = Column(String(50), nullable=False)
    author = Column(String(255), nullable=False)
    read_time = Column(String(50), nullable=False)
    image = Column(String(500), nullable=False)  # Main blog image URL
    table_of_contents = Column(JSON, nullable=False)  # Array of strings
    content = Column(JSON, nullable=False)  # Array of section objects
    published = Column(Boolean, default=True)
    created_at = Column(DateTime, default=datetime.utcnow)
    updated_at = Column(DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    
    def to_dict(self):
        """Convert to dictionary for API response"""
        return {
            "id": str(self.id),
            "slug": self.slug,
            "title": self.title,
            "excerpt": self.excerpt,
            "category": self.category,
            "categoryColor": self.category_color,
            "author": self.author,
            "date": self.created_at.strftime("%b %d, %Y"),
            "readTime": self.read_time,
            "image": self.image,
            "tableOfContents": self.table_of_contents,
            "content": self.content,
            "published": self.published,
            "created_at": self.created_at.isoformat() if self.created_at else None,
            "updated_at": self.updated_at.isoformat() if self.updated_at else None
        }
    
    @staticmethod
    def generate_slug(title: str) -> str:
        """Generate URL-friendly slug from title"""
        slug = title.lower()
        slug = re.sub(r'[^a-z0-9]+', '-', slug)
        slug = re.sub(r'^-|-$', '', slug)
        return slug