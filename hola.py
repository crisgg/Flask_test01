##Imports
from flask import Flask
app = Flask(__name__)

##Define routes
@app.route("/")
def hello():
    return "Hola mundo!"

@app.route("/a")
def a():
    return "Entre a"

@app.route("/b")
def b():
    return "Entre b"

@app.route("/c")
def c():
    return "Entre c"



app.run()

