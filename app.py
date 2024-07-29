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
        return render_template("newmadlib.html", num1=num1, num2=num2, num3=num3, num4=num4, num5=num5, num6=num6, num7=num7, num8=num8, num9=num9, num10=num10, num11=num11, num12=num12, num13=num13, num14=num14)
    return render_template("madlib.html", enter="/completed")
    
     #return "You Submitted the Madlib!"
    
if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)