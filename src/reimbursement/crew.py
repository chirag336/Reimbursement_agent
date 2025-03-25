# src/latest_ai_development/crew.py
from crewai import Agent, Crew, Process, Task
from crewai.project import CrewBase, agent, crew, task
from crewai_tools import SerperDevTool
from reimbursement.services import (
    ReimService,
)
@CrewBase
class LatestAiDevelopmentCrew():
  """LatestAiDevelopment crew"""

  @agent
  def ReimAgent(self) -> Agent:
    return Agent(
      config=self.agents_config['ReimAgent'],
      verbose=True,
      tools=[SerperDevTool()]
    )

  @task
  def extract_data(self) -> Task:
    return Task(
      config=self.tasks_config['extract_data'],
    )


  @crew
  def crew(self) -> Crew:
    """Creates the LatestAiDevelopment crew"""
    return Crew(
      agents=self.agents, 
      tasks=self.tasks, 
      process=Process.sequential,
      verbose=True,
    )