import urllib.request,json
from .models import  Recipe


# Getting api key
api_key = None

# Getting the recipe base url
base_url = None

def configure_request(app):
    global api_key,base_url
    api_key = app.config['RECIPE_API_KEY']
    base_url = app.config['RECIPE_API_BASE_URL']


def get_recipes(category):
    '''
    Function that gets the json response to our url request
    '''
    get_recipes_url = base_url.format(api_key)
    print(get_recipes_url)

    with urllib.request.urlopen(get_recipes_url) as url:
        get_recipes_data = url.read()
        get_recipes_response = json.loads(get_recipes_data)

        recipe_Results = None

        if get_recipes_response['results']:
            recipe_Results_list = get_recipes_response['results']
            recipe_Results = process_searchResults(recipe_Results_list)


    return recipe_Results

def process_searchResults(recipe_list):
    '''
    Function  that processes the recipe searchResults and transform them to a list of Objects

    Args:
        recipe_list: A list of dictionaries that contain recipe details

    Returns :
        recipe_searchResults: A list of recipe objects
    '''

    recipe_Results = []
    for recipe_item in recipe_list:
        id = recipe_item.get('id')
        name = recipe_item.get('name')
        image = recipe_item.get('image')
        link = recipe_item.get('link')
        content = recipe_item.get('content')

    if image:
        recipe_object = Recipe(id,name,image,link,content)
        recipe_Results.append(recipe_object)

    return recipe_Results

