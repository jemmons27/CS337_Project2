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
        final_steps = []
        step_data=[]
        for step in steps:
            #print(step.text)
            #print(step.text)
            split = step.text.split(".")
            for i in split:
                txt = i.lstrip('\n ')
                if txt != '':
                    final_steps.append(txt)
        ind= 0
        for i in final_steps:
            nlp = spacy.load("en_core_web_sm")
            doc = nlp(i)
            cooking_actions = []
            tools = set()
            times = []

            for token in doc:
                #print(token.text, token.pos_, token.dep_, token.morph)
                
                #print(token.dep)
                if token.pos_ == "VERB":
                    cooking_actions.append(token.text)
    
                if token.dep_ in {"dobj", "pobj"}:
                    tools.add(token.text)

                if token.dep_ == "nummod" and token.head.text in {"seconds", "minutes", "hours"}:
                    time_phrase = f"{token.text} {token.head.text}"
                    if doc[token.i-1].text == "to":
                        time_phrase = f"{doc[token.i-2].text} to {time_phrase}"
                    times.append(time_phrase)
            step_info = {'index': ind, 'step': i, 'actions': cooking_actions,'tools':tools, 'times':times, 'doc': doc}
            step_data.append(step_info)
            ind += 1
    return step_data

#soup = get_html_make_soup("https://www.allrecipes.com/shakshuka-for-one-recipe-8584907")
#extract_steps(soup)


def fetch_recipe(url):
    print("Fetching recipe data from", url, "... ")
    soup = get_html_make_soup(url)
    steps = extract_steps(soup)
    ingredients = extract_ingredients(soup)
    return soup, steps, ingredients