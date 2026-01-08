from crewai import Agent, Crew, Process, Task, LLM
from crewai.project import CrewBase, agent, crew, task
from crewai.agents.agent_builder.base_agent import BaseAgent
from typing import List
import os
from bot1.tools.notion_tool import NotionCRMTool
from bot1.tools.telegram_tool import TelegramNotificationTool


@CrewBase
class Bot1():
    """Bot1 crew for CRM Lead Alerts"""

    agents: List[BaseAgent]
    tasks: List[Task]

    def _get_llm(self):
        """Get LLM configuration using LiteLLM"""
        from litellm import completion
        # Return LLM configuration that uses LiteLLM
        return LLM(
            model="gemini/gemini-1.5-flash",
            api_key=os.getenv("GEMINI_API_KEY"),
            base_url=None,
            use_native=False  # Force use of LiteLLM instead of native provider
        )

    @agent
    def lead_analyzer(self) -> Agent:
        """Agent responsible for extracting and analyzing leads from Notion CRM"""
        return Agent(
            config=self.agents_config['lead_analyzer'],
            tools=[NotionCRMTool()],
            llm=self._get_llm(),
            verbose=True
        )

    @agent
    def notification_formatter(self) -> Agent:
        """Agent responsible for formatting and sending Telegram notifications"""
        return Agent(
            config=self.agents_config['notification_formatter'],
            tools=[TelegramNotificationTool()],
            llm=self._get_llm(),
            verbose=True
        )

    @task
    def extract_and_analyze_leads(self) -> Task:
        """Task to extract leads from Notion and classify by priority"""
        return Task(
            config=self.tasks_config['extract_and_analyze_leads'],
        )

    @task
    def format_and_send_alerts(self) -> Task:
        """Task to format and send alerts to Telegram"""
        return Task(
            config=self.tasks_config['format_and_send_alerts'],
        )

    @crew
    def crew(self) -> Crew:
        """Creates the Bot1 CRM Alert crew"""
        return Crew(
            agents=self.agents,
            tasks=self.tasks,
            process=Process.sequential,
            verbose=True,
        )
