# Main = orchestration

import time
import threading
from generator import generate_log
from api import app, processor
import uvicorn


def log_stream():
    count = 0
    start = time.time()

    while True:
        log = generate_log()
        processor.process(log)
        count += 1

        if count % 10000 == 0:
            elapsed = time.time() - start
            print(f"Throughput: {count/elapsed:.2f} logs/sec")

        time.sleep(0.01)  # small sleep to prevent starvation

if __name__ == "__main__":
    # Start log generation in background thread
    thread = threading.Thread(target=log_stream, daemon=True)
    thread.start()

    # Start FastAPI server
    uvicorn.run(app, host="127.0.0.1", port=8000)

