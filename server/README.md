# RAG Chatbot

This project implements a **Retrieval-Augmented Generation (RAG)** chatbot using **FastAPI**. The application allows users to upload a PDF document, store its text embeddings in **Pinecone**, and interact with a chatbot powered by **OpenAI GPT-4**. The chatbot retrieves relevant passages from the document to answer user queries, enhancing the response generation process with context from the document.

## Features

- Upload a PDF document for ingestion.
- Store text embeddings in **Pinecone** for fast retrieval.
- Chatbot functionality to interact with the user, answering queries using **OpenAI GPT-4**.
- Retrieves relevant document passages to improve the accuracy of the answers.
- Fallback mechanism if the chatbot cannot find relevant information in the document.
- Efficient and scalable architecture.

## Chatbot Functionality

The core functionality of this project is its **chatbot**, which enhances the user experience by combining document retrieval with **OpenAI GPT-4** to generate accurate, context-aware responses.

### How it Works:

1. **User Query**: The user submits a query to the chatbot.
2. **Document Retrieval via Pinecone**: The system retrieves relevant text passages from the uploaded document using Pinecone's vector search. These passages are selected based on their relevance to the user's query.
3. **Response Generation via GPT-4**: The relevant document excerpts are combined with the query and sent to **OpenAI GPT-4**. GPT-4 generates a response that incorporates the retrieved information for more accurate and context-aware answers.
4. **Fallback Handling**: If the system cannot find any relevant passages in the document, the chatbot informs the user that it couldn't find the information.

This functionality provides a highly interactive way for users to gain insights from their documents using a powerful combination of retrieval and generation techniques.

## Project Structure

```
├── app
│   ├── __init__.py
│   ├── main.py
│   ├── models
│   │   ├── __init__.py
│   │   └── request_models.py
│   ├── routes
│   │   ├── __init__.py
│   │   ├── chat.py
│   │   └── upload.py
│   ├── services
│   │   ├── chatbot_service.py
│   │   ├── __init__.py
│   │   ├── pdf_processor.py
│   │   └── pinecone_service.py
│   └── utils
│       ├── config.py
│       └── __init__.py
├── LICENSE
├── README.md
└── requirements.txt
```

## Requirements

- Python 3.8+
- **Pinecone** account and API key
- **OpenAI** API key

## Installation

### 1. Clone the Repository

```bash
git clone https://github.com/vireshkumarmistry/rag-chatbot
cd rag-chatbot/server/
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

### Using Docker

1. **Build Docker Image:**

   ```bash
   docker build -t server .
   ```

2. **Run the Application in Docker:**

   ```bash
   docker run -p 8000:8000 server
   ```

---

## API Endpoints

### 1. Upload a PDF Document

**Endpoint**: `POST /api/v1/upload/`

**Description**: Upload a PDF document, extract its text, create a Pinecone index, and store the text embeddings.

#### Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/upload/" \
-H "accept: application/json" \
-H "Content-Type: multipart/form-data" \
-F "file=@yourfile.pdf"
```

#### Response

```json
{
  "message": "Document 'yourfile.pdf' has been successfully uploaded and processed."
}
```

### 2. Chat with the Bot

**Endpoint**: `POST /api/v1/chatbot/`

**Description**: Ask a general question to the chatbot. The response will be generated using GPT-4.

#### Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/chatbot/" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"message": "Tell me something interesting!"}'
```

#### Response

```json
{
  "message": "Here is something interesting..."
}
```

### 3. Chat with Pinecone Vector Support

**Endpoint**: `POST /api/v1/chatbot/pinecone_vector_chat/`

**Description**: Ask a question based on an uploaded document. The chatbot will retrieve relevant text from the document using the Pinecone index and respond using GPT-4.

#### Request

```bash
curl -X POST "http://127.0.0.1:8000/api/v1/chatbot/pinecone_vector_chat/" \
-H "accept: application/json" \
-H "Content-Type: application/json" \
-d '{"query": "What was UK&I Rental profit in FY2024?", "index_name": "ZIGUP-FY24-Results-Deck"}'
```

#### Response

```json
{
  "message": "The UK&I Rental profit in FY2024 was £X million."
}
```

If the query cannot be answered, the response might be:

```json
{
  "message": "Sorry, I couldn't find relevant information in the document."
}
```

---
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

## Future Enhancements

- Add support for more document formats.
- Improve fallback handling with additional context.
- Expand support for multi-user document management and querying.

---