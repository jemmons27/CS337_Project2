import web_scraping
import task_navigation
import spacy



def init_test():
    #url = 'https://www.allrecipes.com/shakshuka-for-one-recipe-8584907'
    #url = 'https://www.allrecipes.com/recipe/26107/best-breakfast-cookie/'
    url = 'https://www.allrecipes.com/spicy-turkey-gumbo-recipe-8744687' # url contains the allrecipes url being used
    #url = 'https://www.allrecipes.com/recipe/217328/jonagolds-chicken-vindaloo/'
    #url = 'https://www.allrecipes.com/recipe/85452/homemade-black-bean-veggie-burgers/'
    ## Initial parsing of recipe in web_scraping.py
    soup, steps, ingredients = web_scraping.fetch_recipe(url)
    task = '' # Task holds the current query, and is overwritten each time a new query is input
    last_query= {'task': task, 'output': ''} #last_query is a dict with keys 'task' and 'output', which store the query and output of the most
    #recent interaction. it is overwritten each time the bot outputs in response to a query
    current_step = 1
    ## curr_step is an int marking current step. Always use curr_step-1 when indexing steps, as "step 1" corresponds to steps[0]
    
    #print('Welcome to the Recipe Bot! Press enter to start the recipe. Type "0" to exit.')
    #input()
    #print('You need the following ingredients:')
    #for ingredient_info in ingredients:
    #    print(ingredient_info['quantity'] + " " + ingredient_info['unit'] + " " + ingredient_info['name'])  

    #print('\n')
    #input('Press enter to start cooking!')
    #print('Get ready to cook!\n\n')
    last_query['output'] = steps[current_step-1]["step"]

    while current_step <= len(steps) and task != '0':
        print(f'||| Step {current_step}: {steps[current_step-1]["step"]}\n\n')
        print(f'Ask a question or ask me to move to a different step!')
        task = input('||| Type here > ')
        
        #### Navigate and resolve task, heading first to task_navigation.py at the direct_task function
        current_step, last_query = task_navigation.direct_task(task, soup, current_step, steps, ingredients, last_query)
    print("You've completed the recipe! Enjoy your meal!")
    
        

def main():
    url = input('Enter a recipe url from Allrecipes.com > ')
    soup, steps, ingredients = web_scraping.fetch_recipe(url)
    task = '' # Task holds the current query, and is overwritten each time a new query is input
    last_query= {'task': task, 'output': ''} #last_query is a dict with keys 'task' and 'output', which store the query and output of the most
    #recent interaction. it is overwritten each time the bot outputs in response to a query
    current_step = 1
    ## curr_step is an int marking current step. Always use curr_step-1 when indexing steps, as "step 1" corresponds to steps[0]
    
    print('Welcome to the Recipe Bot! Press enter to start the recipe. Type "0" to exit.')
    input()
    print('You need the following ingredients:')
    for ingredient_info in ingredients:
        print(ingredient_info['quantity'] + " " + ingredient_info['unit'] + " " + ingredient_info['name'])  

    print('\n')
    input('Press enter to start cooking!')
    print('Get ready to cook!\n\n')
    while current_step <= len(steps) and task != '0':
        print(f'||| Step {current_step}: {steps[current_step-1]["step"]}\n\n')
        print(f'Ask a question or ask me to move to a different step!')
        last_query['output'] = steps[current_step-1]['step']
        
        task = input('||| Type here > ')
        #### Navigate and resolve task, heading first to task_navigation.py at the direct_task function
        current_step, last_query = task_navigation.direct_task(task, soup, current_step, steps, ingredients, last_query)
    print("You've completed the recipe! Enjoy your meal!")
    
    
    
    
if __name__ == "__main__":
    init_test()
    
    
###****UNIMPLEMENTED****
##Lookup where nothing specific is specified IN lookup.py


###
## Brief description/testing
## Can run testing.py to test, different recipes can be used by replacing the url variable at the top of init_test()
##
## init_test calls fetch_recipe from web_scraping.py, then loops through inputs and, 
## for each one, calls direct_task in task_navigation.py
##
## task_navigation.py calls one of the following functions based on what it determines about the task:
##
## - navigation_handler from nav_handler.py
## - lookup_handler from lookup.py
## - step_info_handler from step_info.py
## 
## step_info_handler is for anything related to the 3rd goal from the assignment description. It directs to:
## find_time in time_query.py
## find_ingredient in ingredient_query.py
## find_temperature in temperature_query.py
## 
##
##
##
##
## Nearly every function takes in the same arguments:
## - task(str): the input query, 
##
## - soup: the bs4 object, not sure if this is actually used other than fetch_recipe
## 
## - current_step(int): the current step, used to index steps NOTE for step 1, current_step = 1 and step = steps[current_step-1]
##                                                                 cause it made thinking about it easier for me :O
## - steps([dict]): list of step dictionaries, which are arranged as follows:
##   {'index'(int): index, 'step'(str): step text, 'actions'(list): cooking_actions,'tools'(list):tools, 'times'(list):times, 'doc'(spacy object): doc}
##
## - ingredients: list of ingredient dictionaries, which are arranged as follows:
##   {'name'(str): cleaned ing name, 'quantity'(str): listed amount, 'unit'(str):listed unit, 'raw_name'(str): uncleaned name}
##
## - last_query(dict): information about the most recent interaction, could easily change to a more robust history if necessary
##   formatted as {'query':most recent successfully completed task, 'output'(str): the corresponding string output from the bot}
