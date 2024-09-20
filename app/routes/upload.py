import logging
from io import BytesIO
from fastapi import APIRouter, UploadFile, File, HTTPException
from starlette import status
from starlette.responses import JSONResponse

from app.services.pdf_processor import extract_text_from_pdf, split_text_into_chunks
from app.services.pinecone_service import create_pinecone_index

router = APIRouter()


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Handles PDF file uploads, extracts text from the PDF, processes the text into chunks,
    and creates or updates a Pinecone index with the extracted data.

    Args:
        file (UploadFile): The uploaded PDF file provided via the request. The file's content type is validated to ensure it's a PDF.

    Returns:
        JSONResponse: A JSON response containing a success message if the file is uploaded and processed successfully,
                      or an error message in case of failure, along with the appropriate HTTP status code.

    Raises:
        HTTPException: Raised if:
            - The uploaded file is not a PDF (status code 400).
            - The text extraction from the PDF fails (status code 400).
            - The splitting of text into chunks fails (status code 500).
            - An unexpected error occurs during the upload process (status code 500).

    Logging:
        - Logs a warning if an invalid file type is uploaded.
        - Logs errors when text extraction or text splitting fails.
        - Logs errors for HTTP exceptions and unexpected exceptions during the upload process.

    Example Success Response:
        - HTTP 200: {"message": "Document 'filename.pdf' has been successfully uploaded and processed."}

    Example Failure Responses:
        - HTTP 400: {"detail": "Invalid file type. Please upload a PDF."}
        - HTTP 400: {"detail": "Failed to extract text from PDF. The document might be empty or corrupted."}
        - HTTP 500: {"detail": "Error processing the document. Unable to split the text."}
        - HTTP 500: {"detail": "An error occurred while uploading the PDF. Please try again later."}
    """
    try:
        if file.content_type != "application/pdf":
            logging.warning(
                f"Invalid file type attempted to upload: {file.content_type}"
            )
            raise HTTPException(
                status_code=400, detail="Invalid file type. Please upload a PDF."
            )

        pdf_content = await file.read()
        text = extract_text_from_pdf(BytesIO(pdf_content))
        if not text:
            logging.error("Failed to extract text from the uploaded PDF.")
            raise HTTPException(
                status_code=400,
                detail="Failed to extract text from PDF. The document might be empty or corrupted.",
            )

        text_chunks = split_text_into_chunks(text)
        if not text_chunks:
            logging.error("Failed to split the extracted text into chunks.")
            raise HTTPException(
                status_code=500,
                detail="Error processing the document. Unable to split the text.",
            )

        index_name = file.filename.split(".")[0]
        create_pinecone_index(index_name.lower(), text_chunks)

        return JSONResponse(
            content={
                "message": f"Document '{file.filename}' has been successfully uploaded and processed."
            },
            status_code=status.HTTP_200_OK,
        )

    except HTTPException as exp:
        logging.error(f"HTTP Exception: {exp.detail}")
        raise exp

    except Exception as exp:
        logging.error(f"An unexpected error occurred during PDF upload: {str(exp)}")
        raise HTTPException(
            status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
            detail="An error occurred while uploading the PDF. Please try again later.",
        )
