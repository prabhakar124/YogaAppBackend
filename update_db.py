from database import engine, Base
from models import User, Blog  # Import all models

# This will create all tables
Base.metadata.create_all(bind=engine)
print("✅ Database tables created successfully!")
print("Tables created:")
print("  - users")
print("  - blogs")