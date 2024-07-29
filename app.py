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
        num5=request.form["noun1"]
        num6=request.form["noun2"]
        num7=request.form["noun3"]
        num8=request.form["partofbody1"]
        num9=request.form["plural noun4"]
        num10=request.form["plural noun5"]
        num11=request.form["plural noun6"]
        num12=request.form["part of body2"]
        num13=request.form["part of body3"]
        num14=request.form["noun4"]
        return f"<h1> Thousands of {(num1)} ago, there were calendars that enabled the ancient {(num2)} to divide a year into twelve, each month into {(num3)}, and each week into seven {(num4)}. At first, people told time by sun clock, somethimes known as the {(num5)} dial. Ultimately, they invented the great time keeping devices of today, such as the gandfather, the pocket {(num6)}, the alarm {(num7)}, and, of course, the {(num8)} watch. Children learn about clocks and time almost before they learn the ABCs. They are taught that a day consists of 24 {(num9)}, an hour has 60 {(num10)}, and a minute has 60 {(num11)}. By the time they are in kindergarden, they know if the big {(num12)} is at twelve and the little {(num13)} is at three, and it is o'clock. I wish we could continue this lesson, but we've run out of {(num14)}.</h1>"
    return render_template("madlib.html", enter="/completed")
    
     #return "You Submitted the Madlib!"
    
if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)