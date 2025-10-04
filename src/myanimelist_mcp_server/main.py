from mcp.server.fastmcp import FastMCP
from tools.tools import register_tools

mcp = FastMCP("myanimelist")
register_tools(mcp)

def main():
  mcp.run(transport="stdio")

if __name__ == "__main__":
  main()
