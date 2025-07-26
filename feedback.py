import json
from datetime import datetime
import os

LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)

def log_feedback(user_query, system_response, user_feedback, zip_code=""):
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    feedback_entry = {
        "timestamp": timestamp,
        "query": user_query,
        "response": system_response,
        "feedback": user_feedback,
        "zip_code": zip_code
    }
    filename = os.path.join(LOG_DIR, f"feedback_{timestamp}.json")
    with open(filename, "w") as f:
        json.dump(feedback_entry, f, indent=2)
    return filename