from datetime import datetime

def current_time() -> str:
    return datetime.utcnow().isoformat()
