FINALAI – Intelligent Multi-Tool Assistant

FINALAI is a smart AI assistant that can interact with users, answer questions, and automate tasks like generating meeting summaries (MoM), sending emails, and applying for leave via an internal portal. The system uses a modular graph-based architecture with memory, so it can remember previous interactions and decide dynamically which tool or action to execute based on user input.

Features:

Dynamic Decision Routing:

Uses an LLM to decide whether a user query requires chatting normally, generating a Minutes of Meeting (MoM) from a video, sending an email, or applying leave.

Routes the request to the appropriate tool automatically.

MoM Generator:

Extracts audio from a meeting video

Transcribes the audio

Summarizes the transcript

Categorizes key action points

Returns a structured MoM summary

Email Automation:

Send emails using Gmail SMTP

Supports plain text and HTML content

Remembers context from previous interactions

Leave Application:

Automates leave submission via an internal HR portal using Playwright

Selects leave type, start and end dates, and submits the request

Memory & Persistent Context:

All interactions are stored via MemorySaver

The assistant remembers previous queries and actions

Allows seamless multi-turn conversations

Extensible Graph-Based Architecture:

Each tool/action is a node in a StateGraph

Decision nodes route requests dynamically

Easy to add new tools or automation workflows

Installation:

Clone the repository.

Create a virtual environment and install dependencies using pip or uv install.

Create a .env file with your credentials including USER_EMAIL, APPPASSWORD, LEAVE_URL, USER_NAME, and USER_PASSWORD.

Usage:

Run the assistant using "uv run main.py".

Example interactions:

Chat: ask general questions.

MoM: provide a meeting video path to summarize and categorize action points.

Email: send an email by providing receiver, subject, and body.

Leave: apply leave by providing start and end dates.

Project Structure:

FINALAI/

main.py: Entry point to run the assistant

Graph.py: Builds the intelligent decision graph

MOMgraph.py: Graph for MoM workflow

tools/: Folder containing automation tools such as email_tool.py, leave_tool.py, extract_audio.py, transcription_tool.py, summarization_tool.py, and categorization_tool.py

.env: Environment variables (not tracked in git)

README.md: This documentation

Dependencies:

Python 3.12+

LangGraph

LangChain

Playwright

Pydantic

Gmail account for email automation

Internal HR portal credentials for leave automation

Notes:

By default, if the LLM cannot detect a tool-specific request, it will answer the question normally as a chat response.

The assistant uses threaded memory, so it can maintain context across multiple interactions.

MoM workflow currently supports video input in formats supported by extract_audio.

Future Enhancements:

Add more automation tools such as Slack notifications or Jira ticket creation

Support for multiple video formats in MoM workflow

Improved LLM prompts for more accurate tool detection