from pydantic import BaseModel


class ChatRequest(BaseModel):
    """
    A Pydantic model representing the structure of the chat request input.

    Attributes:
        query (str): The user's input query to be processed by the chatbot.
        index_name (str): The name of the Pinecone index where the chatbot will search for relevant information.
    """

    query: str
    index_name: str
