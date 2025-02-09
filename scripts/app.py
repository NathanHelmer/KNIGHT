from flask import Flask, render_template, jsonify
from net_scan import port_scan

app = Flask(__name__)

@app.route('/run-nmap/')
def run_nmap():
    return jsonify(result = port_scan('127.0.0.1', '1-5000', 'quick'))

if __name__ == '__main__':
    app.run(debug=True)