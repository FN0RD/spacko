#!/usr/bin/env python
import os
from app import create_app, db
from app.auth.models import User, Role, Permission
from app.main.models import SimpleInventory, PlayBook
from flask.ext.script import Manager, Shell
from flask.ext.migrate import Migrate, MigrateCommand

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(app=app, db=db, User=User, Role=Role, Permission=Permission, SimpleInventory=SimpleInventory, PlayBook=PlayBook)

manager.add_command('shell', Shell(make_context=make_shell_context))
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittestTextTestRunner(verbosity=2).run(tests)


if __name__ == '__main__':
    manager.run()
