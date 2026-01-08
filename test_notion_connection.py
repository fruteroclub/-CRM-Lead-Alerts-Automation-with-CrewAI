#!/usr/bin/env python
"""Test script to verify Notion connection and data extraction"""

import os
from dotenv import load_dotenv
from src.bot1.tools.notion_tool import NotionCRMTool

# Load environment variables
load_dotenv()

def test_notion_connection():
    """Test the Notion CRM Tool connection"""

    print("🔍 Testing Notion CRM Connection...")
    print(f"📊 Database ID: {os.getenv('NOTION_DATABASE_ID')}")
    print(f"🔑 Token configured: {'Yes' if os.getenv('NOTION_INTEGRATION_SECRET') else 'No'}")
    print()

    try:
        # Create tool instance
        tool = NotionCRMTool()

        # Extract leads
        print("📥 Extracting leads from Notion...")
        leads = tool._run()

        print(f"\n✅ Successfully extracted {len(leads)} leads!\n")

        # Show summary by days since contact
        critical = [l for l in leads if l['days_since_contact'] >= 21]
        warning = [l for l in leads if 14 <= l['days_since_contact'] <= 20]
        attention = [l for l in leads if 7 <= l['days_since_contact'] <= 13]
        recent = [l for l in leads if l['days_since_contact'] < 7]

        print("📊 SUMMARY BY PRIORITY:")
        print(f"  🔴 Critical (21+ days): {len(critical)} leads")
        print(f"  🟡 Warning (14-20 days): {len(warning)} leads")
        print(f"  🟠 Attention (7-13 days): {len(attention)} leads")
        print(f"  ✅ Recent (< 7 days): {len(recent)} leads")
        print()

        # Show first 5 leads as sample
        print("📋 SAMPLE LEADS (first 5):")
        for i, lead in enumerate(leads[:5], 1):
            print(f"\n{i}. {lead['name']}")
            print(f"   Status: {lead['status']}")
            print(f"   Last Contact: {lead['last_contact']}")
            print(f"   Days Since: {lead['days_since_contact']}")
            if lead.get('company'):
                print(f"   Industry: {lead['company']}")
            if lead.get('telegram'):
                print(f"   Telegram: {lead['telegram']}")
            if lead.get('tags'):
                print(f"   Tags: {lead['tags']}")
            print(f"   URL: {lead['url']}")

        # Show critical leads
        if critical:
            print(f"\n\n🔴 CRITICAL LEADS ({len(critical)} total):")
            for lead in critical[:3]:  # Show first 3
                print(f"  • {lead['name']} - {lead['days_since_contact']} days")

        return leads

    except Exception as e:
        print(f"\n❌ Error: {str(e)}")
        print("\n💡 Troubleshooting:")
        print("  1. Verify NOTION_INTEGRATION_SECRET is correct")
        print("  2. Verify NOTION_DATABASE_ID is correct")
        print("  3. Ensure the integration has access to the database")
        print("  4. Check that the database exists and is shared with the integration")
        return None

if __name__ == "__main__":
    test_notion_connection()
