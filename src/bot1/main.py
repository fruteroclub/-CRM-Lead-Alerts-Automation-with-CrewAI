#!/usr/bin/env python
import sys
import warnings
from datetime import datetime
from dotenv import load_dotenv

from bot1.crew import Bot1

# Load environment variables
load_dotenv()

warnings.filterwarnings("ignore", category=SyntaxWarning, module="pysbd")


def run_crm_alerts():
    """
    Run the CRM Lead Alerts system.
    Extracts leads from Notion, analyzes them, and sends alerts to Telegram.
    """
    inputs = {
        'alert_criteria': '21+ days for critical, 14-20 days for warning, 7-13 days for attention',
        'team_name': 'Frutero'
    }

    try:
        result = Bot1().crew().kickoff(inputs=inputs)
        print("\n✅ CRM Alerts sent successfully!")
        print(f"Result: {result}")
        return result
    except Exception as e:
        print(f"\n❌ Error running CRM alerts: {e}")
        raise Exception(f"An error occurred while running CRM alerts: {e}")


def run():
    """
    Run the crew with default settings (legacy function).
    For CRM alerts, use run_crm_alerts() instead.
    """
    print("ℹ️  Use 'run_crm_alerts' for the CRM Lead Alert system")
    print("Running default crew configuration...")

    inputs = {
        'alert_criteria': '21+ days for critical, 14-20 days for warning, 7-13 days for attention',
        'team_name': 'Frutero'
    }

    try:
        Bot1().crew().kickoff(inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while running the crew: {e}")


def train():
    """
    Train the crew for a given number of iterations.
    """
    inputs = {
        'alert_criteria': '21+ days for critical, 14-20 days for warning, 7-13 days for attention',
        'team_name': 'Frutero'
    }
    try:
        Bot1().crew().train(n_iterations=int(sys.argv[1]), filename=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while training the crew: {e}")


def replay():
    """
    Replay the crew execution from a specific task.
    """
    try:
        Bot1().crew().replay(task_id=sys.argv[1])
    except Exception as e:
        raise Exception(f"An error occurred while replaying the crew: {e}")


def test():
    """
    Test the crew execution and returns the results.
    """
    inputs = {
        'alert_criteria': '21+ days for critical, 14-20 days for warning, 7-13 days for attention',
        'team_name': 'Frutero'
    }

    try:
        Bot1().crew().test(n_iterations=int(sys.argv[1]), eval_llm=sys.argv[2], inputs=inputs)
    except Exception as e:
        raise Exception(f"An error occurred while testing the crew: {e}")


def run_with_trigger():
    """
    Run the crew with trigger payload.
    """
    import json

    if len(sys.argv) < 2:
        raise Exception("No trigger payload provided. Please provide JSON payload as argument.")

    try:
        trigger_payload = json.loads(sys.argv[1])
    except json.JSONDecodeError:
        raise Exception("Invalid JSON payload provided as argument")

    # Extract parameters from trigger payload or use defaults
    alert_criteria = trigger_payload.get(
        'alert_criteria',
        '21+ days for critical, 14-20 days for warning, 7-13 days for attention'
    )
    team_name = trigger_payload.get('team_name', 'Frutero')

    inputs = {
        "crewai_trigger_payload": trigger_payload,
        "alert_criteria": alert_criteria,
        "team_name": team_name
    }

    try:
        result = Bot1().crew().kickoff(inputs=inputs)
        return result
    except Exception as e:
        raise Exception(f"An error occurred while running the crew with trigger: {e}")


if __name__ == "__main__":
    run_crm_alerts()
