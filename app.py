#Khuram Chughtai
#Website Test with Flask

# Library Imports
from flask import Flask


app = Flask(__name__)

@app.route("/")
def printHelloWorld():
    return "Hello World!"

if __name__ == '__main__':
     app.run(debug=True)


