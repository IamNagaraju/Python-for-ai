import logging

from fastapi import FastAPI

logger = logging.getLogger("ai_resume_analyzer")
logger.setLevel(logging.INFO)


def add_logging_middleware(app: FastAPI) -> None:
    @app.middleware("http")
    async def log_requests(request, call_next):
        logger.info("Request: %s %s", request.method, request.url.path)
        response = await call_next(request)
        logger.info("Response status: %s", response.status_code)
        return response
