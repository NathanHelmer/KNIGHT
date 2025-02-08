from flask import Flask, render_template
from net_scan import port_scan

app = Flask(__name__)

@app.route('/run-nmap/')
def run_nmap():
    print('I got clicked')

    return 'Click'

if __name__ == '__main__':
    app.run(debug=True)