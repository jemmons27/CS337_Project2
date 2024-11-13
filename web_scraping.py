from bs4 import BeautifulSoup
import requests
import regex as re
# Get HTML from a URL
url = "https://www.allrecipes.com/shakshuka-for-one-recipe-8584907"
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
# Find all ingredient list items and store them in a dictionary
def extract_ingredients():
    url = "https://www.allrecipes.com/shakshuka-for-one-recipe-8584907"
    response = requests.get(url)
    html = response.content

# Create a BeautifulSoup object
    soup = BeautifulSoup(html, 'html.parser')
    ingredients = []
    for item in soup.find_all('li', class_="mm-recipes-structured-ingredients__list-item"):
    # Extract quantity, unit, and ingredient name
        quantity = item.find('span', {'data-ingredient-quantity': 'true'})
        unit = item.find('span', {'data-ingredient-unit': 'true'})
        ingredient_name = item.find('span', {'data-ingredient-name': 'true'})
        
    # Store information in a dictionary if ingredient name exists
        if ingredient_name:
            ingredient_info = {
                'name': re.sub(r',.*$', '', ingredient_name.text),
                'quantity': quantity.text if quantity else '',
                'unit': unit.text if unit else '',
                'raw_name': ingredient_name.text
            }
            print(ingredient_info['raw'])
            ingredients.append(ingredient_info)
    return ingredients

# Output all ingredients with quantities and units
# for ingredient in ingredients:
#     print(ingredient)

def extract_steps():
    content = soup.find(id="mm-recipes-steps__content_1-0")
    #print(steps)
    if content:
        steps = content.find_all('li')
        for step in steps:
            print(step.text)
    return steps

# Extract data
# Find all links
links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

# Find a specific element
title = soup.find('title').text





