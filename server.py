from flask import Flask, flash, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/ninja')
def ninja():
    showAll = True
    return render_template('ninja.html', show=showAll)

@app.route('/ninja/<color>')
def show_ninjas(color):
    showAll = False
    return render_template('ninja.html', color=color, show=showAll)

app.run(debug=True)
