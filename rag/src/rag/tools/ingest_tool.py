
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma
import os
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel


class VECTORMAKER(BaseModel):
    """INPUT schema for VectorMaker."""


class VECTORMAKERTOOL(BaseTool):
    name: str = "VectorMaker"
    description: str = "This tool is used to create vector database."
    args_schema: Type[BaseModel] = VECTORMAKER

    def _run(self) -> str:
        resource_dir = "resources"
        persist_dir = "vector_db"
        os.makedirs(persist_dir, exist_ok=True)

        all_docs = []
        for file in os.listdir(resource_dir):
            if file.endswith(".pdf"):
                loader = PyPDFLoader(os.path.join(resource_dir, file))
                docs = loader.load()
                all_docs.extend(docs)

        splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=200)
        chunks = splitter.split_documents(all_docs)

        embeddings = OpenAIEmbeddings()
        vectordb = Chroma.from_documents(chunks, embeddings, persist_directory=persist_dir)
        vectordb.persist()
        print(f"✅ Ingested {len(chunks)} chunks into vector store at {persist_dir}")
        return "Ingestion complete!"
