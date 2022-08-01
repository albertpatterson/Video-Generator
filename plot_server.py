import re
from flask import Flask, request, redirect, url_for
from flask import render_template
import subprocess

from numpy import intersect1d

app = Flask(__name__)


@app.route("/")
def hello_world():
    return render_template('index.html')


@app.route("/<name>")
def show_video(name=None):
    return render_template('show_video.html', name=name)


@app.post('/create')
def create():
    slope = request.form['slope']
    intercept = request.form['intercept']

    print('slope', slope)
    print('intercept', intercept)

    out = subprocess.run(
        ['python', 'create_plot.py', slope, intercept], capture_output=True)
    name = re.match('created (.*)', out.stdout.decode('UTF-8')).group(1)

    return redirect(url_for('show_video', name=name))
