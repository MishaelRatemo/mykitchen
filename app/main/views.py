from flask import render_template,request,redirect,url_for,abort
from . import main
from ..models import User,Recipe,Recipe_comment
from .forms import CommentForm
from flask_login import login_required,current_user
from .. import db

#views
@main.route('/')
def index():
  """view root page function that returns index page and its data"""
  

  return render_template('index.html')