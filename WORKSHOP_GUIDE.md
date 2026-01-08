# 🚀 Workshop: Automate Your CRM with AI Agents using CrewAI

**Build an intelligent CRM alert system that monitors your Notion database and sends automated notifications to Telegram**

**📦 Repository**: https://github.com/fruteroclub/-Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI.git

**⏱️ Duration**: 90 minutes  
**📚 Level**: Intermediate  
**🛠️ Stack**: Python, CrewAI, Notion API, Telegram Bot API, GitHub Actions, Groq (FREE AI)

---

## 📋 What You'll Build

An automated system that:
- ✅ Extracts leads from your Notion CRM database
- ✅ Analyzes contact frequency and categorizes by urgency
- ✅ Sends formatted alerts to your Telegram group
- ✅ Runs automatically every day via GitHub Actions (no server needed!)
- ✅ Uses Groq AI (100% FREE - no credit card required!)

**Example Alert:**
```
🚨 CRM Lead Alerts - Your Team
📅 January 07, 2026

📊 Summary
• 🔴 Critical: 15 leads (21+ days)
• 🟡 Warning: 0 leads (14-20 days)
• 🟠 Attention: 0 leads (7-13 days)

🔴 CRITICAL - 21+ Days Without Contact
1. John Doe - Tech Startup
   📅 36 days | Last: 2025-12-02
   💬 @johndoe
   🔗 View in Notion
```

---

## 🎯 Prerequisites

- Python 3.10+ to 3.13 installed
- A GitHub account
- Basic Python knowledge
- A Notion account (free)
- A Telegram account
- Git installed

---

## 🚀 TWO WAYS TO START

Choose your preferred path:

### Path A: 🎁 Use This Template (Quick Start - 10 min)
**Best for**: Learning fast, getting results quickly  
**Pros**: Everything pre-configured, just add your credentials  
**Steps**: Clone → Configure `.env` → Run

### Path B: 🔨 Build From Scratch (Full Workshop - 90 min)
**Best for**: Understanding every component, customization  
**Pros**: Learn CrewAI fundamentals, full control  
**Steps**: `crewai create crew` → Build tools → Configure → Run

---

## 🎁 Path A: Quick Start (Use This Template)

### Step 1: Install CrewAI CLI

```bash
# Install CrewAI with tools
pip install 'crewai[tools]'

# Verify installation
crewai --version
```

### Step 2: Clone the Template

```bash
# Clone this repository
git clone https://github.com/fruteroclub/-Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI.git

# Navigate to directory
cd -Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI
```

### Step 3: Install Project Dependencies

```bash
# CrewAI uses UV for dependency management
# Lock and install dependencies
crewai install

# Or using pip (alternative)
pip install -e .
```

### Step 4: Configure Your Credentials

```bash
# Copy the example environment file
cp .env.example .env

# Edit .env with your credentials
nano .env  # or code .env, vi .env, etc.
```

Fill in these 5 credentials (see sections below for how to get each):

```env
# LLM Configuration (using Groq - FREE!)
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=gsk_your_actual_key_here

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=123456:ABC_your_actual_token
TELEGRAM_GROUP_ID=-1234567890

# Notion Integration Configuration
NOTION_INTEGRATION_SECRET=ntn_your_actual_secret
NOTION_DATABASE_ID=your_32_char_database_id
```

