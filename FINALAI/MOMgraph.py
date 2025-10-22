from langgraph.graph import StateGraph, END
from langchain_openai import ChatOpenAI
from tools.extract_audio import extract_audio
from tools.transcription_tool import transcribe_audio
from tools.summarization_tool import summarize_text
from tools.categorization_tool import categorize_mom
from pydantic import BaseModel
from typing import Optional, Dict, Any

llm = ChatOpenAI(model="gpt-4o", temperature=0)
class MoMState(BaseModel):
    video_path: str
    audio_path: Optional[str] = None
    transcript: Optional[str] = None
    summary: Optional[str] = None
    MoM: Optional[Dict[str, Any]] = None

def FINALAI():

    graph = StateGraph(state_schema=MoMState)
    

    # Step 1: Extract audio
    def extract_audio_node(state):
        video_path = state.video_path
        audio_path = extract_audio(video_path)
        return {"audio_path": audio_path}

    # Step 2: Transcribe
    def transcription_node(state):
        transcript = transcribe_audio(state.audio_path)
        return {"transcript": transcript}

    # Step 3: Summarize
    def summarization_node(state):
        summary = summarize_text(state.transcript, llm)
        return {"summary": summary}

    # Step 4: Categorize
    def categorize_node(state):
        categorized = categorize_mom(state.summary, llm)
        return {"MoM": categorized}

    # Register nodes
    graph.add_node("extract_audio", extract_audio_node)
    graph.add_node("transcription", transcription_node)
    graph.add_node("summarization", summarization_node)
    graph.add_node("categorization", categorize_node)

    # Define edges
    graph.set_entry_point("extract_audio")
    graph.add_edge("extract_audio", "transcription")
    graph.add_edge("transcription", "summarization")
    graph.add_edge("summarization", "categorization")
    graph.add_edge("categorization", END)

    return graph.compile()
