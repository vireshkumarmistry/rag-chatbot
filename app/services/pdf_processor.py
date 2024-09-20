from PyPDF2 import PdfReader
import logging


def extract_text_from_pdf(pdf_file):
    """
    Extracts text from a given PDF file.

    This function reads the provided PDF file using `PyPDF2.PdfReader` and
    concatenates the text from all pages.

    Args:
        pdf_file (str or file-like object): The path to the PDF file or a
                                            file-like object containing the PDF.

    Returns:
        str: The extracted text from the PDF.

    Raises:
        ValueError: If no text is extracted or an error occurs during extraction.
    """
    try:
        reader = PdfReader(pdf_file)
        text = ""
        for page in reader.pages:
            text += page.extract_text()
        if not text:
            raise ValueError(
                "Extracted text is empty. PDF content may be corrupted or non-readable."
            )
        return text
    except Exception as e:
        logging.error(f"Error extracting text from PDF: {str(e)}")
        raise ValueError("Failed to extract text from PDF.")


def split_text_into_chunks(text, chunk_size=500):
    """
    Splits a given text into smaller chunks of a specified size.

    This function splits the input text into chunks, with each chunk containing
    a maximum number of words specified by `chunk_size`. The resulting list of
    text chunks is returned. If splitting fails, a ValueError is raised.

    Args:
        text (str): The input text to be split into chunks.
        chunk_size (int, optional): The number of words per chunk. Default is 500.

    Returns:
        list: A list of text chunks, each containing up to `chunk_size` words.

    Raises:
        ValueError: If splitting fails or the result is empty.
    """
    try:
        words = text.split()
        chunks = [
            " ".join(words[i : i + chunk_size])
            for i in range(0, len(words), chunk_size)
        ]
        if not chunks:
            raise ValueError("Failed to split text into chunks.")
        return chunks
    except Exception as e:
        logging.error(f"Error splitting text into chunks: {str(e)}")
        raise ValueError("Error occurred while splitting text into chunks.")
