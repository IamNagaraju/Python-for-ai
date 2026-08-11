from fastapi import FastAPI

from app.routers.resume import router as resume_router

app = FastAPI(
    title="AI Resume Analyzer",
    version="1.0.0"
)

app.include_router(resume_router)