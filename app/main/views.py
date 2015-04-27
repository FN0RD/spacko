from flask import render_template, redirect, url_for, abort, flash, request, current_app
from flask.ext.login import login_required, current_user
from . import main
from .. import db
from ..auth.models import Permission, Role
from .models import SimpleInventory, PlayBook
from .forms import SimpleInventoryUploadForm, PlayBookUploadForm
from ..decorators import admin_required
import os


@main.route('/', methods=['GET','POST'])
@login_required
def index():
    return render_template('index.html')


@main.route('/inventory', methods=('GET', 'POST'))
@login_required
def inventories():
	uploadform = SimpleInventoryUploadForm()
	if uploadform.validate_on_submit():
		filename = os.path.basename(uploadform.inventory.data.filename)
		local_filename = os.path.join(current_app.config['INVENTORY_DIR'], filename)
		uploadform.inventory.data.save(local_filename)
		inventory = SimpleInventory(local_filename)
		db.session.add(inventory)
		db.session.commit()
		flash("Upload successful %r" % filename)

	inventories = SimpleInventory.query.all()
	return render_template('inventory.html', inventories=inventories, uploadform=uploadform)


@main.route('/playbooks', methods=('GET', 'POST'))
@login_required
def playbooks():
	uploadform = PlayBookUploadForm()
	if uploadform.validate_on_submit():
		filename = os.path.basename(uploadform.playbook.data.filename)
		local_filename = os.path.join(current_app.config['PLAYBOOK_DIR'], filename)
		uploadform.playbook.data.save(local_filename)
		playbook = PlayBook(local_filename)
		db.session.add(playbook)
		db.session.commit()
		flash("Upload successful %r" % filename)

	playbooks = PlayBook.query.all()
	return render_template('playbooks.html', playbooks=playbooks, uploadform=uploadform)
