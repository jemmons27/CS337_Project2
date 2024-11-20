import regex as re
from nav_handler import navigation_handler
from web_scraping import extract_steps, extract_2
from web_scraping import extract_ingredients
from web_scraping import get_html_make_soup
from extract_ingredient import quantity_find_process
from extract_ingredient import time_find_process

#import web_scraping as ws

def fetch_recipe(url):
    print('web_scraping.py on url', url, 'return recipe\n')
    soup = get_html_make_soup(url)
    steps = extract_steps(soup)
    ingredients = extract_ingredients(soup)
    return soup, steps, ingredients

def interpret_task(task, soup, current_step, steps, ingredients):
    ##Do we include functionality for multiple recipes in a single session? Ex: I'd like to do another recipe.
    # recipe_retrieval = re.compile(r'\b(recipe)\b')
    # if re.search(recipe_retrieval, task):
    #     url = input("Please input recipe url > ")
    #     recipe = fetch_recipe(url)
    #     return
    #     '''maybe we can use this python api (https://github.com/remaudcorentin-dev/python-allrecipes)
    #     to literally return the recipe (or top three) and recursively call interpret_task(task)
    #     -- Jasmine'''
    ingredients_re = re.compile(r'\bingredients\b', re.IGNORECASE)
    ##TODO Dynamic handling for ingredients list, for example if a recipe calls for onions, we need to recognize "How many onions"
    if re.search(ingredients_re, task):
        ingredients_handler(task, ingredients)
        ###TODO add ingredient display from global ing variable
        return
    
    display_re = re.compile(r'\b(show me|how much|how many|how long|when)\b', re.IGNORECASE)
    if re.search(display_re, task):
        display_handler(task, soup, ingredients, current_step, steps)
        # print('display handler\n') 
    #TODO-------------------------------
    ##distinguishing between "What temperature" and "What is an oven

    #What temperature
    temperature_re = re.compile(r'\b(temperature|heat|degrees|fahrenheit|celsius)\b', re.IGNORECASE)
    if re.search(temperature_re, task):
        temperature_handler(task)
        print('temperature_handler\n')
    ## RN need to add handling for "What temperature" and similar queries still
    
    navigation_re = re.compile(r'\b(take me to|repeat|go to|go back|what is step)\b', re.IGNORECASE)
    if re.search(navigation_re, task):
        current_step = 0 ## Why set to 0? TODO
        ###
        # #need to implement current_step as a global variable in the "main" fxn later
        ###
        navigation_handler(task, steps, current_step) 
        print('navigation_handler\n')
        return
    
    
    ## What is a ____
    what_is_re = re.compile(r"\b(What is|Whats|What('s)|How do|How to|How is|How('s)|How can|Hows)\b.*?", re.IGNORECASE)
    if re.search(what_is_re, task):
        what_is_handler(task)
    return

def ingredients_handler(task, ingredients):
    output = ''
    for ing in ingredients:
        if ing['quantity'] != '':
            output = output + ing['quantity'] + ' '
        if ing['unit'] != '':
            output = output + ing['unit'] + ' '
        if ing['name'] != '':
            text = ing['name'].lstrip() if ing['name'].startswith(" ") else ing['name']
            output = output + text
        print(output)
        output = ''
    return

def display_handler(task,soup, ingredients, current_step, steps):
    
    quantity = re.compile(r'\b(how much(?!\s+time\b)|how many(?!\s+(minutes?|seconds?|hours?)\b)|amount|quantity)\b', re.IGNORECASE)
    if re.search(quantity, task):
        # print('find ingredient specified, find quantity, display')
        ingredients = extract_ingredients(soup)
        quantity_find_process(task, ingredients)
        ##How much [ingredient], how many [ingredient], what amount of [ingredient], what quantity of [ingredient]
        ##Possible confusions: how much time, how many minutes/seconds/hours
        ##Also the total ingredient needed for recipe vs the amount needed for a specific step
        return
    

    
    time_re = re.compile(r'\b(how long|minutes?|seconds?|hours?|when|time)\b', re.IGNORECASE)
    #How long do I [process] [ingredient], how many seconds do i [process] ingredient, etc.
    #When is [ingredient/process] done? When do I take [ingredient] out?
    
    if re.search(time_re, task):
        print('find step/process being asked about, return amount of time\n')
        time_find_process(task, ingredients, current_step, steps)
        return
    

#temperature handler
def temperature_handler(task,steps):
    temperature_re = re.compile(r'\b(\d+)\s*(degrees|°|F|C|Farenheit|Celsius)\b', re.IGNORECASE)
    tool = re.search(r'\b(oven|stove|burner|pot|pan|grill|microwave)\b', task, re.IGNORECASE)
    for index, step in enumerate(steps):
        if tool in step:
            temperature_match = re.search(temperature_re, task)
            temperature = temperature_match.group(1)
            unit = temperature_match.group(2)
            i = index
            if temperature_match:
                print(f'In step {i}, the recipe says the {tool} needs to be set at {temperature} {unit}.')
            else:
                level = re.search(r'\b(high|medium+(?: |-)high|medium (?: |-)low|low)\b', step, re.IGNORECASE)
                if level:
                    print(f'In step {i}, the recipe says the {tool} needs to be set to {level.group(1)}')
    

    if not temperature_match:
        print(f"The recipe doesn't say what temperature to set the {tool} to.")

# def navigation_handler(task):
'''Rather than having a function here, it's defined in a separate file, navigation_handler.py. 
    We can import it from there to use!
'''

def what_is_handler(task):
    includes_item = re.compile(r'\b(is that|do that|that done)\b.*?', re.IGNORECASE)
    if re.search(includes_item, task):
        print("find relevant task, search ingredient/tool/process\n")
        ##Look at previous chat history maybe?
        return
    print('search on youtube, can probably use the entire phrase\n')
    return




def main():
    task = ''
    while task != '0':
        print("------------press 0 to exit------------")
        task = input("Input task > ")
        interpret_task(task)
        


##Init recipe, then separate function for entering a new recipe

#Structuring the code - storing data in file vs passing it into each function

#How are we storing chat logs/history, if someone asks "What is that?" we need to know what
#"that" refers to


if __name__ == "__main__":
    main()