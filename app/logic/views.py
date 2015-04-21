from flask import render_templates
from . import main


@logic.route('/')
def index():
    return render_template('index.html')
