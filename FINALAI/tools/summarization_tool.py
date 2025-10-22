def summarize_text(text, llm):
    prompt = f"""
    You are a professional meeting assistant.
    Summarize the following meeting transcript clearly and concisely, highlighting:
    - Key discussion points
    - Decisions made
    - Action items
    - Deadlines (if any)

    Transcript:
    {text}
    """
    return llm.invoke(prompt).content
