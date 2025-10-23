from mcp.server.fastmcp import FastMCP
from mom_tool import generate_mom_impl as _generate_mom
from email_tool import send_email as _send_email
from leave_tool import apply_leave as _apply_leave
import asyncio

mcp = FastMCP("ABHI MCP Server")

@mcp.tool()
async def send_email(receiver_email: str, subject: str, text_body: str) -> str:
    """
    Sends an email using Gmail SMTP.

    Args:
        receiver_email (str): Recipient's email address.
        subject (str): Email subject.
        text_body (str): Plain text version of the email.
        html_body (str, optional): HTML version of the email.
    
    Returns: email sending status.
    """

    # send_email is a blocking sync function (smtplib) — run in a thread
    return await asyncio.to_thread(_send_email, receiver_email, subject, text_body)

@mcp.tool()
async def apply_leave(start_day: str, end_day: str) -> str:
    """Apply Leave.

    Args:
        start_day (str): The start date only day name (e.g., "15")
        end_day (str): The end date only day name (e.g., "20")
    """
    
    # apply_leave uses Playwright sync API and is blocking; run it in a thread
    return await asyncio.to_thread(_apply_leave, start_day, end_day)

@mcp.tool()
async def generate_mom(path: str) -> str:
    """it generates mom(minutes of minutes).

    Args:
        path: path of meeting
       
      """
    # _generate_mom is async; await it
    return await _generate_mom(path)


if __name__ == "__main__":
    mcp.run(transport='stdio')