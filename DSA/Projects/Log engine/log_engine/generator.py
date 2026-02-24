#   Generator = ingestion layer

import random
from datetime import datetime

SERVICES = ["auth", "payment", "search", "inventory"]
LEVELS = ["INFO", "WARN", "ERROR"]

def generate_log():
    if random.random() < 0.3:
        ip = "192.168.0.99"
    else:
        ip = f"192.168.0.{random.randint(1, 255)}"

    return {
        "timestamp": datetime.utcnow(),
        "level": random.choices(LEVELS, weights=[0.7, 0.2, 0.1])[0],
        "service": random.choice(SERVICES),
        "ip": ip,
        "message": "sample log message"
    }