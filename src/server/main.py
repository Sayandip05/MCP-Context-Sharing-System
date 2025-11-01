from fastmcp import FastMCP

# Initialize FastMCP server and context storage
mcp = FastMCP("Context Sharing Server")
context_store = {}

@mcp.tool()
def share_context(agent: str, content: str) -> dict:
    """
    Store context from a specified agent.
    
    Args:
        agent: Name of the agent storing context
        content: Context content to store
    """
    if agent not in context_store:
        context_store[agent] = []
    context_store[agent].append(content)
    return {"result": f"Context stored from {agent}: {content}"}

@mcp.tool()
def retrieve_context(query: str) -> dict:
    """
    Retrieve all stored context entries matching the query text.
    
    Args:
        query: Search query to find matching contexts
    """
    matching = []
    for agent, contents in context_store.items():
        for content in contents:
            if query.lower() in content.lower():
                matching.append({"agent": agent, "content": content})
    
    if not matching:
        return {"result": f"No context found matching query: {query}"}
    return {"result": matching}

@mcp.tool()
def list_all_context() -> dict:
    """
    Return the full context store with contexts from all agents.
    """
    return {"result": context_store}

if __name__ == "__main__":
    mcp.run(transport="sse", port=3000)