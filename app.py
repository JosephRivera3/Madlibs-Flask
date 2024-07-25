from flask import Flask, render_template, request, url_for
import random

app = Flask(__name__)

@app.route('/madlib', methods = ['GET', 'POST'])

def fill_in_blank():
    if request.method == "POST":
        return render_template("madlib.html", enter="/completed")
    #Pluralnoun2=pn2

    #retUrn render_template(flex1="/input")

@app.route('/completed', methods = ['GET', 'POST'])
def completed():
    if request.method == "POST":
        num1=request.form["Plural noun1"]
    #num2=request.form["Plural noun2"]

    #return "You Submitted the Madlib!"

    return f"<h1> Thousands of {request.form(num1)}ago</h1>"

if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)