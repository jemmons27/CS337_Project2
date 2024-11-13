import regex as re
from nav_handler import navigation_handler
from web_scraping import extract_steps

#import web_scraping as ws

def fetch_recipe(url):
    print('web_scraping.py on url', url, 'return recipe\n')
    return

def interpret_task(task):
    ##Do we include functionality for multiple recipes in a single session? Ex: I'd like to do another recipe.
    recipe_retrieval = re.compile(r'\b(recipe)\b')
    if re.search(recipe_retrieval, task):
        url = input("Please input recipe url > ")
        recipe = fetch_recipe(url)
        return
        '''maybe we can use this python api (https://github.com/remaudcorentin-dev/python-allrecipes)
        to literally return the recipe (or top three) and recursively call interpret_task(task)
        -- Jasmine'''
    
    display_re = re.compile(r'\b(show me|how much|how many|how long|when)\b', re.IGNORECASE)
    if re.search(display_re, task):
        display_handler(task)
        print('display handler\n') 
    #TODO-------------------------------
    ##distinguishing between "What temperature" and "What is an oven"
    ## RN need to add handling for "What temperature" and similar queries still
    
    navigation_re = re.compile(r'\b(take me to|repeat|go to|go back|what is step)\b', re.IGNORECASE)
    if re.search(navigation_re, task):
        current_step = 0 
        ###
        # #need to implement current_step as a global variable in the "main" fxn later
        ###
        step_list = extract_steps()
        navigation_handler(task, step_list, current_step) 
        print('navigation_handler\n')
        return
    
    
    ## What is a ____
    what_is_re = re.compile(r"\b(What is|Whats|What('s)|How do|How to|How is|How('s)|How can|Hows)\b.*?", re.IGNORECASE)
    if re.search(what_is_re, task):
        what_is_handler(task)
    return


def display_handler(task):
    ingredients = re.compile(r'\bingredients\b', re.IGNORECASE)
    ##TODO Dynamic handling for ingredients list, for example if a recipe calls for onions, we need to recognize "How many onions"
    if re.search(ingredients, task):
        print('show ingredients list\n')
        return
    
    quantity = re.compile(r'\b(how much(?!\s+time\b)|how many(?!\s+(minutes?|seconds?|hours?)\b)|amount|quantity)\b', re.IGNORECASE)
    if re.search(quantity, task):
        print('find ingredient specified, find quantity, display')
        ##How much [ingredient], how many [ingredient], what amount of [ingredient], what quantity of [ingredient]
        ##Possible confusions: how much time, how many minutes/seconds/hours
        ##Also the total ingredient needed for recipe vs the amount needed for a specific step
        return
    

    
    time_re = re.compile(r'\b(how long|minutes?|seconds?|hours?|when|time)\b', re.IGNORECASE)
    #How long do I [process] [ingredient], how many seconds do i [process] ingredient, etc.
    #When is [ingredient/process] done? When do I take [ingredient] out?
    
    if re.search(time_re, task):
        print('find step/process being asked about, return amount of time\n')
        return
    
        

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