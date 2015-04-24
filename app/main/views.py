from flask import render_template, redirect, url_for, abort, flash, request, current_app
from flask.ext.login import login_required, current_user
from . import main
from .. import db
from ..auth.models import Permission, Role
from .models import SimpleInventory
from ..decorators import admin_required


@main.route('/', methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')

@main.route('/inventory', methods=['GET', 'POST'])
@login_required
def inventories():
	inventories = SimpleInventory.query.all()
	return render_template('inventory.html', inventories=inventories)
	
