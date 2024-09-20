# RAG Chatbot with FastAPI

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot using **FastAPI**. It allows users to upload a PDF document, store its text embeddings in **Pinecone**, and interact with a chatbot powered by **OpenAI GPT-4**, which retrieves relevant passages from the document to answer user queries.

## Features

- Upload a PDF document for ingestion.
- Store text embeddings in **Pinecone** for fast retrieval.
- Retrieve relevant document passages to answer questions using **OpenAI GPT-4**.
- Fallback mechanism if the chatbot cannot find relevant information.
- Efficient and scalable architecture.

## Project Structure

```
rag-chatbot/
│
├── app/
│   ├── __init__.py
│   ├── main.py
│   ├── routes/
│   │   ├── __init__.py
│   │   ├── upload.py
│   │   ├── chat.py
│   ├── services/
│   │   ├── __init__.py
│   │   ├── pdf_processor.py
│   │   ├── pinecone_service.py
│   │   ├── chatbot_service.py
│   ├── models/
│   │   ├── __init__.py
│   │   ├── request_models.py
│   └── utils/
│       ├── __init__.py
│       ├── config.py
│
├── .env
├── requirements.txt
└── README.md
```

## Requirements

- Python 3.8+
- **Pinecone** account and API key
- **OpenAI** API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/rag-chatbot.git
cd rag-chatbot
```

### 2. Create a Python Virtual Environment

It's a good practice to create a virtual environment for your project. You can use `venv` to create one:

```bash
python -m venv venv
```

### 3. Activate the Virtual Environment

- On Windows:

  ```bash
  venv\Scripts\activate
  ```

- On macOS and Linux:

  ```bash
  source venv/bin/activate
  ```

### 4. Set Up Environment Variables

Create a `.env` file in the root of the project with the following content:

```bash
PINECONE_API_KEY=your_pinecone_api_key
OPENAI_API_KEY=your_openai_api_key
```

Replace `your_pinecone_api_key`, and `your_openai_api_key` with your actual API keys.

### 5. Install Dependencies

Use `pip` to install the required dependencies:

```bash
pip install -r requirements.txt
```

### 6. Run the FastAPI Application

To start the FastAPI server, run:

```bash
uvicorn app.main:app --reload
```

The server will be available at `http://127.0.0.1:8000`.

## API Endpoints

### 1. Upload a PDF Document

**Endpoint**: `POST /upload/`

**Description**: Upload a PDF document, extract its text, create a Pinecone index, and store the text embeddings.

#### Request

```bash
curl -X POST "http://127.0.0.1:8000/upload/" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@ZIGUP-FY24-Results-Deck.pdf"
```

#### Response

```json
{
  "message": "Document 'ZIGUP-FY24-Results-Deck.pdf' has been successfully uploaded and processed."
}
```

### 2. Chat with the Bot

**Endpoint**: `POST /chat/`

**Description**: Ask a question based on the uploaded document. The chatbot will retrieve relevant text from the document using the **Pinecone** index and respond using **GPT-4**.

#### Request

```bash
curl -X POST "http://127.0.0.1:8000/chat/" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"query": "What was UK&I Rental profit in FY2024?", "index_name": "ZIGUP-FY24-Results-Deck"}'
```

#### Response

```json
{
  "response": "The UK&I Rental profit in FY2024 was £X million."
}
```

If the query cannot be answered, the response might be:

```json
{
  "response": "Sorry, I couldn't find relevant information in the document."
}
```

## Project Structure Explained

- **app/main.py**: The FastAPI entry point that includes the upload and chat routes.
- **app/routes/upload.py**: Handles the PDF upload and ingestion.
- **app/routes/chat.py**: Manages chatbot interactions.
- **app/services/**:
  - **pdf_processor.py**: Extracts and processes text from the uploaded PDF.
  - **pinecone_service.py**: Creates a Pinecone index and stores text embeddings.
  - **chatbot_service.py**: Handles interaction with GPT-4 for generating answers.
- **app/models/request_models.py**: Pydantic models for validating request payloads.
- **app/utils/config.py**: Manages environment variables for API keys.

