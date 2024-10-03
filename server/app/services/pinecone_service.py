import openai
import logging

import pinecone
from pinecone import Pinecone, ServerlessSpec
from app.utils.config import PINECONE_API_KEY
from utils.config import OPENAI_API_KEY

pc = Pinecone(api_key=PINECONE_API_KEY)
openai.api_key = OPENAI_API_KEY

index_name = "text-embedding-ada-002"


def create_pinecone_index(index_name, text_chunks):
    """
    Creates or retrieves a Pinecone index, generates embeddings for a list of text chunks
    using OpenAI, and upserts the embeddings into the Pinecone index.

    Args:
        index_name (str): The name of the Pinecone index to create or retrieve.
        text_chunks (list of str): A list of text strings for which embeddings will be generated
                                   and inserted into the Pinecone index.

    Raises:
        ValueError: Raised if the Pinecone index creation or upsertion of embeddings fails,
                    or if there is an error generating embeddings via the OpenAI API.

    Returns:
        None
    """
    try:
        try:
            pc.create_index(
                name=index_name,
                dimension=1536,
                metric="cosine",
                spec=ServerlessSpec(cloud="aws", region="us-east-1"),
            )
            index = pc.Index(index_name)
        except pinecone.exceptions.PineconeException:
            logging.info(
                f"Pinecone index '{index_name}' already exists. Using the existing index."
            )
            index = pc.Index(index_name)

        vectors_to_upsert = []
        for i, chunk in enumerate(text_chunks):
            # OpenAI to get embeddings
            response = openai.embeddings.create(
                input=chunk, model="text-embedding-ada-002"
            )
            embedding = response.data[0].embedding
            vectors_to_upsert.append((str(i), embedding, {"text": chunk}))

        # Upsert embeddings in bulk
        if vectors_to_upsert:
            index.upsert(vectors=vectors_to_upsert)
            logging.info(
                f"Successfully upserted {len(vectors_to_upsert)} vectors into index: {index_name}"
            )
        else:
            logging.warning("No vectors to upsert. The text chunks might be empty.")

    except pinecone.exceptions.PineconeException as exp:
        logging.error(f"Pinecone error: {str(exp)}")
        raise ValueError("Failed to create Pinecone index or upsert embeddings.")

    except openai.OpenAIError as e:
        logging.error(f"OpenAI API error: {str(e)}")
        raise ValueError("Failed to generate embeddings using OpenAI.")

    except Exception as e:
        logging.error(f"Error creating Pinecone index: {str(e)}")
        raise ValueError("An unexpected error occurred while creating Pinecone index.")
