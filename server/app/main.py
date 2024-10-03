import logging

from fastapi import FastAPI
from fastapi.responses import JSONResponse
from fastapi.middleware.cors import CORSMiddleware
from starlette import status

from app.routes import upload, chat

app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(upload.router, prefix="/api/v1/upload", tags=["Upload"])
app.include_router(chat.router, prefix="/api/v1/chatbot", tags=["Chat"])


@app.get("/")
async def root():
    """Default Router for RAG Chatbot Running Status"""
    return JSONResponse(
        status_code=status.HTTP_200_OK,
        content={"message": "RAG Chatbot API is running"},
    )


@app.exception_handler(Exception)
async def global_exception_handler(exc: Exception):
    """Global exception handler"""
    logging.error(f"Unhandled error occurred: {exc}")
    return JSONResponse(
        status_code=500,
        content={
            "message": "An internal server error occurred. Please try again later."
        },
    )
