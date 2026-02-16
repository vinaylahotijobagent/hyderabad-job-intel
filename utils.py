from datetime import datetime, timezone
from app.config import SECONDS_BACK

def is_recent(posted_ts):
    now_ts = int(datetime.now(timezone.utc).timestamp())
    return (now_ts - posted_ts) <= SECONDS_BACK
