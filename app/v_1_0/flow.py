from flask import render_template
from . import app


@app.route('/query')
def query():
    """
    return query result
    """
    return render_template('query.html')
