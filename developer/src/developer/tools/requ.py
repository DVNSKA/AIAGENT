# developers/src/developers/tools/rag_tool.py
from crewai.tools import BaseTool
from typing import Type
from pydantic import BaseModel, Field
from pathlib import Path
import os
import importlib

from rag.main import run as rag_run  # uses your rag.main.run(query)


def _find_rag_root() -> Path:
    # Try to find a sibling 'rag' project with a pyproject.toml
    here = Path(__file__).resolve()
    for p in here.parents:
        cand = p / "rag"
        if (cand / "pyproject.toml").exists():
            return cand
    # Allow explicit override
    env = os.getenv("RAG_PROJECT_DIR")
    if env:
        return Path(env)
    # Fallback: try package location (not ideal if installed as wheel)
    try:
        pkg = importlib.import_module("rag")
        return Path(pkg.__file__).resolve().parents[2]
    except Exception:
        raise RuntimeError(
            "Could not locate rag project root. Set RAG_PROJECT_DIR to /path/to/rag."
        )


class RAGInput(BaseModel):
    argument: str = Field(..., description="Query or topic to run through the RAG crew.")


class RAGTool(BaseTool):
    name: str = "RAG"
    description: str = "Use this tool to search and extract relevant docs via the RAG crew."
    args_schema: Type[BaseModel] = RAGInput

    def _run(self, argument: str) -> str:
        print(f"🔍 Running RAG for: {argument}")
        try:
            rag_root = _find_rag_root()
            # Point RAG to the actual resources/persist dirs
            os.environ["RAG_RESOURCES_DIR"] = str(rag_root / "resources")
            os.environ["RAG_PERSIST_DIR"] = str(rag_root / "vector_db")

            result = rag_run(argument)
            return str(result) if result is not None else ""
        except Exception as e:
            return f"Error running RAG: {e}"