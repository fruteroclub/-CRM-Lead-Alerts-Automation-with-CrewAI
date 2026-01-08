#!/usr/bin/env python
"""Test script to send a sample CRM alert to Telegram"""

import os
from dotenv import load_dotenv
from datetime import datetime

# Load environment variables
load_dotenv()

def test_telegram_alert():
    """Send a test alert to Telegram group"""

    print("🚀 Testing Telegram Alert System...")
    print(f"📱 Group ID: {os.getenv('TELEGRAM_GROUP_ID')}")
    print(f"🤖 Bot Token: {os.getenv('TELEGRAM_BOT_TOKEN')[:20]}...")
    print()

    # First, get real data from Notion
    print("📥 Fetching real leads from Notion...")
    from src.bot1.tools.notion_tool import NotionCRMTool

    notion_tool = NotionCRMTool()
    leads = notion_tool._run()

    # Classify leads
    critical = [l for l in leads if l['days_since_contact'] >= 21]
    warning = [l for l in leads if 14 <= l['days_since_contact'] <= 20]
    attention = [l for l in leads if 7 <= l['days_since_contact'] <= 13]

    print(f"✅ Found {len(leads)} total leads")
    print(f"   🔴 Critical: {len(critical)}")
    print(f"   🟡 Warning: {len(warning)}")
    print(f"   🟠 Attention: {len(attention)}")
    print()

    # Create formatted message using HTML
    today = datetime.now().strftime("%B %d, %Y")

    message = f"""🚨 <b>CRM Lead Alerts - Frutero</b>
📅 {today}

📊 <b>Summary</b>
• 🔴 Critical: {len(critical)} leads (21+ days)
• 🟡 Warning: {len(warning)} leads (14-20 days)
• 🟠 Attention: {len(attention)} leads (7-13 days)
"""

    # Add critical leads
    if critical:
        message += f"\n🔴 <b>CRITICAL - 21+ Days Without Contact</b>\n"
        # Sort by days descending, show top 5
        critical_sorted = sorted(critical, key=lambda x: x['days_since_contact'], reverse=True)
        for i, lead in enumerate(critical_sorted[:5], 1):
            message += f"\n{i}. <b>{lead['name']}</b>"
            if lead.get('company'):
                message += f" - {lead['company']}"
            message += f"\n   📅 {lead['days_since_contact']} days | Last: {lead['last_contact']}"
            if lead.get('telegram'):
                message += f"\n   💬 {lead['telegram']}"
            message += f"\n   🔗 <a href=\"{lead['url']}\">View in Notion</a>"

        if len(critical) > 5:
            message += f"\n\n<i>... and {len(critical) - 5} more critical leads</i>"

    # Add warning leads
    if warning:
        message += f"\n\n🟡 <b>WARNING - 14-20 Days</b>\n"
        warning_sorted = sorted(warning, key=lambda x: x['days_since_contact'], reverse=True)
        for i, lead in enumerate(warning_sorted[:3], 1):
            message += f"\n{i}. <b>{lead['name']}</b>"
            if lead.get('company'):
                message += f" - {lead['company']}"
            message += f"\n   📅 {lead['days_since_contact']} days | Last: {lead['last_contact']}"
            message += f"\n   🔗 <a href=\"{lead['url']}\">View in Notion</a>"

    # Add attention leads
    if attention:
        message += f"\n\n🟠 <b>ATTENTION - 7-13 Days</b>\n"
        attention_sorted = sorted(attention, key=lambda x: x['days_since_contact'], reverse=True)
        for i, lead in enumerate(attention_sorted[:3], 1):
            message += f"\n{i}. <b>{lead['name']}</b>"
            if lead.get('company'):
                message += f" - {lead['company']}"
            message += f"\n   📅 {lead['days_since_contact']} days | Last: {lead['last_contact']}"
            message += f"\n   🔗 <a href=\"{lead['url']}\">View in Notion</a>"

    # If no alerts
    if not critical and not warning and not attention:
        message += "\n✅ <b>All Clear!</b>\nNo leads need immediate attention. Great work! 🎉"
    else:
        message += f"\n\n💡 <b>Action Required</b>\nTotal leads needing follow-up: <b>{len(critical) + len(warning) + len(attention)}</b>"

    print("📝 Message Preview:")
    print("=" * 60)
    print(message)
    print("=" * 60)
    print()

    # Send to Telegram
    print("📤 Sending to Telegram...")
    from src.bot1.tools.telegram_tool import TelegramNotificationTool

    telegram_tool = TelegramNotificationTool()
    result = telegram_tool._run(message)

    print(f"\n{result}")

    return result

if __name__ == "__main__":
    test_telegram_alert()
