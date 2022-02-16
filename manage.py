from app import create_app, db
from flask_script import Manager, Server
from app.models import User, Recipe, Recipe_comment
from flask_migrate import Migrate, MigrateCommand

# create app_instance
app = create_app('development')

manager = Manager(app)
manager.add_command('server', Server)

migrate = Migrate(app, db)
manager.add_command('db', MigrateCommand)


@manager.command
def test():
    """Run the unit tests"""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)


@manager.shell
def make_shell_context():
    return dict(app=app, db=db, User=User, Recipe=Recipe, Recipe_comment=Recipe_comment)


if __name__ == "__main__":
    manager.run()
