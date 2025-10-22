from langgraph.graph import StateGraph, END
from langgraph.checkpoint.memory import MemorySaver
from langchain_openai import ChatOpenAI
from MOMgraph import FINALAI
from tools.email_tool import send_email
from tools.leave_tool import apply_leave
from pydantic import BaseModel
from typing import Optional

# LLMs
router_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0)
chat_llm = ChatOpenAI(model="gpt-4o-mini", temperature=0.7)

# ================================================================
# 🧱 State Model
# ================================================================
class GlobalState(BaseModel):
    user_input: str
    task_type: Optional[str] = None
    video_path: Optional[str] = None
    receiver_email: Optional[str] = None
    subject: Optional[str] = None
    text_body: Optional[str] = None
    start_day: Optional[str] = None
    end_day: Optional[str] = None
    result: Optional[str] = None


# ================================================================
# 🧩 Graph Builder
# ================================================================
def build_intelligent_graph():
    graph = StateGraph(state_schema=GlobalState)

    # ============================================================
    # 🤖 Decision Node: determine task
    # ============================================================
    def decision_node(state):
        prompt = f"""
        You are an intelligent assistant that can either chat normally or trigger tools.

        Tools available:
        1. "mom" - Create Minutes of Meeting (MoM) from a meeting video.
        2. "email" - Send an email.
        3. "leave" - Apply for leave using an internal HR portal.

        Return ONLY the tool name if clearly requested.
        Return "chat" if the user is just asking a question.

        User request: {state.user_input}
        """
        decision_msg = router_llm.invoke(prompt)  # returns AIMessage
        decision = decision_msg.content.strip().lower()

        print(f"🧭 LLM Decision: {decision}")
        return {"task_type": decision}

    graph.add_node("decision", decision_node)

    # ============================================================
    # 💬 Chat Node (default)
    # ============================================================
    def chat_node(state):
        response = chat_llm.invoke(state.user_input)
        return {"result": response}

    graph.add_node("chat", chat_node)

    # ============================================================
    # 📧 Email Node
    # ============================================================
    def send_email_node(state):
        if not state.receiver_email or not state.subject:
            return {"result": "Missing email details."}
        status = send_email(state.receiver_email, state.subject, state.text_body)
        return {"result": status}

    graph.add_node("email", send_email_node)

    # ============================================================
    # 🗓️ Leave Node
    # ============================================================
    def apply_leave_node(state):
        if not state.start_day or not state.end_day:
            return {"result": "Missing leave dates."}
        status = apply_leave(state.start_day, state.end_day)
        return {"result": status}

    graph.add_node("leave", apply_leave_node)

    # ============================================================
    # 🧾 MoM Node (wrap entire subgraph)
    # ============================================================
    def mom_entry_node(state):
        mom_graph_instance = FINALAI()
        result = mom_graph_instance.invoke({"video_path": state.video_path})
        return {"result": result}

    graph.add_node("mom_entry", mom_entry_node)

    # ============================================================
    # 🧩 Router function for decision
    # ============================================================
    def decision_router(state: GlobalState):
        task = state.task_type
        if task == "mom":
            return "mom_entry"
        elif task == "email":
            return "email"
        elif task == "leave":
            return "leave"
        else:
            return "chat"


    # ============================================================
    # 🧩 Define edges
    # ============================================================
    graph.set_entry_point("decision")
    graph.add_conditional_edges(
        "decision",
        decision_router,
        {
            "mom_entry": "mom_entry",
            "email": "email",
            "leave": "leave",
            "chat": "chat"
        }
    )

    # End points
    graph.add_edge("chat", END)
    graph.add_edge("email", END)
    graph.add_edge("leave", END)
    graph.add_edge("mom_entry", END)

    return graph