**📚 Jump to the credential sections below to get each key:**
- [Part 1: Notion Setup](#part-1-setup-your-notion-crm-database-10-min)
- [Part 2: Notion API Keys](#part-2-get-your-notion-api-credentials-10-min)
- [Part 3: Telegram Bot](#part-3-create-your-telegram-bot-15-min)
- [Part 4: Groq API Key](#part-4-get-groq-api-key-5-min---100-free)

### Step 5: Test the System

```bash
# Run the test script
python test_telegram_alert.py
```

✅ **Expected Output:**
```
🚀 Testing CRM Alert System...
📥 Fetching leads from Notion...
✅ Found X total leads
📤 Sending to Telegram...
✅ Message sent successfully!
```

**Check your Telegram group** - you should see the alert! 🎉

### Step 6: Deploy to GitHub Actions (Optional)

Follow [Part 10](#part-10-deploy-to-github-actions-10-min) for automatic daily alerts.

---

## 🔨 Path B: Build From Scratch

### Step 1: Install CrewAI

```bash
# Install CrewAI with tools
pip install 'crewai[tools]'
```

### Step 2: Create New Crew Project

```bash
# Create a new crew project
crewai create crew crm-alerts-bot

# Navigate to the project
cd crm_alerts_bot
```

**During setup, you'll be prompted to:**
1. Choose your LLM provider: Select "Groq" (or "Other" if not listed)
2. Choose model: `llama-3.1-8b-instant`

### Step 3: Project Structure

CrewAI creates this structure:

```
crm_alerts_bot/
├── .env                    # Your credentials
├── .gitignore             # Already configured
├── pyproject.toml         # Dependencies
├── README.md              # Auto-generated
└── src/
    └── crm_alerts_bot/
        ├── __init__.py
        ├── main.py
        ├── crew.py
        ├── config/
        │   ├── agents.yaml
        │   └── tasks.yaml
        └── tools/
            └── custom_tool.py
```

### Step 4: Install Additional Dependencies

```bash
# Add required packages
crewai install

# Add our custom dependencies
uv add requests python-dotenv

# Or using pip
pip install requests python-dotenv
```

### Step 5: Build the Tools

Now you need to create the custom tools. Follow the workshop sections:
- [Part 6: Build the Tools](#part-6-build-the-tools-20-min)
- [Part 7: Configure Agents](#part-7-understanding-the-ai-agents-10-min)

---

## 📖 Full Workshop Guide

### Part 1: Setup Your Notion CRM Database (10 min)

#### Step 1.1: Create a Notion Database

1. **Go to Notion** → Create a new page
2. **Add a Database** (Full page or inline)
3. **Name it**: "CRM Leads"

#### Step 1.2: Add Required Properties

| Property Name | Type | Required | Description |
|---------------|------|----------|-------------|
| `Customer` | Title | ✅ Yes | Lead/Customer name |
| `Last Contact Date` | Date | ✅ Yes | When you last contacted them |
| `Status` | Select | ✅ Yes | Lead, Active, Closed, etc. |
| `Industry` | Select | No | Their industry/category |
| `Contact Person` | Text | No | Point of contact name |
| `Telegram` | Text | No | Their Telegram handle |
| `Email` | Email | No | Email address |
| `Tags` | Multi-select | No | Categorization tags |

#### Step 1.3: Add Sample Data

Add 3-5 leads with different `Last Contact Date` values:
- Some from 30+ days ago (will trigger critical alerts)
- Some from 15 days ago (will trigger warnings)
- Some from today (recent contacts)

---

### Part 2: Get Your Notion API Credentials (10 min)

#### Step 2.1: Create a Notion Integration

1. **Go to**: https://www.notion.so/my-integrations
2. **Click**: "+ New integration"
3. **Fill in**:
   - Name: `CRM Alert Bot`
   - Associated workspace: Select your workspace
   - Type: Internal integration
4. **Click**: "Submit"
5. **Copy the "Internal Integration Secret"**
   - Format: `secret_xxxxx...` or `ntn_xxxxx...`
   - ⚠️ **SAVE AS**: `NOTION_INTEGRATION_SECRET`

#### Step 2.2: Share Database with Integration

1. **Open your CRM database** in Notion
2. **Click**: "•••" menu (top right)
3. **Click**: "Add connections"
4. **Search and select**: "CRM Alert Bot"
5. ✅ **Confirm** - Integration now has access

#### Step 2.3: Get Your Database ID

**From URL:**
1. Open database as full page
2. URL looks like: `https://www.notion.so/xxxxx?v=yyyyy`
3. Database ID = part between `.so/` and `?v=`
   - Example: `a1b2c3d4e5f678901234567890abcdef` (32 chars)
   - ⚠️ **SAVE AS**: `NOTION_DATABASE_ID`

---

### Part 3: Create Your Telegram Bot (15 min)

#### Step 3.1: Create Bot with BotFather

1. **Open Telegram** → Search: `@BotFather`
2. **Send**: `/start`
3. **Send**: `/newbot`
4. **Enter bot name**: `CRM Alert Bot`
5. **Enter username**: `your_crm_alert_bot` (must end in 'bot')
6. **Copy the token**:
   - Format: `1234567890:ABCdefGHIjklMNOpqrsTUVwxyz`
   - ⚠️ **SAVE AS**: `TELEGRAM_BOT_TOKEN`

#### Step 3.2: Create a Telegram Group

1. **Create new group** in Telegram
2. **Name it**: "CRM Alerts"
3. **Add your bot**: Search `@your_crm_alert_bot`
4. **Optional**: Make bot admin
   - Settings → Administrators → Add bot

#### Step 3.3: Get Your Group ID

**Method 1: Web API** (Easiest)
```bash
# Replace YOUR_BOT_TOKEN with your actual token
curl https://api.telegram.org/botYOUR_BOT_TOKEN/getUpdates
```

1. Send a message in your group (mention the bot)
2. Run the command above
3. Look for: `"chat":{"id":-1234567890}`
4. The ID is the negative number
   - ⚠️ **SAVE AS**: `TELEGRAM_GROUP_ID`

**Method 2: Using @userinfobot**
1. Add `@userinfobot` to your group
2. It shows the group ID
3. Remove it afterwards

**Method 3: Python Script**
```python
import requests
token = "YOUR_BOT_TOKEN"
url = f"https://api.telegram.org/bot{token}/getUpdates"
print(requests.get(url).json())
# Look for "chat": {"id": -1234567890}
```

---

### Part 4: Get Groq API Key (5 min) - 100% FREE!

#### Why Groq?

✅ **100% FREE** - No credit card required!  
✅ **Fast** - Lightning-speed inference  
✅ **14,400 requests/day** - Generous free tier  
✅ **Simple** - Same API as OpenAI

#### Step 4.1: Get API Key

1. **Go to**: https://console.groq.com
2. **Sign up** with email or Google
3. **Navigate to**: API Keys
4. **Click**: "Create API Key"
5. **Name it**: "CRM Alerts"
6. **Copy the key**:
   - Format: `gsk_xxxxxxxxxxxxxxxxxxxxx`
   - ⚠️ **SAVE AS**: `GROQ_API_KEY`

#### Alternative: Use OpenAI Instead

If you prefer OpenAI (requires payment):

1. Get key from: https://platform.openai.com/api-keys
2. In your `.env`:
   ```env
   MODEL=openai/gpt-4o-mini
   OPENAI_API_KEY=sk_your_key_here
   ```

**Note**: Groq is free, OpenAI requires payment!

---

### Part 5: Configure Your .env File

Create/edit `.env` with your credentials:

```env
# LLM Configuration (Groq - FREE!)
# Recommended model for speed and free tier
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=gsk_YOUR_ACTUAL_KEY

# Alternative: OpenAI (requires payment)
# MODEL=openai/gpt-4o-mini
# OPENAI_API_KEY=sk_YOUR_ACTUAL_KEY

# Telegram Configuration
TELEGRAM_BOT_TOKEN=123456:ABC_YOUR_ACTUAL_TOKEN
TELEGRAM_GROUP_ID=-1234567890

# Notion Configuration
NOTION_INTEGRATION_SECRET=ntn_YOUR_ACTUAL_SECRET
NOTION_DATABASE_ID=your_32_character_database_id
```

**⚠️ IMPORTANT**: Never commit `.env` to Git! It's in `.gitignore`.

---

### Part 6: Build the Tools (20 min)

**If using the template**: Tools are already built! Check `src/bot1/tools/`

**If building from scratch**: Create these two tools:

#### Tool 1: Notion CRM Tool

Create `src/your_project/tools/notion_tool.py`:

```python
"""Notion CRM Tool for extracting leads data"""
import os
import requests
from datetime import datetime
from typing import List, Dict, Any
from crewai.tools import BaseTool
from pydantic import Field


class NotionCRMTool(BaseTool):
    """Extracts leads from Notion CRM database"""

    name: str = "Notion CRM Lead Extractor"
    description: str = "Extracts leads from Notion CRM with contact history"

    notion_token: str = Field(default_factory=lambda: os.getenv("NOTION_INTEGRATION_SECRET", ""))
    database_id: str = Field(default_factory=lambda: os.getenv("NOTION_DATABASE_ID", ""))

    def _run(self) -> List[Dict[str, Any]]:
        """Extract all leads from Notion"""
        if not self.notion_token or not self.database_id:
            raise ValueError("Missing Notion credentials in .env")

        url = f"https://api.notion.com/v1/databases/{self.database_id}/query"
        headers = {
            "Authorization": f"Bearer {self.notion_token}",
            "Notion-Version": "2022-06-28",
            "Content-Type": "application/json"
        }

        response = requests.post(url, headers=headers, json={})
        if response.status_code != 200:
            raise Exception(f"Notion API error: {response.text}")

        data = response.json()
        leads = []
        current_date = datetime.now()

        for page in data.get("results", []):
            props = page.get("properties", {})

            # Extract customer name
            customer = props.get("Customer", {})
            name = customer.get("title", [{}])[0].get("plain_text", "Unknown")

            # Extract last contact date
            last_contact_prop = props.get("Last Contact Date", {})
            date_obj = last_contact_prop.get("date")

            if date_obj and date_obj.get("start"):
                last_contact = datetime.fromisoformat(date_obj["start"].split("T")[0])
                days_diff = (current_date - last_contact).days
                last_contact_str = last_contact.strftime("%Y-%m-%d")
            else:
                days_diff = 999
                last_contact_str = "No date"

            # Extract other fields
            status = props.get("Status", {}).get("select", {}).get("name", "Lead")
            industry = props.get("Industry", {}).get("select", {}).get("name", "")
            
            telegram_prop = props.get("Telegram", {})
            telegram = telegram_prop.get("rich_text", [{}])[0].get("plain_text", "")

            leads.append({
                "id": page.get("id"),
                "url": page.get("url"),
                "name": name,
                "last_contact": last_contact_str,
                "days_since_contact": days_diff,
                "status": status,
                "company": industry,
                "telegram": telegram
            })

        return leads
```

#### Tool 2: Telegram Notification Tool

Create `src/your_project/tools/telegram_tool.py`:

```python
"""Telegram Tool for sending alerts"""
import os
import requests
from crewai.tools import BaseTool
from pydantic import Field


class TelegramNotificationTool(BaseTool):
    """Sends formatted notifications to Telegram group"""

    name: str = "Telegram Alert Sender"
    description: str = "Sends HTML-formatted alerts to Telegram"

    bot_token: str = Field(default_factory=lambda: os.getenv("TELEGRAM_BOT_TOKEN", ""))
    group_id: str = Field(default_factory=lambda: os.getenv("TELEGRAM_GROUP_ID", ""))

    def _run(self, message: str) -> str:
        """Send message to Telegram group"""
        if not self.bot_token or not self.group_id:
            raise ValueError("Missing Telegram credentials in .env")

        url = f"https://api.telegram.org/bot{self.bot_token}/sendMessage"
        payload = {
            "chat_id": self.group_id,
            "text": message,
            "parse_mode": "HTML",
            "disable_web_page_preview": True
        }

        response = requests.post(url, json=payload, timeout=10)

        if response.status_code == 200:
            return f"✅ Message sent to group {self.group_id}"
        else:
            error = response.json().get("description", "Unknown error")
            return f"❌ Telegram error: {error}"
```

---

### Part 7: Understanding the AI Agents (10 min)

This system uses **CrewAI** to orchestrate two AI agents:

#### Agent 1: Lead Analyzer
- **Role**: Analyzes CRM leads by urgency
- **Tool**: Notion CRM Tool
- **Output**: Classified leads (Critical/Warning/Attention)

#### Agent 2: Notification Formatter
- **Role**: Creates formatted Telegram messages
- **Tool**: Telegram Notification Tool
- **Output**: Sends HTML alert to group

#### The Workflow

```
Notion DB → Lead Analyzer Agent → Classified Data
               ↓
Notification Formatter Agent → Telegram Group
```

---

### Part 8: Test Your System (5 min)

```bash
# Run the test script
python test_telegram_alert.py
```

**Expected Output:**
```
🚀 Testing CRM Alert System...
📥 Fetching leads from Notion...
✅ Found X total leads
   🔴 Critical: X
   🟡 Warning: X
   🟠 Attention: X

📤 Sending to Telegram...
✅ Message sent successfully!
```

**Check Telegram** - You should see the alert! 🎉

---

### Part 9: Customize Your Alerts (10 min)

#### Change Alert Thresholds

Edit `test_telegram_alert.py`:

```python
# Default thresholds
critical = [l for l in leads if l['days_since_contact'] >= 21]
warning = [l for l in leads if 14 <= l['days_since_contact'] <= 20]
attention = [l for l in leads if 7 <= l['days_since_contact'] <= 13]

# Customize to your needs
critical = [l for l in leads if l['days_since_contact'] >= 30]
warning = [l for l in leads if 21 <= l['days_since_contact'] <= 29]
attention = [l for l in leads if 14 <= l['days_since_contact'] <= 20]
```

#### Customize Message Format

Edit the HTML template:

```python
message = f"""🚨 <b>Your Custom Title</b>
📅 {today}

<b>Your custom content...</b>
"""
```

---

### Part 10: Deploy to GitHub Actions (10 min)

#### Step 10.1: Workflow File

The workflow is in `.github/workflows/crm_alerts.yml`:

```yaml
name: Daily CRM Lead Alerts

on:
  schedule:
    # Runs every day at 9 AM (adjust for timezone)
    # PST (UTC-8): '0 17 * * *'
    # CST Mexico (UTC-6): '0 15 * * *'
    # EST (UTC-5): '0 14 * * *'
    - cron: '0 15 * * *'
  workflow_dispatch:  # Manual trigger

jobs:
  send-alerts:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v3
      - uses: actions/setup-python@v4
        with:
          python-version: '3.11'
      - name: Install dependencies
        run: pip install -e .
      - name: Send alerts
        env:
          GROQ_API_KEY: ${{ secrets.GROQ_API_KEY }}
          NOTION_INTEGRATION_SECRET: ${{ secrets.NOTION_INTEGRATION_SECRET }}
          NOTION_DATABASE_ID: ${{ secrets.NOTION_DATABASE_ID }}
          TELEGRAM_BOT_TOKEN: ${{ secrets.TELEGRAM_BOT_TOKEN }}
          TELEGRAM_GROUP_ID: ${{ secrets.TELEGRAM_GROUP_ID }}
        run: python test_telegram_alert.py
```

#### Step 10.2: Push to GitHub

```bash
git init
git add .
git commit -m "Initial commit: CRM alerts system"
git remote add origin https://github.com/YOUR_USERNAME/your-repo.git
git push -u origin main
```

#### Step 10.3: Add GitHub Secrets

1. Go to: **Settings** → **Secrets and variables** → **Actions**
2. Click: **New repository secret**
3. Add all 5 secrets:

| Secret Name | Value |
|-------------|-------|
| `GROQ_API_KEY` | Your Groq API key |
| `NOTION_INTEGRATION_SECRET` | Your Notion secret |
| `NOTION_DATABASE_ID` | Your database ID |
| `TELEGRAM_BOT_TOKEN` | Your bot token |
| `TELEGRAM_GROUP_ID` | Your group ID |

#### Step 10.4: Test GitHub Actions

1. Go to: **Actions** tab
2. Click: **Daily CRM Lead Alerts**
3. Click: **Run workflow**
4. Wait ~1-2 minutes
5. Check Telegram! ✅

---

## 🎓 Workshop Complete!

### What You Built:

✅ Notion CRM integration  
✅ Telegram bot notifications  
✅ AI-powered lead analysis (Groq)  
✅ Automated daily alerts (GitHub Actions)  
✅ 100% free infrastructure!

### Next Steps:

1. Customize alert thresholds
2. Add more data fields
3. Change schedule
4. Share with your team!

---

## 🔧 Troubleshooting

### "Notion API error 401"
- Verify `NOTION_INTEGRATION_SECRET`
- Ensure integration has database access

### "Can't find database"
- Check `NOTION_DATABASE_ID` (32 characters)
- Verify database is shared with integration

### "Telegram error: Forbidden"
- Bot must be in the group
- Verify `TELEGRAM_GROUP_ID` (with minus sign)

### "Groq API error"
- Check `GROQ_API_KEY` is correct
- Verify free tier limits (14,400/day)

### "GitHub Actions failing"
- Verify all 5 secrets are set
- Check Action logs for details

---

## 📚 Resources

- **Repository**: https://github.com/fruteroclub/-Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI.git
- **CrewAI Docs**: https://docs.crewai.com
- **CrewAI Quickstart**: https://docs.crewai.com/en/quickstart
- **Groq Console**: https://console.groq.com
- **Notion API**: https://developers.notion.com
- **Telegram Bot API**: https://core.telegram.org/bots/api

---

## 💡 Extension Ideas

1. Add weekly summary reports
2. Integrate with Slack/Discord
3. Implement lead scoring with AI
4. Auto-generate follow-up messages
5. Build analytics dashboard
6. Add sentiment analysis
7. Create automated reminders
8. A/B test different alert formats

---

## 🌟 Why This Stack?

- **CrewAI**: Multi-agent orchestration
- **Groq**: FREE, fast AI (14,400 req/day)
- **Notion**: Flexible CRM with great API
- **Telegram**: Instant team notifications
- **GitHub Actions**: Free automation

**Total Monthly Cost**: $0 🎉

---

**Questions?** Open an issue on GitHub!

**Workshop by**: Frutero Club  
**License**: MIT

---

## Sources

- [CrewAI Quickstart](https://docs.crewai.com/en/quickstart)
- [Building AI Agents with CrewAI Guide](https://medium.com/@sahin.samia/building-ai-agents-with-crewai-a-step-by-step-guide-172627e110c5)
- [CrewAI GitHub Repository](https://github.com/crewAIInc/crewAI)
