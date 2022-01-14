from flask import Flask
from threading import Thread
from os import name,system

app = Flask('')
@app.route('/')

def home():    return "I'm alive"
def run():    app.run(host='0.0.0.0',port=8080)
Thread(target=run).start()

cmd=input("[#]Insert command to run your script")
system("clear")
system(cmd)
