from flask import Flask, render_template, request

app = Flask(__name__)

#@app.route('/madlib', methods = ['GET', 'POST'])
#def Starter():
    #if request.method == "POST":
        #return render_template("madlib.html", enter="/completed")


@app.route('/completed', methods = ['GET', 'POST'])
def completed():
    if request.method == "POST":
        num1=request.form["Plural noun1"]
        num2=request.form["Plural noun2"]
        num3=request.form["1st number"]
        num4=request.form["plural noun3"]
        return f"<h1> Thousands of {(num1)} ago, there were calendars that enabled the ancient {(num2)} to divide a year into twelve, each month into {(num3)}, and each week into seven {(num4)}</h1>"
    return render_template("madlib.html", enter="/completed")
    
     #return "You Submitted the Madlib!"
    
if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)