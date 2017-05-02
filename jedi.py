from flask import Flask
from os import environ
    
app = Flask(__name__)


@app.route("/hello/<first_name>/<second_name>")
def say_hi(first_name,second_name):
    return "your Jedi name is: {}".format(second_name[:3]+first_name[:2])
    

if __name__ == "__main__":
    app.run(host=environ['IP'],
            port=int(environ['PORT']))










