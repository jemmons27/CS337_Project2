import regex as re
from time_query import find_time
from ingredient_query import find_ingredients
from temperature_query import find_temperature
from tools_query import find_tools
"""
File containing step_info_handler, which is called for any query asking for specifics on the current step (How many onions do I use)
by task_navigation.py

step_info_handler splits tasks based on if they reference a specific noun/verb or not, then finds what is being asked about and
returns that information
"""
def step_info_handler(task, steps, current_step, ingredients, last_query):
    
    #### Direct to find_time in time_query.py
    time_re  = re.compile(r"\b(how long|time|minutes?|seconds?|hours?|days?)\b", re.IGNORECASE)
    if re.search(time_re, task):
        current_step, last_query = find_time(task, steps, current_step, ingredients, last_query)
    
    
    ### Direct toward find_temperature in temperature_query.py
    temperature_re = re.compile(r'\b(temperature|heat|degrees|fahrenheit|celsius|hot|cold|F|C|set|heat|temp)\b', re.IGNORECASE)  
    if re.search(temperature_re, task):
        current_step, last_query = find_temperature(task, steps, current_step, ingredients, last_query)
    
    ### Direct toward find_ingredients in ingredient_query.py
    ingredients_re = re.compile(r"\b(which ingredients|how many|how much|amount|quantity|ingredients)\b", re.IGNORECASE)
    if re.search(ingredients_re, task):
        current_step, last_query = find_ingredients(task, steps, current_step, ingredients, last_query)
    
    tools_re = re.compile(r"\b(tools)\b", re.IGNORECASE)
    if re.search(tools_re, task):
        current_step, last_query = find_tools(task, steps, current_step, ingredients, last_query)      
    
    return current_step, last_query


