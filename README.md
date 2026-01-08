# 🚀 CRM Lead Alerts Automation with CrewAI

**Automate your CRM follow-ups with AI agents** - Never lose a lead again!

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Python 3.10+](https://img.shields.io/badge/python-3.10+-blue.svg)](https://www.python.org/downloads/)
[![CrewAI](https://img.shields.io/badge/CrewAI-1.7.2+-orange.svg)](https://www.crewai.com/)

## 📋 Overview

This system automatically monitors your Notion CRM database and sends intelligent alerts to your Telegram group when leads need follow-up attention.

**✨ Features:**

- 🤖 **AI-Powered Analysis** - Uses Groq AI (FREE!)
- 📊 **Smart Classification** - Categorizes leads by urgency
- 📱 **Telegram Notifications** - Formatted alerts to your team
- ⏰ **Automated Schedule** - Runs daily via GitHub Actions
- 🆓 **100% Free** - All services have free tiers

## 🎯 Quick Start

```bash
# 1. Clone
git clone https://github.com/fruteroclub/-Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI.git
cd -Workshop-Automate-Your-CRM-with-AI-Agents-using-CrewAI

# 2. Install
pip install -e .

# 3. Configure
cp .env.example .env
# Edit .env with your credentials

# 4. Run
python test_telegram_alert.py
```

📚 **Need credentials?** See [WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md)

## 📊 How It Works

```
Notion CRM → Lead Analyzer Agent → Notification Formatter → Telegram
```

**Alert Levels:**
- 🔴 Critical: 21+ days
- 🟡 Warning: 14-20 days
- 🟠 Attention: 7-13 days

## 🔧 Configuration

### Variables de Entorno

Create/edit `.env` with your credentials:

```env
# LLM Configuration (using Groq - FREE!)
MODEL=groq/llama-3.1-8b-instant
GROQ_API_KEY=your_groq_api_key_here

# Telegram Bot Configuration
TELEGRAM_BOT_TOKEN=your_bot_token_here
TELEGRAM_GROUP_ID=your_group_id_here

# Notion Integration Configuration
NOTION_INTEGRATION_SECRET=your_notion_secret_here
NOTION_DATABASE_ID=your_database_id_here
```

**Note**: Copy `.env.example` to `.env` and fill in your actual credentials.

### Manual Execution

```bash
# Activate virtual environment
source .venv/bin/activate

# Run alert system
python test_telegram_alert.py
```

## 🤖 System Architecture

### CrewAI Agents

1. **Lead Analyzer** (`lead_analyzer`)
   - Extracts leads from Notion CRM
   - Calculates days since last contact
   - Classifies by priority levels
   - Organizes by urgency

2. **Notification Formatter** (`notification_formatter`)
   - Formats alerts in HTML
   - Sends to Telegram group
   - Includes direct Notion links
   - Generates statistical summary

### Custom Tools

1. **NotionCRMTool** ([src/bot1/tools/notion_tool.py](src/bot1/tools/notion_tool.py))
   - Connects to Notion API
   - Extracts lead properties
   - Calculates days since last contact

2. **TelegramNotificationTool** ([src/bot1/tools/telegram_tool.py](src/bot1/tools/telegram_tool.py))
   - Sends formatted messages
   - Supports HTML parsing
   - Direct API calls

### Telegram Message Format

```
🚨 CRM Lead Alerts - Frutero
📅 January 08, 2026

📊 Summary
• 🔴 Critical: 3 leads (21+ days)
• 🟡 Warning: 2 leads (14-20 days)
• 🟠 Attention: 1 lead (7-13 days)

🔴 CRITICAL - 21+ Days Without Contact

1. Juan Pérez - Acme Corp
   📅 25 days | Last: 2024-12-10
   💬 @juanperez
   🔗 View in Notion

2. María García - Tech Solutions
   📅 23 days | Last: 2024-12-12
   🔗 View in Notion

🟡 WARNING - 14-20 Days
...
```

## ☁️ Deploy to GitHub Actions

**100% FREE** - Runs automatically without keeping your PC on!

### Why GitHub Actions?

✅ **100% FREE** - No cost
✅ **Always Active** - No need for your PC to be on
✅ **Automatic** - Runs at your scheduled time
✅ **Reliable** - GitHub infrastructure

### Setup Steps

#### 1. Push to GitHub

If you don't have the repo on GitHub yet:

```bash
cd /home/scarf/bot1

# Initialize git (if not done)
git init
git add .
git commit -m "Add CRM alerts system"

# Create repo on GitHub and push
git remote add origin https://github.com/YOUR_USERNAME/your-repo.git
git branch -M main
git push -u origin main
```

#### 2. Configure Secrets on GitHub

Secrets keep your credentials secure. Go to your repo on GitHub:

**GitHub.com → Your Repo → Settings → Secrets and variables → Actions → New repository secret**

Create these 5 secrets:

| Secret Name | Value | Description |
|-------------|-------|-------------|
| `GROQ_API_KEY` | `gsk_xxxxxxxxxxxxxxxxxxxxx` | Your Groq API key (FREE!) |
| `NOTION_INTEGRATION_SECRET` | `ntn_xxxxxxxxxxxxxxxxxxxxx` | Your Notion integration secret |
| `NOTION_DATABASE_ID` | `your_database_id_here` | 32-character database ID |
| `TELEGRAM_BOT_TOKEN` | `123456:ABC-DEF1234ghIkl...` | Your bot token from BotFather |
| `TELEGRAM_GROUP_ID` | `-1234567890` | Your group ID (with minus sign) |

#### 3. Adjust Timezone

The file `.github/workflows/crm_alerts.yml` is already created. Edit it for your timezone:

```yaml
schedule:
  # For 9 AM in different timezones:
  # Mexico (UTC-6): '0 15 * * *'
  # Colombia/Peru (UTC-5): '0 14 * * *'
  # Argentina (UTC-3): '0 12 * * *'
  # Spain (UTC+1): '0 8 * * *'
  - cron: '0 15 * * *'  # Change this for your zone
```

#### 4. Enable GitHub Actions

1. Push the workflow file:
   ```bash
   git add .github/workflows/crm_alerts.yml
   git commit -m "Add GitHub Actions workflow for daily alerts"
   git push
   ```

2. Go to: **GitHub.com → Your Repo → Actions**

3. You'll see the workflow "Daily CRM Lead Alerts"

4. **First manual test**:
   - Click on "Daily CRM Lead Alerts"
   - Click on "Run workflow" → "Run workflow"
   - Wait ~1 minute
   - Verify the message arrived on Telegram ✅

#### 5. Verify It Works

- ✅ Workflow should appear in green
- ✅ You should receive the message on Telegram
- ✅ It will run automatically every day at 9 AM

### Monitoring

**View Execution History**
**GitHub → Actions** → Click on any execution to see logs

**Error Notifications**
GitHub will send you an email if any execution fails

### Useful Commands

**Test locally before pushing**
```bash
cd /home/scarf/bot1
source .venv/bin/activate
python test_telegram_alert.py
```

**Change schedule**
Edit `.github/workflows/crm_alerts.yml` and change the cron:
```yaml
- cron: '0 15 * * *'  # Time in UTC format
```

**Time calculator:**
- Your local time - UTC offset = Time in cron
- Example Mexico (UTC-6): 9 AM + 6 = 15:00 → `'0 15 * * *'`

### Security

✅ **Secrets are encrypted** - GitHub keeps them secure
✅ **Don't appear in logs** - Shown as `***`
✅ **Not in code** - Only in GitHub configuration

### Alternative Platforms

| Solution | Cost | Complexity | Always Active |
|----------|------|------------|---------------|
| **GitHub Actions** | Free | ⭐ Easy | ✅ Yes |
| Replit | Free | ⭐⭐ Medium | ✅ Yes |
| Railway | Free/$5 | ⭐⭐ Medium | ✅ Yes |
| VPS | $5-10/mo | ⭐⭐⭐ High | ✅ Yes |
| Local Cron | Free | ⭐ Easy | ❌ Only if PC on |

**Recommendation**: Use GitHub Actions - simplest, free, and reliable.

## ⚙️ Customization

### Change Alert Criteria

Edit `test_telegram_alert.py`:

```python
# Default thresholds
critical = [l for l in leads if l['days_since_contact'] >= 21]
warning = [l for l in leads if 14 <= l['days_since_contact'] <= 20]
attention = [l for l in leads if 7 <= l['days_since_contact'] <= 13]

# Customize to your needs
critical = [l for l in leads if l['days_since_contact'] >= 30]
warning = [l for l in leads if 21 <= l['days_since_contact'] <= 29]
```

### Change Notion Properties

Edit [src/bot1/tools/notion_tool.py](src/bot1/tools/notion_tool.py) to map different property names:

```python
# Search properties with different names
name_prop = properties.get("Name") or properties.get("Cliente") or properties.get("Lead")
```

## 🐛 Troubleshooting

### "NOTION_INTEGRATION_SECRET not found"
- Verify `.env` file exists with correct variables
- Make sure you're running from project directory

### "Notion API error 401"
- Check `NOTION_INTEGRATION_SECRET`
- Ensure integration has database access

### "Can't find database"
- Verify `NOTION_DATABASE_ID` (32 characters)
- Ensure database is shared with integration

### "Telegram error: Forbidden"
- Bot must be added to the group
- Verify `TELEGRAM_GROUP_ID` (with minus sign)
- Check bot permissions in group

### "Groq API error"
- Verify `GROQ_API_KEY` is correct
- Check free tier limits (14,400 requests/day)

### "GitHub Actions failing"
- Verify all 5 secrets are set
- Check Action logs for details

### No messages received on Telegram
- Verify bot is added to group
- Confirm `TELEGRAM_GROUP_ID` is correct (negative number for groups)
- Review bot permissions in group

## 📁 Project Structure

```
bot1/
├── .env                              # Environment variables (not committed)
├── .env.example                      # Template with placeholders
├── .github/
│   └── workflows/
│       └── crm_alerts.yml           # GitHub Actions workflow
├── src/bot1/
│   ├── main.py                      # Main function run_crm_alerts()
│   ├── crew.py                      # Agent and task definitions
│   ├── config/
│   │   ├── agents.yaml              # Agent configuration
│   │   └── tasks.yaml               # Task configuration
│   └── tools/
│       ├── notion_tool.py           # Notion CRM extraction tool
│       └── telegram_tool.py         # Telegram notification tool
├── test_telegram_alert.py           # Test script
├── pyproject.toml                   # Project dependencies
├── WORKSHOP_GUIDE.md                # Complete 90-min workshop
└── README.md                        # This file
```

## 📈 Benefits

✅ **Complete automation** - No manual intervention
✅ **Never lose a lead** - Proactive alerts
✅ **Quick access** - Direct Notion links
✅ **Team visibility** - Everyone sees alerts
✅ **Clear prioritization** - Know what's urgent

## 🔐 Security

- 🔒 Credentials in `.env` (DON'T commit to repository)
- 🔒 `.env` must be in `.gitignore`
- 🔒 Regenerate tokens if exposed publicly
- 🔒 GitHub Secrets are encrypted

## 📚 Documentation

- [Workshop Guide](WORKSHOP_GUIDE.md) - Complete 90-min tutorial with API key setup
- [CrewAI Docs](https://docs.crewai.com) - Framework documentation
- [Groq Console](https://console.groq.com) - Get your free API key
- [Notion API](https://developers.notion.com) - Notion integration docs
- [Telegram Bot API](https://core.telegram.org/bots/api) - Bot documentation

## 🎯 Next Improvements

- [ ] Web dashboard for visualization
- [ ] Calendar integration for follow-ups
- [ ] Predictive conversion analysis
- [ ] Personalized messages per lead
- [ ] Automatic response system
- [ ] Weekly summary reports
- [ ] Slack/Discord integration

## 🤝 Contributing

PRs welcome! See [WORKSHOP_GUIDE.md](WORKSHOP_GUIDE.md) for setup.

## 📄 License

MIT License - See LICENSE file

---

**Made with ❤️ by Frutero Club** | **Star ⭐ if useful!**
