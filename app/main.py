from fastapi import FastAPI
import random
import threading
from app.logger import log_periodically

app = FastAPI(title="FastAPI Logger App")


@app.on_event("startup")
def start_logger():
    thread = threading.Thread(target=log_periodically, daemon=True)
    thread.start()


@app.get("/")
def read_root():
    return {"status": "running"}


@app.get("/random")
def get_random_number():
    return {"random_number": random.random()}
