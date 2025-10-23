from mcp.server.fastmcp import resource

@resource("company://info/{query}")
async def company_info(query: str) -> str:
    """Fetch company information or policy details (RAG-like behavior).

    Args:
        query: The topic or question about the company.
    """
    # TODO: Integrate a real RAG pipeline here
    # For now, return placeholder
    if "policy" in query.lower():
        return "Company policy: We prioritize innovation and work-life balance."
    elif "founder" in query.lower():
        return "Founded in 2020 by Abhiram Pabbisetty."
    else:
        return f"Company info placeholder for query: {query}"
