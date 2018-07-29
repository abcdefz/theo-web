import os
import sys
import click
from flask_script import Manager, Shell, Server
from flask_migrate import Migrate, MigrateCommand
from app import create_app, db


COV = None
if os.getenv('FLASK_COVERAGE'):
    import coverage
    COV = coverage.coverage(branch=True, include='/*')
    COV.start()


app = create_app(os.getenv('ENV') or 'test')
manager = Manager(app)
migrate = Migrate(app, db)


def make_shell_context():
    return dict(
        app=app,
        db=db,
    )


manager.add_command("shell", Shell(make_context=make_shell_context))
manager.add_command("db", MigrateCommand)
manager.add_command("allhost", Server(host="0.0.0.0", port=5000))


@manager.command
def test(coverage=False):
    """
    Run the unit tests.
    """
    if coverage and not os.getenv('FLASK_COVERAGE'):
        import subprocess
        os.environ['FLASK_COVERAGE'] = '1'
        sys.exit(subprocess.call(sys.argv))

    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)
    if COV:
        COV.stop()
        COV.save()
        print('Coverage Summary:')
        COV.report()
        basedir = os.path.abspath(os.path.dirname(__file__))
        covdir = os.path.join(basedir, 'tmp/coverage')
        COV.html_report(directory=covdir)
        print('HTML version: file://%s/index.html' % covdir)
        COV.erase()


if __name__ == '__main__':
    manager.run()
