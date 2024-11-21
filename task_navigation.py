import regex as re
from nav_handler import navigation_handler
from lookup import lookup_handler
from step_info import step_info_handler

def direct_task(task, soup, current_step, steps, ingredients, last_query):
    navigation_re = re.compile(r'\b(go to|repeat|take me to|go back|next)\b', re.IGNORECASE)
    ##Navigation check, Go to nav_handler.py
    if re.search(navigation_re, task):
        ###TODO ERASE PRINT STATEMENT
        ##
        print("\nThis has been interpreted as a navigation task")
        current_step, last_query = navigation_handler(task, steps, current_step, last_query)
        return current_step, last_query
    
    lookup_re = re.compile(r"\b(what is|what's|whats|define|how do i|how is|how to|show me what)\b", re.IGNORECASE)
    ## Go to lookup.py and run lookup_handler
    if re.search(lookup_re, task):
        print("\nThis has been interpreted as a lookup task")
        current_step, last_query = lookup_handler(task, steps, current_step, ingredients, last_query)
        return current_step, last_query
    
    step_info_re = re.compile(r'\b(how much|how long|temperature|when|what can|replace|how many|time|amount|quantity|ingredients|hot|heat|cold|fahrenheit|celsius|F|C|set|degrees)\b', re.IGNORECASE)
    # Quantity: How much, how many, what amount, what quantity,
    # Time: How long, how many minutes/seconds/hours, when is ___ done, when do i
    # Temperature: What temperature, how many degrees, set ___ at/to
    # Tools: What do I use to, What do I need
    # Replacement: What can I replace __ with, what can I use instead of ___, can I replace __ with __,
    
    
    ### Go to step_info.py and run step_info_handler
    if re.search(step_info_re, task):
        print("\nThis has been interpreted as a step info task")
        current_step, last_query = step_info_handler(task, steps, current_step, ingredients, last_query)
        
        return current_step, last_query
    
    
    last_query['query'] = task
    last_query['output'] = ''
    return current_step, last_query
    
    
    
