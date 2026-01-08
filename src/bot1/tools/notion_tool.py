"""Notion CRM Tool for extracting leads data"""
import os
import requests
from datetime import datetime
from typing import List, Dict, Any
from crewai.tools import BaseTool
from pydantic import Field


class NotionCRMTool(BaseTool):
    """Tool for extracting leads from Notion CRM database"""

    name: str = "Notion CRM Lead Extractor"
    description: str = (
        "Extracts leads data from Notion CRM database. "
        "Returns lead information including customer name, last contact date, "
        "and days since last contact."
    )

    notion_token: str = Field(default_factory=lambda: os.getenv("NOTION_INTEGRATION_SECRET", ""))
    database_id: str = Field(default_factory=lambda: os.getenv("NOTION_DATABASE_ID", ""))

    def _run(self) -> List[Dict[str, Any]]:
        """
        Extract all leads from Notion CRM database

        Returns:
            List of leads with their information
        """
        if not self.notion_token or not self.database_id:
            raise ValueError("NOTION_INTEGRATION_SECRET and NOTION_DATABASE_ID must be set in environment")

        try:
            # Query the database using Notion API
            url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
            headers = {
                "Authorization": f"Bearer {self.notion_token}",
                "Notion-Version": "2022-06-28",
                "Content-Type": "application/json"
            }

            response = requests.post(url, headers=headers, json={})

            if response.status_code != 200:
                raise Exception(f"Notion API error {response.status_code}: {response.text}")

            data = response.json()
            leads = []
            current_date = datetime.now()

            for page in data.get("results", []):
                properties = page.get("properties", {})

                # Extract lead information
                lead_data = {
                    "id": page.get("id", ""),
                    "url": page.get("url", ""),
                }

                # Extract Customer Name (title property)
                customer_prop = properties.get("Customer", {})
                title_content = customer_prop.get("title", [])
                if title_content:
                    lead_data["name"] = title_content[0].get("plain_text", "Sin nombre")
                else:
                    lead_data["name"] = "Sin nombre"

                # Extract Last Contact Date
                last_contact_prop = properties.get("Last Contact Date", {})
                date_obj = last_contact_prop.get("date")

                if date_obj and date_obj.get("start"):
                    last_contact_str = date_obj.get("start", "")
                    try:
                        # Notion returns ISO format: "2026-01-06"
                        last_contact = datetime.fromisoformat(last_contact_str.split("T")[0])
                        lead_data["last_contact"] = last_contact.strftime("%Y-%m-%d")

                        # Calculate days since last contact
                        days_diff = (current_date - last_contact).days
                        lead_data["days_since_contact"] = days_diff
                    except Exception as e:
                        print(f"Warning: Could not parse date '{last_contact_str}': {e}")
                        lead_data["last_contact"] = last_contact_str
                        lead_data["days_since_contact"] = 999
                else:
                    lead_data["last_contact"] = "Sin fecha"
                    lead_data["days_since_contact"] = 999

                # Extract Status
                status_prop = properties.get("Status", {})
                status_select = status_prop.get("select")
                if status_select:
                    lead_data["status"] = status_select.get("name", "Lead")
                else:
                    lead_data["status"] = "Lead"

                # Extract Email (note the space: "Email ")
                email_prop = properties.get("Email ", {})
                email_content = email_prop.get("email") or ""
                lead_data["email"] = email_content

                # Extract Industry
                industry_prop = properties.get("Industry", {})
                industry_select = industry_prop.get("select")
                if industry_select:
                    lead_data["company"] = industry_select.get("name", "")
                else:
                    # Try as rich_text
                    industry_text = industry_prop.get("rich_text", [])
                    if industry_text:
                        lead_data["company"] = industry_text[0].get("plain_text", "")
                    else:
                        lead_data["company"] = ""

                # Extract Contact Person
                contact_prop = properties.get("Contact Person", {})
                contact_text = contact_prop.get("rich_text", [])
                if contact_text:
                    lead_data["contact_person"] = contact_text[0].get("plain_text", "")
                else:
                    lead_data["contact_person"] = ""

                # Extract Telegram
                telegram_prop = properties.get("Telegram", {})
                telegram_text = telegram_prop.get("rich_text", [])
                if telegram_text:
                    lead_data["telegram"] = telegram_text[0].get("plain_text", "")
                else:
                    lead_data["telegram"] = ""

                # Extract Tags
                tags_prop = properties.get("Tags", {})
                tags_multi = tags_prop.get("multi_select", [])
                if tags_multi:
                    lead_data["tags"] = ", ".join([tag.get("name", "") for tag in tags_multi])
                else:
                    lead_data["tags"] = ""

                # Extract Notes
                notes_prop = properties.get("Notes", {})
                notes_text = notes_prop.get("rich_text", [])
                if notes_text:
                    lead_data["notes"] = notes_text[0].get("plain_text", "")
                else:
                    lead_data["notes"] = ""

                # Extract Owner
                owner_prop = properties.get("Owner", {})
                owner_people = owner_prop.get("people", [])
                if owner_people:
                    lead_data["owner"] = owner_people[0].get("name", "")
                else:
                    # Try as select
                    owner_select = owner_prop.get("select")
                    if owner_select:
                        lead_data["owner"] = owner_select.get("name", "")
                    else:
                        lead_data["owner"] = ""

                leads.append(lead_data)

            return leads

        except requests.exceptions.RequestException as e:
            raise Exception(f"Network error querying Notion: {str(e)}")
        except Exception as e:
            raise Exception(f"Error querying Notion database: {str(e)}")
