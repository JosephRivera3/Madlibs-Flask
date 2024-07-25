from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/madlib', methods = ['GET', 'POST'])
#def Starter():
    #if request.method == "POST":
        #return render_template("madlib.html", enter="/completed")


@app.route('/completed', methods = ['GET', 'POST'])
def completed():
    if request.method == "POST":
         return render_template("madlib.html", enter="/completed")
    num1=request.form["Plural noun1"]
    num2=request.form["Plural noun2"]
     #return "You Submitted the Madlib!"
    return f"<h1> Thousands of {(num1)} ago, there were calendars that enabled the ancient {(num2)} to divide a year into twelve</h1>"

if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)