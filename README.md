# Knowledge-Based Network Information Gathering and Hacking Tool (KNIGHT) by Siege Engine
Identifying the need to make cybersecurity practices and methods more accessible to the average student, this project seeks to create a product that bridges initial learning gaps and difficulties in the cybersecurity field. Focusing on penetration testing (pentesting) and red/blue team operations, the project has culminated in a pentesting “dropbox”, a small device in the shape of a box that can be dropped into an existing network and used to remotely perform reconnaissance and exploitation on a target system. Using an intuitive graphical user interface and requiring no prior knowledge to set up and use, the “dropbox” leverages standard cybersecurity tools and concepts such as Kali Linux, NMAP, vulnerability scanning, and Common Vulnerabilities and Exposures (CVEs) to provide a hands-on, educational introduction to pentesting methodologies. The “dropbox” serves not only as a useful cybersecurity tool but specifically aims to provide an educational walkthrough for those beginning to study network security.

![image](https://github.com/user-attachments/assets/e8756260-7a7d-40b0-bb26-8484d32c4698)

## Creating a Virtual Environment
Create the virtual environment run these commands in the home directory:

`python -m venv venv`

Activate the virtual environment:

`venv\Scripts\activate`

Install required packages:

`python -m venv env`

`source env/bin/activate`

`pip install -r requirements.txt`

If you use pip to install more packages to your virtual environment, you can make a new requirements.txt using:

`pip freeze > requirements.txt`
