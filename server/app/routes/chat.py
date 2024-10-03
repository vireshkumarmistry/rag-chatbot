from fastapi import APIRouter, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from app.models.request_models import PineconeVectorChatRequest, ChatRequest
from app.services.chatbot_service import pinecone_vector_service, chat_bot
import logging

router = APIRouter()


@router.post("/")
async def chatbot(chat_request: ChatRequest):
    try:
        response = chat_bot(chat_request.message)
        return JSONResponse(content={"message": response}, status_code=status.HTTP_200_OK)
    except Exception:
        raise HTTPException(status_code=500, detail="Something went wrong!! Please Try Again.")


@router.post("/pinecone_vector_chat")
async def pinecone_vector_chat(chat_request: PineconeVectorChatRequest):
    """
    Handles POST requests to the chatbot API, processes a user's query, and returns the chatbot's response.

    Args:
        chat_request (PineconeVectorChatRequest): A request object containing the user's query and the Pinecone index name.

    Returns:
        JSONResponse: A JSON response containing the chatbot's message with HTTP status 200 if successful,
                      or a JSON error message with the relevant HTTP status code for exceptions.

    Raises:
        HTTPException: Raised if:
            - An HTTP-related error occurs.
            - A ValueError is raised due to invalid inputs (query or index name).
            - A generic exception occurs during chatbot interaction.

    Logging:
        - Logs warnings if no relevant data is found for the query.
        - Logs errors for HTTP exceptions, invalid input errors, or any unexpected exceptions during chatbot interaction.

    Example JSON response:
        - On success: {"message": "Chatbot's response"}
        - On failure: {"message": "Sorry, I couldn't find relevant information in the document."}

    """
    try:
        response = pinecone_vector_service(chat_request.query, chat_request.index_name.lower())
        if response:
            return JSONResponse(
                content={"message": response}, status_code=status.HTTP_200_OK
            )
        else:
            logging.warning(f"No relevant data found for query: {chat_request.query}")
            return JSONResponse(
                content={
                    "message": "Sorry, I couldn't find relevant information in the document."
                },
                status_code=status.HTTP_200_OK,
            )

    except HTTPException as e:
        logging.error(f"HTTP Exception: {e.detail}")
        raise e

    except ValueError as e:
        logging.error(f"Invalid input error: {str(e)}")
        raise HTTPException(
            status_code=400,
            detail="Invalid query or index name. Please provide valid inputs.",
        )

    except Exception as e:
        logging.error(f"An error occurred during chatbot interaction: {str(e)}")
        raise HTTPException(
            status_code=500,
            detail="An error occurred while processing your request. Please try again later.",
        )
