from dotenv import load_dotenv
load_dotenv()

from app.database import create_db
from app.notifier import send_message
from app.config import WORKDAY_COMPANIES
from app.companies.workday import ingest_workday

def main():
    create_db()

    wd_total_checked = 0
    wd_total_inserted = 0

    for company in WORKDAY_COMPANIES:
        checked, inserted = ingest_workday(company)
        wd_total_checked += checked
        wd_total_inserted += inserted

    summary = f"""
Daily Ingestion Summary

Workday GCCs:
Checked: {wd_total_checked}
Inserted: {wd_total_inserted}
"""

    send_message(summary)

if __name__ == "__main__":
    main()
