from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.ingest_tool import VECTORMAKERTOOL
from .tools.retrieval_tool import RETRIVERTOOL
@CrewBase
class Rag():
    """Rag crew"""

    agents: List[BaseAgent]
    tasks: List[Task]
    @agent
    def ingestion_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['ingestion_agent'],
             tools=[VECTORMAKERTOOL()], # type: ignore[index]
            verbose=True
        )

    @agent
    def retrieval_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['retrieval_agent'],
             tools=[RETRIVERTOOL()], # type: ignore[index]
            verbose=True
        )
    
    @task
    def ingestion_task(self) -> Task:
        return Task(
            config=self.tasks_config['ingestion_task'], # type: ignore[index]
        )

    @task
    def retrieval_task(self) -> Task:
        return Task(
            config=self.tasks_config['retrieval_task'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Rag crew"""
        # To learn how to add knowledge sources to your crew, check out the documentation:
        # https://docs.crewai.com/concepts/knowledge#what-is-knowledge

        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.sequential,
            verbose=True,
            # process=Process.hierarchical, # In case you wanna use that instead https://docs.crewai.com/how-to/Hierarchical/
        )
