"""server."""

from mcp.server.fastmcp import FastMCP

# Initialize FastMCP server
mcp = FastMCP("simple_calculator")


@mcp.tool()
def add(a: int, b: int) -> int:
    """Add two numbers together.

    Args:
        a: The first number to add.
        b: The second number to add.

    """
    return a + b


@mcp.tool()
def subtract(a: int, b: int) -> int:
    """Subtract two numbers.

    Args:
        a: The first number to subtract.
        b: The second number to subtract.

    """
    return a - b


@mcp.tool()
def multiply(a: int, b: int) -> int:
    """Multiplies two numbers.

    Args:
        a: The first number to multiply.
        b: The second number to multiply.

    """
    return a * b


if __name__ == "__main__":
    # Initialize and run the server
    mcp.run(transport="stdio")
