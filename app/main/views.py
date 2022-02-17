from re import search
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
  
  search_recipe = request.args.get('recipe_query')
  if search_recipe:
        return redirect(url_for('.search', recipe_name=search_recipe ))
  else:
      
    return render_template('index.html', recipes =data)

@root.route('/search/<recipe_name>')
def search(recipe_name):
    ''' View function to display the search results '''
    
    search_url = 'https://api.spoonacular.com/recipes/complexSearch?query=berries&number=50&apiKey=d7de66eae26449be8fcc6320812e027d'
    s_data = requests.get(search_url).json()['results']
    print(s_data)
    
    
    # recipe_name_list = recipe_name.split()
    # recipe_name_format = "+".join(recipe_name_list)
    # searched_recipes = s_data
    title = f'search results for {recipe_name}'
    return render_template('search.html',recipes = s_data, title=title)



# @root.route('/recipe/<int:id>')
# def recipe(id):

#     recipe = get_movie(id)
#     title = f'{recipe.title}'
    

#     return render_template('movie.html',title = title,movie = movie, reviews=reviews)