def categorize_mom(summary, llm):
    prompt = f"""
    From the following meeting summary, extract a structured Minutes of Meeting (MoM)
    in valid JSON format with these keys:
    {{
      "Agenda": [],
      "Discussion Points": [],
      "Decisions": [],
      "Action Items": []
    }}

    Ensure JSON is well-formatted and parseable.
    Meeting Summary:
    {summary}
    """
    return llm.invoke(prompt).content
