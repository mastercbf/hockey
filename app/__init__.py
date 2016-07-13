from flask import Flask #render_template,request,redirect,url_for
from hockey.app.hockey import *
app = Flask(__name__)

@app.route("/")
def hello():
    return 'Hi'
    #return most(teamstats(),"G")

@app.route("/mostgoals")
def mostgoals():

    return most(teamstats(),"G")

@app.route("/leastgoals")
def leastgoals():

    return least(teamstats(),"G")

if __name__ == "__main__":
    #app.debug=True
    app.run()
