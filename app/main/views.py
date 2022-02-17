from flask import render_template,request,redirect,url_for,abort
from . import root
from ..models import User,Recipe,Recipe_comment
from .forms import CommentForm
from flask_login import login_required,current_user
from .. import db
from ..requests import get_recipes

import requests
import json





#views
@root.route('/')
def index():
  """view root page function that returns index page and its data"""
  # recipes= requests.get('https://api.spoonacular.com/food/search?&apiKey=d7de66eae26449be8fcc6320812e027d')
  # recipe_list = json.loads(recipes.content)
  
  # all_recipes = get_recipes()
  # print(all_recipes)
  url= 'https://api.spoonacular.com/recipes/complexSearch?&apiKey=d7de66eae26449be8fcc6320812e027d&number=8'
  data= requests.get(url).json()['results']
  print(data)
  
  return render_template('index.html', recipes =data)


