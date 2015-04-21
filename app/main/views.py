from flask import render_template, redirect, url_for, abort, flash, request, current_app
from flask.ext.login import login_required, current_user
from . import main
from .forms import EditClientForm, EditClientAdminForm
from .. import db
from ..models import Permission, Role, Client
from ..decorators import admin_required


@main.route('/', methods=['GET','POST'])
@login_required
def index():
    form = EditClientForm()
    clients = Client.query.order_by(Client.name).all()
    return render_template('index.html', form=form, clients=clients)


@main.route('/edit-client/<int:id>', methods=['GET','POST'])
@login_required
@admin_required
def edit_client_admin(id):
    client = Client.query.get_or_404(id)
    form = EditProfileAdminForm(user=user)
    if form.validate_on_submit():
        client.client_role = form.client_role.data
        db.session.add(client)
        flash('Client updated successfully.')
        return redirect(url_for('.client', name=client.name))
    form.client_role.data = client.client_role
    return render_template('edit_client.html', form=form, client=client)
