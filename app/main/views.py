from flask import render_template,request,redirect,url_for,abort
from . import root
from ..models import User,Recipe,Recipe_comment
from .forms import CommentForm
from flask_login import login_required,current_user
from .. import db
from ..requests import get_recipes



#views
@root.route('/')
def index():
  """view root page function that returns index page and its data"""
  
  all_recipes = get_recipes()
  print(all_recipes)
  return render_template('index.html', recipes = all_recipes)