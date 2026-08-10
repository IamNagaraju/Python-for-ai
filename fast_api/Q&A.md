# Q1. Why do we use Uvicorn?
FastAPI is an ASGI application, and Uvicorn is an ASGI server. It runs the FastAPI application, listens for HTTP requests, forwards them to FastAPI, and returns the response to the client. It also supports asynchronous execution, making it suitable for high-performance applications.

# Q2. Explain uvicorn main:app --reload

main.py
      │
      ▼
app = FastAPI()
      │
      ▼
Run this application
--reload automatically restarts the server.
# Why FastAPI instead of Flask?

A complete answer:

✅ Async support
✅ High performance
✅ Automatic validation (Pydantic)
✅ Automatic Swagger documentation
✅ Excellent type hint support

WSGI (Old) #synchronous

ASGI (Modern) # asynchronous

Node js 
Express

↓

Node Runtime

↓

libuv Event Loop

FastAPI

↓

Uvicorn

↓

asyncio Event Loop

The server is not blocked.

Why is FastAPI non-blocking?
FastAPI supports asynchronous programming using Python's async/await. It runs on an ASGI server like Uvicorn, which uses Python's asyncio event loop. When an awaited I/O operation (such as a database query or OpenAI API call) is in progress, the event loop switches to handling other requests instead of blocking the thread.
ASGI = Asynchronous Server Gateway Interface

Think of responsibilities:

Uvicorn
Accept HTTP requests
Manage sockets
Run the event loop
Handle connections
FastAPI
Execute your business logic
Validate input
Call databases
Call OpenAI
Return JSON
When do you use path parameters vs query parameters?
Path parameters identify a specific resource, while query parameters are used for filtering, searching, sorting, pagination, or other optional request options.
