from flask.ext.wtf import Form
from wtforms import TextAreaField, SelectField, SubmitField


class EditClientForm(Form):
    client_action = SelectField('Action')
    client_notes = TextAreaField('Notes')
    submit = SubmitField('Submit')


class EditClientAdminForm(Form):
    client_role = SelectField('Ansible Role')
    submit = SubmitField('Run')
