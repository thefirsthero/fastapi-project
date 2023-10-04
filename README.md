# FastAPI Todo App

This is a simple todo app using FastAPI, HTMX, Jinja and SQLite. It allows you to create, update and delete tasks from a web interface. It uses SQLite as the database and SQLAlchemy as the ORM.

## Why these technologies?

- FastAPI: FastAPI is a modern and fast web framework for Python that supports async operations, dependency injection, data validation and automatic documentation. It is based on Pydantic and Starlette, and it is well suited for building RESTful APIs and microservices.  
- HTMX: HTMX is a lightweight JavaScript library that lets you add dynamic behavior to your HTML using custom attributes. It enables you to use AJAX, WebSockets, CSS transitions and server-sent events without writing any JavaScript code. It is ideal for creating interactive and responsive web pages with minimal effort.  
- Jinja: Jinja is a powerful and flexible templating engine for Python that allows you to generate HTML, XML or other markup formats from Python data structures. It supports template inheritance, sandboxed execution, automatic HTML escaping and many other features. It integrates well with FastAPI and HTMX, and it makes it easy to create dynamic web pages.  
- SQLite: SQLite is a self-contained, serverless, zero-configuration and cross-platform database engine that stores data in a single file. It supports most of the SQL standard features, such as transactions, triggers, views and indexes. It is fast, reliable and portable, and it can handle low to medium traffic web applications.  
- SQLAlchemy: SQLAlchemy is a popular and mature ORM (object-relational mapper) for Python that provides a high-level abstraction over various databases. It allows you to write Python code to manipulate data instead of raw SQL queries. It supports multiple database backends, including SQLite, and it offers many advanced features such as declarative mapping, query expressions, session management and schema migrations.  

## How to run this app?

To run this app, you need to have Python 3.8 or higher installed on your system. You also need to install the required packages using the following command:

```bash
pip install -r requirements.txt
```

Alternatively, you can use Docker to build and run the app without installing anything locally. To do that, you need to have Docker and Docker Compose installed on your system. Then, you can use the following commands:

```bash
docker-compose build
docker-compose up
```

To start the app, you need to run the following command:

```bash
uvicorn main:app --reload
```

This will start a local server on port 8000. You can access the app by visiting http://localhost:8000 in your browser.

To use the app, you need to create an account and log in. You can then add tasks by filling the form and clicking the "Add" button. You can also update the status of a task by clicking the "Update" button or delete a task by clicking the "Delete" button.

## References

: [Why FastAPI?](https://fastapi.tiangolo.com/alternatives/)
: [FastAPI - The Database Toolkit for Python](https://fastapi.tiangolo.com/)
: [Why Every Web Developer Should Know HTMX?](https://dev.to/rajasegar/why-every-web-developer-should-know-htmx-4f5a)
: [htmx - high power tools for html](https://htmx.org/)
: [Jinja2 Explained in 5 Minutes!](https://www.youtube.com/watch?v=QnDWIZuWYW0)
: [Jinja - Reviews, Pros & Cons | Companies using Jinja](https://stackshare.io/jinja)
: [What Is SQLite and Why Is It So Popular?](https://www.freecodecamp.org/news/what-is-sqlite-and-why-is-it-so-popular-b0151e9c6e9f/)
: [SQLite - The Database Toolkit for Python](https://www.sqlite.org/index.html)
: [SQLAlchemy - Introduction](https://www.sqlalchemy.org/intro.html)
: [SQLAlchemy + Pandas: A Comprehensive Guide to Database Session Management](https://towardsdatascience.com/sqlalchemy-pandas-a-comprehensive-guide-to-database-session-management-fb3c7a0c7b0f)
