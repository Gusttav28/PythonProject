from flask import *


app = Flask(__name__)

@app.route("/")
def index():
    return "hello world"
    

if __name__ == "main":
    app.run(port=3000, debug=True)
    

