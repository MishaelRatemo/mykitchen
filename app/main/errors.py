from flask import render_template
from . import root

@root.app_errorhandler(404)
def errors(error):
  """Functon to render the 404 error page"""
  return render_template('errors.html'),404