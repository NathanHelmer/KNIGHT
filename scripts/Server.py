from flask import Flask, jsonify
import os

app = Flask(name)

LOGS_DIR = "logs"

def parse_logfile(filepath):
    """Extract headers from a log file."""
    headers = {}
    with open(filepath, "r", encoding="utf-8") as file:
        for  in range(4):  # Read first 4 lines (headers)
            line = file.readline().strip()
            if ": " in line:
                key, value = line.split(": ", 1)
                headers[key] = value
    return headers

@app.route("/logs", methods=["GET"])
def get_logs():
    """Return a list of logs with extracted headers."""
    logs = []
    for filename in os.listdir(LOGS_DIR):
        if filename.endswith(".txt"):
            filepath = os.path.join(LOGS_DIR, filename)
            headers = parse_log_file(filepath)
            if headers:  # Only add files with valid headers
                logs.append(headers)
    return jsonify(logs)

if name == "main":
    app.run(debug=True)
