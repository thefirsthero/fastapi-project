# Import necessary modules and functions
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import Session
from database import Base

# Define the ToDo model
class ToDo(Base):
    __tablename__ = "todos"

    id = Column(Integer, primary_key=True, index=True)
    content = Column(String)
    session_key = Column(String)

# Function to create a new todo item in the database
def create_todo(db: Session, content: str, session_key: str):
    todo = ToDo(content=content, session_key=session_key)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

# Function to retrieve a todo item by its ID
def get_todo(db: Session, item_id: int):
    return db.query(ToDo).filter(ToDo.id == item_id).first()

# Function to update the content of a todo item
def update_todo(db: Session, item_id: int, content: str):
    todo = get_todo(db, item_id)
    todo.content = content
    db.commit()
    db.refresh(todo)
    return todo

# Function to retrieve a list of todos associated with a session key
def get_todos(db: Session, session_key: str, skip: int = 0, limit: int = 100):
    return db.query(ToDo).filter(ToDo.session_key == session_key).offset(skip).limit(limit).all()

# Function to delete a todo item from the database
def delete_todo(db: Session, item_id: int):
    todo = get_todo(db, item_id)
    db.delete(todo)
    db.commit()
