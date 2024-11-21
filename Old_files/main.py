### MAIN FILE : integrates questions.py, extract_ingredient.py, navigation_handler.py, and temperature_handler.py
import Old_files.questions as questions

##list of functions in questions.py and what they do
'''
fetch_recipe(url) - has a print message
interpret_task(task) - interprets the task and calls the appropriate handler
display_handler(task) - handles queries about ingredients and time
temperature_handler(task, steps) - handles queries about temperature (both integer/degree and level of heat)
what_is_handler(task) - has a print message (is supposed to handle queries about what something is)
'''
#list of functions in nav_handler.py and what they do
'''
navigation_handler(task, steps, current_step) - handles queries about navigation through the recipe
'''
#list of functions in web_scraping.py and what they do
'''
get_html_make_soup(url) - creates a BeautifulSoup object from html
extract_ingredients(soup) - extracts the ingredients and stores in a dictionary
extract_steps(soup) - extracts the steps (list of BeautifulSoup Tag objects)
'''

def main():
    print('Welcome to the Recipe Assistant!')
    recipe_url = input("Please input recipe url > ")
    soup, steps, ingredients, verbs = questions.fetch_recipe(recipe_url)
    print(verbs)
    current_step = 0
    print('Press enter to start the recipe.')
    input()
    print('You need the following ingredients:')
    for ingredient_info in ingredients:
        print(ingredient_info['quantity'] + " " + ingredient_info['unit'] + " " + ingredient_info['name'])
    while current_step < len(steps):
        print('Step', current_step + 1, ':', steps[current_step].text)
        task = input("What would you like to do? Ex. move to a step, ask a question... > ")
        current_step += 1
        questions.interpret_task(task, soup, current_step, steps, ingredients, verbs)
    

main()