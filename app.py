from flask import Flask, render_template, request, url_for

app = Flask(__name__)

@app.route('/madlib', methods = ['GET', 'POST'])

def fill_in_blank():
    if request.method == "POST":
        pn1=request.form["Plural noun1"]
        pn2=request.form["Plural noun2"]
        

        return render_template("madlib.html", enter="/completed")
    #return render_template(flex1="/input")

@app.route('/completed', methods = ['GET', 'POST'])
def completed():
    #return "You Submitted the Madlib!"
    
     return "Thousands of ago"

if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)