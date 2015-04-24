from flask import render_template, redirect, url_for, abort, flash, request, current_app
from flask.ext.login import login_required, current_user
from . import main
from .. import db
from ..models.auth import Permission, Role
from ..decorators import admin_required


@main.route('/', methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

