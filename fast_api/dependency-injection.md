Dependency Injection is a design pattern where required objects or services are provided to a function instead of being created inside it. In FastAPI, Depends() is used to inject dependencies such as database connections, authentication, configuration, or external service clients.

@app.get("/users")
def get_users():
    db = connect_database()   # Repeated everywhere
    return db.get_users()

Another API:
@app.post("/users")
def create_user():
    db = connect_database()   # Repeated again
    db.create_user()

Solution: 
Create one function.
def get_db():
    return "Database Connection"

Now instead of creating it everywhere:

from fastapi import Depends

@app.get("/users")
def get_users(db = Depends(get_db)):
    return db

Instead:
def get_current_user():
    return {
        "name": "Naga"
    }

@app.get("/profile")

def profile(user = Depends(get_current_user)):
    return user

Dependency Chain: 

def get_db():
    return "Database"


def get_user(db = Depends(get_db)):
    return "Current User"


@app.get("/profile")
def profile(user = Depends(get_user)):
    return user