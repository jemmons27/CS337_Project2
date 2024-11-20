import regex as re
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
    
    ingredients_re = re.compile(r"\b(which ingredients|how many|how much|amount|quantity|ingredients)\b", re.IGNORECASE)
    if re.search(ingredients_re, task):
        referenced_item = ''
        current_step, last_query = find_ingredients(task, steps, current_step, ingredients, last_query, referenced_item)
    
    return current_step, last_query





def find_time(task, steps, current_step, ingredients, last_query, referenced_item=''):
    if referenced_item == '':
        pass
    doc = steps[current_step - 1]['doc']
    response = []
    rest_of_phrase = False
    until_re = re.complile(r'\buntil\b', re.IGNORECASE)
    for token in doc:
   
        if rest_of_phrase == False:
            if (token.pos_ == 'NUM') | (token.dep_ == 'nummod'):
                response.append(token.text)
                rest_of_phrase = True
            elif (re.search(until_re, token.text)):
                response.append(token.text)
                rest_of_phrase = True
        else:
            response.append(token.text)
    if (response == []):
        print('No response found, please restructure your query')
        return current_step, last_query
    response = ' '.join(response)
    print(response)
    last_query['query'] = task
    last_query['output'] = response
    return current_step, last_query

def find_ingredients(task, steps, current_step, ingredients, last_query, referenced_item=''):
    print("interpreted as a query about the ingredients")
    recipe_re = re.compile(r'\brecipe\b', re.IGNORECASE)
    if re.search(recipe_re, task):
        res = ''
        for ing in ingredients:
            if ing['quantity'] != '':
                res = res + ing['quantity'] + ' '
            if ing['unit'] != '':
                res = res + ing['unit'] + ' '
            if ing['name'] != '':
                res = res + ing['name']
            res = res + '\n'
        print(res)
        last_query['query'] = task
        last_query['output'] = res
    doc = steps[current_step - 1]['doc']
    #### Restructure ingredient webscraping to remove extra stuff
    ### Like in example sliced bread, to serve alongside
    ### or peppers and/or sweet peppers
    print('UNIMPLEMENTED')    
    
    return current_step, last_query

