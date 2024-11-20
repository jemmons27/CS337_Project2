import regex as re
from time_query import find_time
from ingredient_query import find_ingredients
from temperature_query import find_temperature
"""
File containing step_info_handler, which is called for any query asking for specifics on the current step (How many onions do I use)

step_info_handler splits tasks based on if they reference a specific noun/verb or not, then finds what is being asked about and
returns that information
"""
def step_info_handler(task, steps, current_step, ingredients, last_query):
    no_specific_item = re.compile(r"\b(do that|do this|is that|is this|what's that|whats that)\b", re.IGNORECASE)
    if re.search(no_specific_item, 'a'):
        print("Step_info_handler found no specific information referenced, parsing last query")
        referenced_item = '' ### Call a separate function here, which finds the referenced item, then continues
                             ### with the normal step_info logic
        print("UNIMPLEMENTED")
        return current_step, last_query
    
    
    time_re  = re.compile(r"\b(how long|time|minutes?|seconds?|hours?|days?)\b", re.IGNORECASE)
    if re.search(time_re, task):
        referenced_item = ''
        current_step, last_query = find_time(task, steps, current_step, ingredients, last_query, referenced_item)
        
    temperature_re = re.compile(r'\b(temperature|heat|degrees|fahrenheit|celsius|hot|cold|F|C)\b', re.IGNORECASE)  
    if re.search(temperature_re, task):
        referenced_item = ''
        current_step, last_query = find_temperature(task, steps, current_step, ingredients, last_query, referenced_item)
    
    ingredients_re = re.compile(r"\b(which ingredients|how many|how much|amount|quantity|ingredients)\b", re.IGNORECASE)
    if re.search(ingredients_re, task):
        referenced_item = ''
        current_step, last_query = find_ingredients(task, steps, current_step, ingredients, last_query, referenced_item)
          
    
    return current_step, last_query


