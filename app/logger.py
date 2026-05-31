import logging
import json
import sys
import time

class JsonFormatter(logging.Formatter):
    def format(self, record):
        log = {
            "level": record.levelname.lower(),   # 👈 THIS is what you need
            "message": record.getMessage(),
            "logger": record.name,
        }
        return json.dumps(log)

handler = logging.StreamHandler(sys.stdout)
handler.setFormatter(JsonFormatter())

logger = logging.getLogger("app")
logger.setLevel(logging.INFO)
logger.handlers.clear()
logger.propagate = False
logger.addHandler(handler)


def log_periodically():
    while True:
        logger.info("Heartbeat log from FastAPI")
        time.sleep(30)
