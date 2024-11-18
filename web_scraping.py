from bs4 import BeautifulSoup
import requests
import regex as re
import spacy
from spacy.symbols import nsubj, VERB
from spacy import displacy

# Get HTML from a URL
# Create a BeautifulSoup object
def get_html_make_soup(url):
    response = requests.get(url)
    html = response.content
    soup = BeautifulSoup(html, 'html.parser')
    return soup

# Find all ingredient list items and store them in a dictionary
def extract_ingredients(soup):
    # url = "https://www.allrecipes.com/shakshuka-for-one-recipe-8584907"
    # response = requests.get(url)
    # html = response.content

# Create a BeautifulSoup object
    # soup = BeautifulSoup(html, 'html.parser')
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
            # print(ingredient_info)
            ingredients.append(ingredient_info)
    return ingredients

# Output all ingredients with quantities and units
# for ingredient in ingredients:
#     print(ingredient)

def extract_steps(soup):
    content = soup.find(id="mm-recipes-steps__content_1-0")
    #print(steps)
    if content:
        steps = content.find_all('li')
        for step in steps:
            #print(step.text)
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(step.text)
            verbs = set()
            print(step.text)
            for possible_subject in doc:
                if possible_subject.head.pos == VERB:
                    verbs.add(possible_subject.head)
                    print(possible_subject.head)
                    print([child for child in possible_subject.children])



    return steps

extract_steps()






# s = get_html_make_soup("https://www.allrecipes.com/shakshuka-for-one-recipe-8584907")
# extract_ingredients(s)
# extract_steps(s)