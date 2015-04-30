from flask.ext.wtf import Form
from wtforms import TextAreaField, SelectField, SubmitField, FileField

class SimpleInventoryUploadForm(Form):
    inventory = FileField('Inventory file')
    submit = SubmitField('Upload')

class PlayBookUploadForm(Form):
    playbook = FileField('Playbook file')
    submit = SubmitField('Upload')

