FastAPI is the framework that helps us build that backend.

Why FastAPI?

Instead of Flask or Django?

1. Very Fast

Built on:

Starlette
Pydantic
AsyncIO

One of the fastest Python web frameworks

2. Automatic API Documentation

When you write:
@app.get("/users")
def get_users():
    return {"users": []}

FastAPI automatically creates: http://localhost:8000/docs

3. Type Safety

@app.get("/users/{id}")
def get_user(id: int):
    return id
 # If someone passes: string FastAPI automatically returns validation errors.No manual checking.
# Why do we use Uvicorn?
Uvicorn is a lightning-fast ASGI (Asynchronous Server Gateway Interface) web server for Python. It is used to run asynchronous Python web frameworks like FastAPI or Starlette by listening for network requests, handling incoming HTTP or WebSocket connections, and passing them to your application code.What Uvicorn DoesBridges networks and code: Receives client requests and sends back responses without making your application handle low-level socket connections.Supports async code: Handles asynchronous operations smoothly using fast tools like uvloop.Enables WebSockets: Supports long-lived, real-time two-way communication channels.

Run in development: Use uvicorn main:app --reload where main is your python file and app is your application instance. The --reload flag restarts the server automatically when code changes.Run with multiple workers: Use uvicorn main:app --workers 4 to utilize multiple CPU cores.