from flask import Flask, render_template, jsonify
from net_scan import port_scan

app = Flask(__name__)

@app.route('/run-nmap/')
def run_nmap(ipaddr='127.0.0.1', ports='1-100', scan_flags='-sN'):
    return jsonify(result = port_scan(ipaddr, ports, scan_flags))

if __name__ == '__main__':
    app.run(debug=True)