import regex as re
#import web_scraping as ws

def fetch_recipe(url):
    print('web_scraping.py on url', url, 'return recipe\n')
    return

def interpret_task(task):
    ##Do we include functionality for multiple recipes in a single session? Ex: I'd like to do another recipe.
    recipe_retrieval = re.compile(r'\b(recipe)\b')
    if re.search(recipe_retrieval, task):
        url = input("Please input recipe url >")
        recipe = fetch_recipe(url)
        return
    
    display_re = re.compile(r'\b(show me|how much|how many|how long|when)\b', re.IGNORECASE)
    if re.search(display_re, task):
        display_handler(task)
        print('display handler\n') 
    #TODO-------------------------------
    ##distinguishing between "What temperature" and "What is an oven"
    ## RN need to add handling for "What temperature" and similar queries still
    
    navigation_re = re.compile(r'\b(take me to|repeat|go to|go back)\b', re.IGNORECASE)
    if re.search(navigation_re, task):
        navigation_handler(task)
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
    quantity = re.compile(r'\b(how much|how many|what amount|quantity)\b', re.IGNORECASE)
    if re.search(quantity, task):
        print('find ingredient specified, find quantity, display')
        return
    time_re = re.compile(r'\b(how long|minute|second|hour|when)\b', re.IGNORECASE)
    if re.search(time_re, task):
        print('find step/process being asked about, return amount of time\n')
        return
    
        

def navigation_handler(task):
    next_step = re.compile(r'\bnext\b', re.IGNORECASE)
    if re.search(next_step, task):
        print('display next step\n')
    ##This is wrong, 'take me to the third step' vs 'take me to the 3rd step' not sure if need to handle
    ##the first
    nth_step = re.compile(r'\b(?:take me to the|go to the|take me to step|go to step) (\d+)', re.IGNORECASE)
    n = re.search(nth_step, task)
    if n:
        n = int(n.group(1))
        #go_to_step(recipe, step)
        print('go to step', n)
    repeat = re.compile(r'\b(repeat|this step)\b', re.IGNORECASE)
    repeat_flag = re.search(repeat, task)
    if repeat_flag:
        #re_print current step
        print('repeat the current step')
    return

def what_is_handler(task):
    includes_item = re.compile(r'\b(is that|do that|that done)\b.*?', re.IGNORECASE)
    if re.search(includes_item, task):
        print("find relevant task, search ingredient/tool/process\n")
        return
    print('search on youtube, can probably use the entire phrase\n')
    return




def main():
    task = ''
    while task != '0':
        print("press 0 to exit\n")
        task = input("Input task >")
        interpret_task(task)
        




if __name__ == "__main__":
    main()