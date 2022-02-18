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


yurl = "https://spoonacular-recipe-food-nutrition-v1.p.rapidapi.com/"
headers = {
  'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
  'x-rapidapi-key': "cc6c3317f7msh684a2b86f374b2cp16d1efjsnb097fe790e7d",
  }
random_joke = "food/jokes/random"
find = "recipes/findByIngredients"
randomFind = "recipes/random"




#views
@root.route('/')
def index():
  """view root page function that returns index page and its data"""
  # recipes= requests.get('https://api.spoonacular.com/food/search?&apiKey=d7de66eae26449be8fcc6320812e027d')
  # recipe_list = json.loads(recipes.content)
  
  # all_recipes = get_recipes()
  # print(all_recipes)
  url= 'https://api.spoonacular.com/recipes/complexSearch?&apiKey=e9ff3ed11b27452bb6fbf27e9805c48b&number=8'
  data= requests.get(url).json()['results']
  print(data)
  
  
  # search_recipe = request.args.get('recipe_query')
  # if search_recipe:
  #       return redirect(url_for('.search', recipe_name=search_recipe ))
  # else:
      
  #   return render_template('index.html', recipes =data)
  joke_response = str(requests.request("GET", yurl + random_joke, headers=headers).json()['text'])
  return render_template('index.html', recipes =data, joke= joke_response  )

@root.route('/search/<recipe_name>')
def search(recipe_name):
    ''' View function to display the search results '''
    
    search_url = 'https://api.spoonacular.com/recipes/complexSearch?query=berries&number=50&apiKey=e9ff3ed11b27452bb6fbf27e9805c48b'
    s_data = requests.get(search_url).json()['results']
    print(s_data)
    
    
    # recipe_name_list = recipe_name.split()
    # recipe_name_format = "+".join(recipe_name_list)
    # searched_recipes = s_data
    title = f'search results for {recipe_name}'
    return render_template('search.html',recipes = s_data, title=title)

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

@root.route('/recipe')
def get_recipe():
  recipe_id = request.args['id']
  recipe_info_endpoint = "recipes/{0}/information".format(recipe_id)
  ingedientsWidget = "recipes/{0}/ingredientWidget".format(recipe_id)
  equipmentWidget = "recipes/{0}/equipmentWidget".format(recipe_id)

  recipe_info = requests.request("GET", yurl + recipe_info_endpoint, headers=headers).json()
    
  recipe_headers = {
    	'x-rapidapi-host': "spoonacular-recipe-food-nutrition-v1.p.rapidapi.com",
    	'x-rapidapi-key': "cc6c3317f7msh684a2b86f374b2cp16d1efjsnb097fe790e7d",
    	'accept': "text/html"
  }
  querystring = {"defaultCss":"true", "showBacklink":"false"}

  recipe_info['inregdientsWidget'] = requests.request("GET", yurl + ingedientsWidget, headers=recipe_headers, params=querystring).text
  recipe_info['equipmentWidget'] = requests.request("GET", yurl + equipmentWidget, headers=recipe_headers, params=querystring).text
  
  return render_template('recipe.html', recipe=recipe_info)