from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template("home.html")

@app.route('/inventory')
def inventory():
    return render_template("/inventory.html")

@app.route('/Autoparts')
def Autoparts():
    return render_template("/Autoparts.html")

@app.route('/contact')
def contact():
    return render_template('/Contact.html')



if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
