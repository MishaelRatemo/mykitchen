from flask import render_template,request,redirect,url_for,abort
from . import root
from ..models import User,Recipe,Recipe_comment
from .forms import CommentForm
from flask_login import login_required,current_user
from .. import db
from ..requests import get_recipes

import requests
import json

yurl = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "cc6c3317f7msh684a2b86f374b2cp16d1efjsnb097fe790e7d",
  }

random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"

# @root.route('/')
# def search_page():
#   # joke_response = str(requests.request("GET", yurl + random_joke, headers=headers).json()['text'])
#   return render_template('search.html', joke=joke_response)





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
  
  joke_response = str(requests.request("GET", yurl + random_joke, headers=headers).json()['text'])
    
  return render_template('index.html', recipes =data, joke= joke_response  )


@root.route('/recipes')
def get_recipes():
  if (str(request.args['ingridients']).strip() != ""):
    # If there is a list of ingridients -> list
    querystring = {"number":"5","ranking":"1","ignorePantry":"false","ingredients":request.args['ingridients']}
    response = requests.request("GET", yurl + find, headers=headers, params=querystring).json()
    return render_template('recipes.html', recipes=response)
  else:
  # Random recipes
    querystring = {"number":"5"}	
  response = requests.request("GET", yurl + randomFind, headers=headers, params=querystring).json()
  print(response)
  return render_template('recipes.html', recipes=response['recipes'])




