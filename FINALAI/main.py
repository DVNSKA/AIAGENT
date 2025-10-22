from langgraph.checkpoint.memory import MemorySaver
from Graph import build_intelligent_graph
from IPython.display import Image, display
if __name__ == "__main__":
    memory = MemorySaver()
    graph_builder = build_intelligent_graph()
    app = graph_builder.compile(checkpointer=memory)

    # Use a persistent UUID so it remembers your conversation
    config = {"configurable": {"thread_id": "abhiram-session"}}
    png_data = app.get_graph().draw_mermaid_png()
    with open("graph.png", "wb") as f:
        f.write(png_data)
    print("✅ Graph saved as graph.png")
    # 👇 Example 1: Ask to summarize a meeting video
    # result = app.invoke({"user_input": "hi who are you"}, config=config)
    # print(result)

    # 👇 Example 2: Ask to send an email — it will remember previous context
    # result = app.invoke({
    #     "user_input": "send an email to abhiram a ai joke ",
    #     "receiver_email": "pabbisettyabhiram@gmail.com",
    #     "subject": "Today's AI Joke",
    #     "text_body": "Here’s the summary we generated earlier."
    # }, config=config)
    result = app.invoke({
        "user_input": "apply leave for me ",
        "start_day": "25",
        "end_day": "26",
    }, config=config)
    print(result)
