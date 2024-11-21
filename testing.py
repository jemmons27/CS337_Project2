import web_scraping
import task_navigation
import spacy



def init_test():
    #url = 'https://www.allrecipes.com/shakshuka-for-one-recipe-8584907'
    url = 'https://www.allrecipes.com/recipe/26107/best-breakfast-cookie/'
    #url = 'https://www.allrecipes.com/spicy-turkey-gumbo-recipe-8744687' # url contains the allrecipes url being used
    print("God damn it... another recipe?") ##TODO remove it!!!!!!!!
    ## Initial parsing of recipe in web_scraping.py
    soup, steps, ingredients = web_scraping.fetch_recipe(url)
    task = '' # Task holds the current query, and is overwritten each time a new query is input
    last_query= {'task': task, 'output': ''} #last_query is a dict with keys 'task' and 'output', which store the query and output of the most
    #recent interaction. it is overwritten each time the bot outputs in response to a query
    curr_step = 1
    ## curr_step is an int marking current step. Always use curr_step-1 when indexing steps, as "step 1" corresponds to steps[0]
    while task != '0':
        print('----- Input 0 to exit -----\n')
        task = input('Input task > ')
        #### Navigate and resolve task, heading first to task_navigation.py at the direct_task function
        curr_step, last_query = task_navigation.direct_task(task, soup, curr_step, steps, ingredients, last_query)
        

def main():
    init_test()
    
    
    
    
if __name__ == "__main__":
    main()
    
    
###****UNIMPLEMENTED****
##Lookup where nothing specific is specified IN lookup.py 