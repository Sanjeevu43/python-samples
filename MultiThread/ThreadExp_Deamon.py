import threading
import time

def daemon_task():
    while True:
        print("Daemon thread running...")
        time.sleep(1)

def non_daemon_task():
    print("Non-daemon thread running...")
    time.sleep(3)

# Create a daemon thread
daemon_thread = threading.Thread(target=daemon_task, daemon=True)
daemon_thread.start()

# Create a non-daemon thread
non_daemon_thread = threading.Thread(target=non_daemon_task)
non_daemon_thread.start()

print("Main thread doing other things...")
time.sleep(2)  # Allows the non-daemon thread to start and run for a while.

# The program will exit after the non-daemon thread finishes,
# even though the daemon thread is still running.
print("Main thread exiting.")