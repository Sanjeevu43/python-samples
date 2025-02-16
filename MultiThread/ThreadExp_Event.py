import threading
import time

event = threading.Event()

def worker():
    print("Worker thread waiting for event...")
    event.wait()  # Blocks until the event is set
    print("Worker thread received event!")
    # Do something after the event is set...

worker_thread = threading.Thread(target=worker)
worker_thread.start()

print("Main thread doing other things...")
time.sleep(2)

print("Main thread setting the event...")
event.set()  # Signal the event

worker_thread.join()  # Wait for the worker thread to finish
print("Main thread finished.")