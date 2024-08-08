import subprocess
import time

# List of Flask application scripts
flask_apps = [
    "/home/ganesh/Downloads/Web Challenges/Web Challenges/ssrf/main_app.py",
    "commandinjection.py",
    "/home/ganesh/Downloads/Web Challenges/Web Challenges/ssrf/internal_service.py",
    "hiddenpoint.py",
    "/Downloads/test/test/app.py"
]

# Start each Flask application in a separate process
processes = []
for app in flask_apps:
    process = subprocess.Popen(['python', app], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    processes.append(process)
    print(f"Started {app} with PID {process.pid}")

# Keep the script running to keep the processes alive
try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down Flask applications...")
    # Terminate each process
    for process in processes:
        process.terminate()
        process.wait()
    print("All Flask applications have been stopped.")

