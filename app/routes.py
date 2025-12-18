from fastapi import APIRouter, HTTPException
from .schema import UserCreate, UserUpdate

router = APIRouter()

users = []  # temporary in-memory storage
currnt_id = 1
@router.post("/users")
def create_user(user: UserCreate):
    
    users.append(user.dict())
    return {
        "message": "User created successfully",
        "user": user
    }
@router.get("/")
def home():
    return {
        "message":"Server is running.",
        "status":"success",
        "route":"go to /users"
        }

@router.get("/users")
def get_users():
    return {
        "message":"Server is running.",
        "status":"success",
        "users":users  
        }



@router.put("/users/{email}")
def update_user(email: str, user: UserUpdate):
    for u in users:
        if u["email"] == email:
            u.update({k: v for k, v in user.dict().items() if v is not None})
            return {"message": "User updated", "user": u}

    raise HTTPException(status_code=404, detail="User not found")

@router.delete("/users/{email}")
def delete_user(email: str):
    for u in users:
        if u["email"] == email:
            users.remove(u)
            return {"message": "User deleted"}

    raise HTTPException(status_code=404, detail="User not found")
