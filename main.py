# Benefits of FastAPI:
# 1) it is just plain python (easy to understand as syntax is just plain python)
# 2) built in async (asynchronous programming)
# 3) built in data validation -> Pydantic models; i.e. To declare a request body, you use Pydantic models with all their power and benefits.
# 4) typed python! -> for (request bodies and more??)
# 5) errors are in json
# 6) built in authentication - HTTP Basic OAuth2 tokens (JWT tokens) and header API keys.
# 7) swagger ui built in; if you go to the /docs route you get documentation!!! :) (demo API to stakeholders easily!) ; the /redoc route does the same w/ a diff UI/

from fastapi import FastAPI
from models import ToDo

app = FastAPI()


@app.get("/")
async def root():
    return {"message": "Hello World"}

todos = []

# Get all todos
@app.get("/todos")
async def get_todos():
    return {"todos": todos}

# Get single todo
@app.get("/todos/{todo_id}")
async def get_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            return {"todo": todo}
    return {"todos": "No todos found"}

# Create a todo
@app.post("/todos")
async def create_todos(todo: ToDo): # fast api is typed; i.e. todo: int or todo: str, will enforce that the todo being passed in the method is of type int or str.
    todos.append(todo)
    return {"todos": "Todo has been added"}

# Update a todo
@app.put("/todos/{todo_id}")
async def update_todos(todo_id: int, todo_obj: ToDo):
    for todo in todos:
        if todo.id == todo_id:
            todo.id = todo_id
            todo.item = todo_obj.item
            return {"todo": todo}
    return {"todos": "No todos found to update"}

# Delete a todo
@app.delete("/todos/{todo_id}")
async def delete_todo(todo_id: int):
    for todo in todos:
        if todo.id == todo_id:
            todos.remove(todo)
            return {"message":"todo has been DELETED!"}
    return {"todos": "No todos found"}