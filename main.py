
from fastapi import FastAPI, Depends, HTTPException, status
from fastapi.security import HTTPBasic, HTTPBasicCredentials

app = FastAPI(title="Simple Auth + Actions API")

security = HTTPBasic()

# Tài khoản mẫu (demo)
USER_DB = {
    "admin": "12345",
    "user": "password"
}

def authenticate(credentials: HTTPBasicCredentials = Depends(security)):
    username = credentials.username
    password = credentials.password
    if username not in USER_DB or USER_DB[username] != password:
        raise HTTPException(
            status_code=status.HTTP_401_UNAUTHORIZED,
            detail="Unauthorized",
            headers={"WWW-Authenticate": "Basic"},
        )
    return username

@app.get("/")
def root():
    return {"message": "Welcome! Please authenticate to use actions."}

@app.get("/action1")
def action1(user: str = Depends(authenticate)):
    # Thực hiện tác vụ 1
    return {"user": user, "result": "Action 1 executed successfully"}

@app.get("/action2")
def action2(user: str = Depends(authenticate)):
    # Thực hiện tác vụ 2
    return {"user": user, "result": "Action 2 executed successfully"}
