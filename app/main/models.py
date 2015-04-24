import os
from .. import db

class SimpleInventory(db.Model):
    """
    Represents a file-backed ansible inventory.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    filename = db.Column(db.UnicodeText, unique=True)

    def __init__(self, filename, name=None):
        self.name = name if name else  os.path.basename(filename)
        self.filename = filename

    def __repr__(self):
        return '<SimpleInventory %r>' % self.name

class PlayBook(db.Model):
    """
    Represents a file-backed ansible playbook.
    """
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), unique=True)
    filename = db.Column(db.UnicodeText, unique=True)

    def __init__(self, filename, name=None):
        self.name = name if name else  os.path.basename(filename)
        self.filename = filename

    def __repr__(self):
        return '<Playbook %r>' % self.name
    
