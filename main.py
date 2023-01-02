from fastapi import FastAPI
#install fastapi (pip) and uvicorn files
from fastapi.middleware.cors import CORSMiddleware
import Scripts.system as System

app = FastAPI()

origins = [
    "http://localhost:3000",
    "localhost:3000"
]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"]
)

@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.get("/api/uptime")
async def root():
    return System.uptime()