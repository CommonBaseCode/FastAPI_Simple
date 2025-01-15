from fastapi import FastAPI
from app.routes import router
from app.database import engine
from app.models import Base
import uvicorn

# Creating a Database Table
Base.metadata.create_all(bind=engine)

app = FastAPI()

# Router Registration
app.include_router(router, prefix="/users", tags=["Users"])

@app.get("/")
def read_root():
    return {"message": "Welcome to the REST API!"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000, log_level="info")