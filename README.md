<div align="center">
  
![Knight](https://github.com/user-attachments/assets/a194506f-dce2-4383-934d-2354ddfc8fa6)

</div>

# Knowledge-Based Network Information Gathering and Hacking Tool (KNIGHT) by Siege Engine
Identifying the need to make cybersecurity practices and methods more accessible to the average student, this project seeks to create a product that bridges initial learning gaps and difficulties in the cybersecurity field. Focusing on penetration testing (pentesting) and red/blue team operations, the project has culminated in a pentesting “dropbox”, a small device in the shape of a box that can be dropped into an existing network and used to remotely perform reconnaissance and exploitation on a target system. Using an intuitive graphical user interface and requiring no prior knowledge to set up and use, the “dropbox” leverages standard cybersecurity tools and concepts such as Kali Linux, NMAP, vulnerability scanning, and Common Vulnerabilities and Exposures (CVEs) to provide a hands-on, educational introduction to pentesting methodologies. The “dropbox” serves not only as a useful cybersecurity tool but specifically aims to provide an educational walkthrough for those beginning to study network security.
<div align="center">
  
![BigDuckOutline](https://github.com/user-attachments/assets/dae19088-43b5-47f7-b971-2be5092a6cee)

</div>

## Concept
A Raspberry Pi device is plugged in via ethernet to a network. When the device is plugged in, it automatically connects to Wireguard VPN. The user can connect their own computer to the VPN and gain access to the device. The device can be accessed through a browser with HTTP or the user can connect to the device using Remote Desktop Protocol (RDP) for more direct access.

## Implementation
As part of creating a streamlined, UI-based approach to pentesting, multiple different services and tools had to be connected in a backend to work with the frontend. The frontend service was created using HTML and JavaScript. HTML pages are managed by Flask, a Python-based web framework. A Flask script runs a webserver and renders pages to the user. Tools such as NMAP and Metasploit were integrated using Python scripts. Flask also manages interactions with these scripts, passing their results to the website.​

<div align="center">

 ![FrontBackConnection](https://github.com/user-attachments/assets/50a87e03-4897-4d64-bb20-309c28e484f9)

</div>

## Technical Layout and User Instructions
See the included Technical Manual and User Manual for further instructions on how the KNIGHT works and how to use it.
