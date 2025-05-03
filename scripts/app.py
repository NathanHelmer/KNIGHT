'''
app.py
Description: runs Flask applications at the routes specified in '@app.route()'
Created: 2/7/25
Updated: 4/26/25
'''
import os
import shutil
from flask import Flask, render_template, jsonify, request, send_file
from net_scan import port_scan, get_flags
from vuln_scan import vuln_scanner
from osdetection import *

app = Flask(__name__, template_folder='../UserInterface', static_folder='../UserInterface/images')

# Precondition: none
# Postcondition: Renders the index.html page
@app.route('/')
def home():
    return render_template('index.html')

# Precondition: none
# Postocondition: Renders the nmap-scans.html page
@app.route('/nmap-scans/')
def run_nmap_page():
    return render_template('nmap-scans.html')

# Precondition: none
# Postocondition: Renders the scan-logs.html page
@app.route('/scan-logs/')
def run_nmap_logs_page():
    return render_template('scan-logs.html')

# Precondition: none
# Postocondition: Renders the vuln-scans.html page
@app.route('/vuln-scans/')
def run_vuln_scans_page():
    return render_template('vuln-scans.html')

# Precondition: none
# Postcondition: Renders the help.html page
@app.route('/help/')
def run_help_page():
    return render_template('help.html')

# Precondition: Arguments for the IP address, ports, and command line command are provided in the http request.
# These should be labeled 'ip', 'ports', and 'cmd' respectively. Requests should be of the form 
# /run-nmap-scan/?ip=<ip>&ports=<ports>&cmd=<cmd>.
# Postcondition: Runs an Nmap scan using net_scan.py and returns the results as a json string.
@app.route('/run-nmap-scan/', methods=['GET'])
def run_nmap_scan():
    ipaddr = request.args.get('ip','')
    ports = request.args.get('ports','')
    cmd_line = request.args.get('cmd','')
    
    if ports == '':
        ports = '1-1000'
    
    if ipaddr == '':
        ipaddr = '127.0.0.1'

    scan_flags = get_flags(cmd_line, ipaddr, ports)
    path = nmap_results_path() 

    port_scan(ipaddr, ports, scan_flags, path)
    return jsonify({"message": "Scan completed", "path": path})

# Precondition: Arguments for the IP address and ports are provided in the http request. These should be labeled ip
# and ports respectively. Requests should be made in the form /run-vuln-scan/?ip=<ip>&ports=<ports>.
# Postcondition: Runs a vulnerabilitiy scan using vuln_scan.py and returns the results as a json string.
@app.route('/run-vuln-scan/', methods=['GET'])
def run_vuln_scan():
    ipaddr = request.args.get('ip', '')
    ports = request.args.get('ports', '')

    if ports == '':
        ports = '1-1000'
    
    if ipaddr == '':
        ipaddr = '127.0.0.1'
    
    path = vuln_results_path()
    vuln_scanner(ipaddr, ports, path)

    return jsonify({"message": "Scan completed", "path": path})

# Precondition: The path to the target nmap file is passed as an argument in the http request.
# Postoncdition: Returns a plain text string of the file contents with a web request response. 
@app.route('/get-nmap-results/', methods=['GET'])
def get_nmap_results():
    path = request.args.get('path')
    print("Received path:", path)

    try:
        print("Opening file")
        with open(path, "r") as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No scan results available yet.", 200, {'Content-Type': 'text/plain'}

# Precondition: The path to the target vuln file is passed as an argument in the http request.
# Postcondition: Returns a plain text string of the file contents with a web request response.
@app.route('/get-vuln-results/', methods=['GET'])
def get_vuln_results():
    path = request.args.get('path')
    #path = vuln_results_path()
    try:
        with open(path, "r") as file:
            content = file.read()
        return content, 200, {'Content-Type': 'text/plain'}
    except FileNotFoundError:
        return "No scan results available yet.", 200, {'Content-Type': 'text/plain'}

# Precondition: none
# Postcondition: Returns the names for all nmap log files in the nmap folder.
@app.route('/get-all-nmap-logs/', methods=['GET'])
def get_all_nmap_logs():
    LOGS_DIR = nmap_logs_path()
    try:
        files = os.listdir(LOGS_DIR)
        logs = [{"Name": file} for file in files]
        return jsonify(logs)
    except Exception as e:
        print("error")
        return jsonify({"error": str(e)}), 500

# Precondition: none
# Postcondition: Returns teh names for all nmap log files in the nmap folder.
@app.route('/get-all-vuln-logs/', methods=['GET'])
def get_all_vuln_logs():
    LOGS_DIR = vuln_logs_path()
    try:
        files = os.listdir(LOGS_DIR)
        logs = [{"Name": file} for file in files]
        return jsonify(logs)
    except Exception as e:
        print("error")
        return jsonify({"error": str(e)}), 500

# Precondition: none
# Postcondition: Returns a json string of the path to the nmap logs.
@app.route('/get-nmap-dir/', methods=['GET'])
def get_nmap_dir():
    path = nmap_logs_path()
    return jsonify({"nmap_logs_dir": path})

# Precondition: none
# Postcondition: Returns a json string of the path to the nmap logs.
@app.route('/get-vuln-dir/', methods=['GET'])
def get_vuln_dir():
    path = vuln_logs_path()
    return jsonify({"vuln_logs_dir": path})

# Precondition: The path to the log being deleted is passed as an argument in the http request.
# Postcondition: Deletes the log specified in the http request if it exits and returns a json string stating either
# that the file was deleted or that it was not found.
@app.route('/delete-log/', methods=['POST'])
def delete_log():
    path = request.args.get('path')
    try:
        if os.path.exists(path):
            os.remove(path)
            return jsonify({"message": "File deleted"}), 200
        else:
            return jsonify({"message": "File not found"}), 404
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Precondition: The path to the log file is passed as an argument in the http request.
# Postcondition: Returns the file as an attachment if found or a json string with an error message if it is not.
@app.route('/download-log/', methods=['GET'])
def download_log():
    log_path = request.args.get('path')

    try:
        if os.path.exists(log_path):  
            print("File exists")
            return send_file(log_path, as_attachment=True)  
        else:
            print("File does not exist")
            return jsonify({"error": "File not found"}), 404  
    except Exception as e:
        return jsonify({"error": str(e)}), 500

# Precondition: none
# Postcondition: Returns a zip file of the logs folders if found or a json string with an error message if it is not.
@app.route('/download-all', methods=['GET'])
def download_all():
    log_path = results_path()
    
    try:
        shutil.make_archive(base_name='all_files', format='zip', root_dir=log_path, base_dir='.')
        if (sys.platform == 'linux'):
            return send_file("/home/admin/KNIGHT/all_files.zip", as_attachment=True)
        else:
            return send_file("\\home\\admin\\KNIGHT\\all_files.zip")
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)