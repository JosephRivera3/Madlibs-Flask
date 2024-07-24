from flask import Flask, render_template

app = Flask(__name__)

@app.route('/madlib', methods = ['GET', 'POST'])

def fill_in_blank():
    return render_template("madlib.html")

if __name__ == '__main__':
        app.run(host='0.0.0.0' , port=80, debug=True)