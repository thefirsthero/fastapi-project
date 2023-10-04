# Import necessary modules and functions
import random
import uuid
from datetime import timedelta
from fastapi import Depends, FastAPI, Form, Request, Response
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from sqlalchemy.orm import Session
from database import Base, SessionLocal, engine
from models import create_todo, delete_todo, get_todo, get_todos, update_todo

# Create database tables if they don't exist
Base.metadata.create_all(bind=engine)

# Create a FastAPI app instance
app = FastAPI()
templates = Jinja2Templates(directory="templates")

# Function to get a database session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

# Define a route for the home page
@app.get("/", response_class=HTMLResponse)
def home(request: Request, db: Session = Depends(get_db)):
    # Generate or retrieve a session key from cookies
    session_key = request.cookies.get("session_key", uuid.uuid4().hex)
    
    # Get todos associated with the session key
    todos = get_todos(db, session_key)
    
    # Prepare context for rendering the home page template
    context = {
        "request": request,
        "todos": todos,
        "title": "Home"
    }
    
    # Create a response with the template and set a cookie for the session key
    response = templates.TemplateResponse("home.html", context)
    response.set_cookie(key="session_key", value=session_key, expires=259200)  # 3 days
    return response

# Define a route to add a new todo item
@app.post("/add", response_class=HTMLResponse)
def post_add(request: Request, content: str = Form(...), db: Session = Depends(get_db)):
    # Get the session key from cookies
    session_key = request.cookies.get("session_key")
    
    # Create a new todo item in the database
    todo = create_todo(db, content=content, session_key=session_key)
    
    # Prepare context for rendering the todo item template
    context = {"request": request, "todo": todo}
    
    return templates.TemplateResponse("todo/item.html", context)

# Define a route to edit a todo item
@app.get("/edit/{item_id}", response_class=HTMLResponse)
def get_edit(request: Request, item_id: int, db: Session = Depends(get_db)):
    # Get the todo item to be edited from the database
    todo = get_todo(db, item_id)
    
    # Prepare context for rendering the edit form template
    context = {"request": request, "todo": todo}
    
    return templates.TemplateResponse("todo/form.html", context)

# Define a route to update a todo item
@app.put("/edit/{item_id}", response_class=HTMLResponse)
def put_edit(request: Request, item_id: int, content: str = Form(...), db: Session = Depends(get_db)):
    # Update the content of a todo item in the database
    todo = update_todo(db, item_id, content)
    
    # Prepare context for rendering the updated todo item template
    context = {"request": request, "todo": todo}
    
    return templates.TemplateResponse("todo/item.html", context)

# Define a route to delete a todo item
@app.delete("/delete/{item_id}", response_class=Response)
def delete(item_id: int, db: Session = Depends(get_db)):
    # Delete a todo item from the database
    delete_todo(db, item_id)

# Rest of the code for routes and their functions
