# CrewAI RAG Project

This project implements a **Retrieval-Augmented Generation (RAG)** pipeline using **CrewAI**, **LangChain**, and **Chroma**.  
It allows you to ingest PDF documents into a vector database and query them using an AI agent.

---

## Project Overview

The project has two main agents/tools:

1. **VectorMaker Tool**  
   - Loads all PDF files in the `resources/` folder.  
   - Splits the content into chunks for better processing.  
   - Generates embeddings using OpenAIEmbeddings.  
   - Stores the embeddings in a Chroma vector database (`vector_db/`) for fast similarity search.  

2. **Retrieval Tool**  
   - Accepts a user question.  
   - Performs a similarity search on the vector database.  
   - Generates a relevant answer using the retrieved chunks.

This setup allows you to **ask questions about any PDF** in your resources folder and get meaningful answers.  

---

## Current PDF

The current PDF in the `resources/` folder is **my favorite book, "Too Good to Be True"**, which is used as the main source for testing the RAG system. You can ask questions about its content, themes, or any details in the book, and the agent will respond using the vector database.

---

## How to Use

1. Place PDFs in the `resources/` folder.  
2. Run the ingestion task to build the vector database:

```bash
uv add -u requirmen6s.txt
crewai run 
```
### Customizing

**Add your `OPENAI_API_KEY` into the `.env` file**

- Modify `src/rag/config/agents.yaml` to define your agents
- Modify `src/rag/config/tasks.yaml` to define your tasks
- Modify `src/rag/crew.py` to add your own logic, tools and specific args
- Modify `src/rag/main.py` to add custom inputs for your agents and tasks

## Running the Project

To kickstart your crew of AI agents and begin task execution, run this from the root folder of your project:

```bash
$ crewai run
```

This command initializes the RAG Crew, assembling the agents and assigning them tasks as defined in your configuration.

This example, unmodified, will run the create a `report.md` file with the output of a research on LLMs in the root folder.

## Understanding Your Crew

The RAG Crew is composed of multiple AI agents, each with unique roles, goals, and tools. These agents collaborate on a series of tasks, defined in `config/tasks.yaml`, leveraging their collective skills to achieve complex objectives. The `config/agents.yaml` file outlines the capabilities and configurations of each agent in your crew.

## Support

For support, questions, or feedback regarding the Rag Crew or crewAI.
- Visit our [documentation](https://docs.crewai.com)
- Reach out to us through our [GitHub repository](https://github.com/joaomdmoura/crewai)
- [Join our Discord](https://discord.com/invite/X4JWnZnxPb)
- [Chat with our docs](https://chatg.pt/DWjSBZn)

Let's create wonders together with the power and simplicity of crewAI.
