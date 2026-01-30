# FastAPI Learning Journey 🚀

A blog application built to learn and practice modern Python web development with FastAPI, SQLAlchemy, and async programming.

## 📚 What I Learned

### 1. **FastAPI Fundamentals**
- Setting up a FastAPI application with proper project structure
- Using dependency injection with `Depends()` for database sessions
- Type hints and `Annotated` types for cleaner code
- Automatic API documentation with OpenAPI/Swagger
- Request/response models with Pydantic schemas
- HTTP status codes and proper REST API design

### 2. **Async Python Programming**
- Understanding `async`/`await` syntax
- Working with `AsyncSession` for database operations
- Using `asynccontextmanager` for application lifespan management
- Async database queries with SQLAlchemy 2.0

### 3. **SQLAlchemy 2.0 (Modern ORM)**
- Declarative models with `Mapped` and `mapped_column`
- Relationship mapping between User and Post models
- Cascade operations (`cascade="all, delete-orphan"`)
- Eager loading with `selectinload()` to avoid N+1 queries
- Foreign key constraints and database indexing
- Using `async_sessionmaker` for async database sessions

### 4. **Database Design**
- One-to-many relationships (User → Posts)
- Proper use of foreign keys and indexes
- Automatic timestamp handling with `datetime.now(UTC)`
- SQLite with async support via `aiosqlite`

### 5. **API Design Patterns**
- RESTful routing with APIRouter
- CRUD operations (Create, Read, Update, Delete)
- Difference between PUT (full update) and PATCH (partial update)
- Proper HTTP status codes (201 for creation, 204 for deletion, 404 for not found)
- Input validation and error handling

### 6. **Pydantic Schemas**
- Separating concerns: Create, Update, and Response schemas
- Field validation with `Field()` (min_length, max_length)
- Email validation with `EmailStr`
- Optional fields for partial updates
- `ConfigDict` with `from_attributes=True` for ORM compatibility

### 7. **Template Rendering**
- Serving HTML templates with Jinja2
- Mixing API endpoints with server-side rendering
- Static file serving for CSS, JS, and images
- Media file handling for user uploads

### 8. **Error Handling**
- Custom exception handlers for different contexts (API vs HTML)
- Handling `HTTPException` and `RequestValidationError`
- Conditional error responses (JSON for API, HTML for web pages)
- User-friendly error pages

### 9. **Project Organization**
- Modular router structure (`routers/users.py`, `routers/posts.py`)
- Separation of concerns (models, schemas, database, routers)
- Clean imports and dependencies

### 10. **Modern Python Features**
- Type hints with `Mapped[type]`
- Union types with `|` operator (e.g., `str | None`)
- Property decorators for computed fields (`@property`)
- Context managers for resource management

## 🏗️ Project Structure

```
.
├── main.py              # Application entry point, lifespan, routes
├── database.py          # Database configuration and session management
├── models.py            # SQLAlchemy ORM models (User, Post)
├── schemas.py           # Pydantic schemas for validation
├── routers/
│   ├── users.py         # User CRUD endpoints
│   └── posts.py         # Post CRUD endpoints
├── templates/           # Jinja2 HTML templates
├── static/              # CSS, JS, images
├── media/               # User-uploaded files
└── blog.db              # SQLite database
```

## 🔧 Tech Stack

- **FastAPI** - Modern, fast web framework
- **SQLAlchemy 2.0** - Async ORM with modern syntax
- **Pydantic** - Data validation using Python type hints
- **aiosqlite** - Async SQLite driver
- **Jinja2** - Template engine
- **SQLite** - Lightweight database

## 🚀 Key Features Implemented

### API Endpoints

**Users:**
- `POST /api/users` - Create new user
- `GET /api/users/{user_id}` - Get user details
- `GET /api/users/{user_id}/posts` - Get all posts by user
- `PATCH /api/users/{user_id}` - Update user (partial)
- `DELETE /api/users/{user_id}` - Delete user

**Posts:**
- `POST /api/posts` - Create new post
- `GET /api/posts` - Get all posts
- `GET /api/posts/{post_id}` - Get single post
- `PUT /api/posts/{post_id}` - Full update
- `PATCH /api/posts/{post_id}` - Partial update
- `DELETE /api/posts/{post_id}` - Delete post

### Web Pages
- Home page with all posts
- Individual post view
- User posts page

## 💡 Key Learnings & Best Practices

1. **Always use eager loading** (`selectinload`) when you know you'll need related data to avoid N+1 query problems

2. **Separate schemas for different operations** - Create, Update, and Response schemas serve different purposes

3. **Use proper HTTP methods** - POST for create, GET for read, PUT for full update, PATCH for partial, DELETE for removal

4. **Validate at the edge** - Let Pydantic handle validation before data reaches your business logic

5. **Async all the way** - When using async, make sure the entire chain is async (database, handlers, etc.)

6. **Type hints everywhere** - They help with IDE support, catch bugs early, and serve as documentation

7. **Dependency injection** - FastAPI's `Depends()` makes testing and code reuse much easier

8. **Proper error handling** - Different contexts (API vs web) need different error responses

## 🎯 What's Next?

This project was built for learning, but here are potential improvements:
- Authentication & authorization (JWT tokens)
- Password hashing (bcrypt)
- File upload handling for profile pictures
- Pagination for post lists
- Search functionality
- Comments on posts
- Testing with pytest
- Docker containerization
- Environment variables for configuration

## 🏃 Running the Project

```bash
# Install dependencies
uv sync

# Run the application
fastapi dev main.py
```

Visit:
- Web UI: http://localhost:8000
- API Docs: http://localhost:8000/docs
- Alternative API Docs: http://localhost:8000/redoc

---

**Note:** This is a learning project focused on understanding FastAPI, async Python, and modern web development patterns. The goal was to learn by building, not to create a production-ready application.