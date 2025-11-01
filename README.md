# MCP Context Sharing Server

A Model Context Protocol (MCP) server for sharing context between multiple agents.

## Features

- **Share Context**: Store context from any agent
- **Retrieve Context**: Search and retrieve stored contexts
- **List All Context**: View all stored contexts from all agents

## Installation

```bash
pip install fastmcp
```

## Running the Server

```bash
python src\server\main.py
```

The server will start with SSE transport at: `http://localhost:3000/sse`

## Using MCP Inspector

To test and interact with your server using the MCP Inspector:

1. Make sure your server is running
2. Open a new terminal and run:
   ```bash
   npx @modelcontextprotocol/inspector
   ```
3. The Inspector will open at `http://localhost:6274`
4. Connect to your server using SSE transport with URL: `http://localhost:3000/sse`

## Available Tools

### share_context
Store context from a specified agent.

**Parameters:**
- `agent` (string): Name of the agent storing context
- `content` (string): Context content to store

### retrieve_context
Retrieve all stored context entries matching a query.

**Parameters:**
- `query` (string): Search query to find matching contexts

### list_all_context
Return the full context store with contexts from all agents.

**Parameters:** None

## Example Usage

Once connected via MCP Inspector:

1. **Share Context**: Use `share_context` tool with agent="Agent1", content="This is some context"
2. **Retrieve Context**: Use `retrieve_context` tool with query="some"
3. **List All**: Use `list_all_context` to see all stored contexts

"# MCP-Context-Sharing-System" 
