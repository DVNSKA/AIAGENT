from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
from .tools.RAG import RETRIVERTOOL
@CrewBase
class Developer():
    """Developer crew"""

    agents: List[BaseAgent]
    tasks: List[Task]

    @agent
    def python_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['python_developer'], # type: ignore[index]
            verbose=True
        )

    @agent
    def javascript_developer(self) -> Agent:
        return Agent(
            config=self.agents_config['javascript_developer'], # type: ignore[index]
            verbose=True
        )
    
    @agent
    def search_agent(self) -> Agent:
        return Agent(
            config=self.agents_config['search_agent'], # type: ignore[index]
            verbose=True,
            tools=[RETRIVERTOOL()]
        )


    @task
    def python_task(self) -> Task:
        return Task(
            config=self.tasks_config['python_task'], # type: ignore[index]
        )

    @task
    def javascript_task(self) -> Task:
        return Task(
            config=self.tasks_config['javascript_task'], # type: ignore[index]
            output_file='report.md'
        )
    
    @task
    def search_information(self) -> Task:
        return Task(
            config=self.tasks_config['search_information'], # type: ignore[index]
            output_file='report.md'
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Developer crew"""
        manager = Agent(
            config=self.agents_config['task_manager'],
            allow_delegation=True
            )
        return Crew(
            agents=self.agents, # Automatically created by the @agent decorator
            tasks=self.tasks, # Automatically created by the @task decorator
            process=Process.hierarchical,
            verbose=True,
            manager_agent=manager,
            )
