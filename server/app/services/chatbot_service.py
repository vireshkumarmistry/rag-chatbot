import openai
import logging

from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import Pinecone
from langchain.chains.retrieval_qa.base import RetrievalQA
from langchain_community.chat_models import ChatOpenAI

from app.core.config import settings


def pinecone_vector_service(query, index_name):
    """
    Generates a chatbot response for a given query using a retrieval-based
    question-answering (QA) model.

    The function utilizes OpenAI embeddings and a Pinecone vector store to search
    for relevant documents from an existing index. It then uses the GPT-4 model
    to provide a response based on the retrieved information. If no relevant data
    is found, it logs a warning and returns None. The function handles both
    ValueError and general exceptions, logging any errors that occur.

    Args:
        query (str): The user's input query that needs to be processed by the chatbot.
        index_name (str): The name of the Pinecone index where document embeddings are stored.

    Returns:
        str: The generated response from the chatbot based on the retrieved documents.
        None: If no relevant data is found for the query.

    Raises:
        ValueError: If there is an issue with the input query or embedding process
                    or unexpected error occurs during the chatbot interaction.
    """
    try:
        embeddings = OpenAIEmbeddings(openai_api_key=settings.OPENAI_API_KEY)
        docsearch = Pinecone.from_existing_index(index_name, embeddings)

        qa_chain = RetrievalQA.from_chain_type(
            llm=ChatOpenAI(model="gpt-4", openai_api_key=settings.OPENAI_API_KEY),
            chain_type="stuff",
            retriever=docsearch.as_retriever(),
        )

        response = qa_chain.run(query)
        if not response:
            logging.warning(f"No relevant data found for query: {query}")
            return None

        return response

    except ValueError as e:
        logging.error(f"Invalid input or embeddings error: {str(e)}")
        raise ValueError("Failed to retrieve relevant data or process query.")

    except Exception as e:
        logging.error(f"Error during chatbot response generation: {str(e)}")
        raise ValueError("An unexpected error occurred during the chatbot interaction.")


def chat_bot(message: str):
    try:
        # Setting API Key
        client = openai.OpenAI(api_key=settings.OPENAI_API_KEY)

        completion = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": "You are a helpful assistant."},
                {
                    "role": "user",
                    "content": message
                }
            ]
        )

        return completion.choices[0].message.content
    except Exception as exp:
        logging.error(f"ChatBot OpenAI error: {str(exp)}")
        raise Exception("Something went wrong!!! Please try again.")
