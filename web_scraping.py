from bs4 import BeautifulSoup
import requests

# Get HTML from a URL
url = "https://www.allrecipes.com/shakshuka-for-one-recipe-8584907"
response = requests.get(url)
html = response.content

# Create a BeautifulSoup object
soup = BeautifulSoup(html, 'html.parser')
# Find all ingredient list items and store them in a dictionary
ingredients = []
for item in soup.find_all('li', class_="mm-recipes-structured-ingredients__list-item"):
    # Extract quantity, unit, and ingredient name
    quantity = item.find('span', {'data-ingredient-quantity': 'true'})
    unit = item.find('span', {'data-ingredient-unit': 'true'})
    ingredient_name = item.find('span', {'data-ingredient-name': 'true'})
    
    # Store information in a dictionary if ingredient name exists
    if ingredient_name:
        ingredient_info = {
            'name': ingredient_name.text,
            'quantity': quantity.text if quantity else None,
            'unit': unit.text if unit else None
        }
        ingredients.append(ingredient_info)

# Output all ingredients with quantities and units
# for ingredient in ingredients:
#     print(ingredient)

content = soup.find(id="mm-recipes-steps__content_1-0")
#print(steps)
if content:
    steps = content.find_all('li')
    for step in steps:
        print(step.text)

# Extract data
# Find all links
links = soup.find_all('a')
# for link in links:
#     print(link.get('href'))

# Find a specific element
title = soup.find('title').text





