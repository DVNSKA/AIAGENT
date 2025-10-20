from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field


class RETRIVER(BaseModel):
    """INput schema for RETRIVER."""
    message: str = Field(..., description="The message that needs to be searched for relevant text chunks in vectore db.")

class RETRIVERTOOL(BaseTool):
    

    name: str = "RETRIVER"
    description: str = (
        "This tool is used Returns top 3 relevant text chunks for a query using similarity search.."
    )
    args_schema: Type[BaseModel] = RETRIVER

    def _run(self, message: str) -> str:
        embeddings = OpenAIEmbeddings()
        resource_dir="resources"
        persist_dir="vector_db"
        vectordb = Chroma(persist_directory=persist_dir, embedding_function=embeddings)

        results = vectordb.similarity_search(message, k=3)
        context = "\n\n".join([doc.page_content for doc in results])

        return context

