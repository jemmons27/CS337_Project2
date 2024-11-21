import regex as re
import spacy

"""
    sorry!!! this is a bit of a gross function
"""
def find_ingredients(task, steps, current_step, ingredients, last_query):
    print("interpreted as a query about the ingredients")
    ### Logic for this statement is looking for query with both ingredient(s) and recipes
    recipe_re = re.compile(r'\b((?=.*\bingredients?\b)(?=.*\brecipe\b).*|ingredients? list)\b', re.IGNORECASE)
    if re.search(recipe_re, task):
        res = ''
        for ing in ingredients:
            if ing['quantity'] != '':
                res = res + ing['quantity'] + ' '
            if ing['unit'] != '':
                res = res + ing['unit'] + ' '
            if ing['name'] != '':
                res = res + ing['raw_name']
            res = res + '\n'
        print(res)
        last_query['query'] = task
        last_query['output'] = res
        return current_step, last_query
    
    # Contains both ingredient(s) and step
    step_re = re.compile(r'\b(?=.*\bingredients?\b)(?=.*\bstep\b).*', re.IGNORECASE)
    doc = steps[current_step-1]['doc']
    if re.search(step_re, task):
        step = steps[current_step-1]
        ingredient_list = [ing['name'] for ing in ingredients if ing['name'] in step['step']]
        remaining_ing = [ing['name'] for ing in ingredients if ing['name'] not in step['step']]
        for ingredient_name in remaining_ing:
            split_ing = ingredient_name.split() ## rolled oats -> [rolled, oats]
            split_step = re.findall(r'\b\w+\b', step['step'])
            duplicates = [word2 for word1 in split_ing for word2 in split_step if word2 == word1]
            if duplicates != []:
                ingredient_list.append(ingredient_name)
        
        
        ##TODO:::::  ADD QUANTITIES if necessary?????
        str = "For this step, you need the following ingredients: \n{"
        for ing in ingredient_list:
            str = str + '\n' + ing
        str = str + '\n}'
        print(str)
        last_query['query'] = task
        last_query['output'] = str
        return current_step, last_query
    ###Ingredients for full recipe
    ###Ingredients for step
    ###Amount of a single ingredient  ##Steps vs total recipe??? Assuming steps for now
    
    task = task.rstrip(' ?.,')
    nlp = spacy.load('en_core_web_sm')
    doc2 = nlp(task)
    query_ingredient = ''
    ingredient_list = []
    for token in doc2:
        if token.dep_ == 'dobj': ## If nothing trailing ingredient name, i.e. "how much baking powder?" recognizes powder as root not dobj
            query_ingredient = token.text
            break
        elif token.dep_ == 'ROOT':
            query_ingredient = token.text
            break
    if query_ingredient != '': ## match the query ingredient to one or more from the true list
        ingredient_list = [ing for ing in ingredients if query_ingredient in ing['name']]
    else:
        print('No ingredient found, More logic to implement?')
        return current_step, last_query
    has_amount = False
    amount = ''
    ##Check if the step includes a specific amount
    ## this is meant to cover cases where some of the ingredient is used in another step
    for token in doc:
        if (token.dep_=='nummod') | (token.pos_ == 'NUM'):
            has_amount = True
            amount = token.text
    res = ''
    if has_amount: 
        res = res + amount + ' '
    else: ## Formatting the output
        if ingredient_list[0]['quantity'] != '':
            res = res + ingredient_list[0]['quantity'] + ' '
    if ingredient_list[0]['unit'] != '':
        res = res + ingredient_list[0]['unit'] + ' '
    res = res + ingredient_list[0]['name']
    print("Use " + res)
    last_query['query'] = task
    last_query['output'] = res
    return current_step, last_query
        
            
    
    
    ##How much milk do I need?
    ###How many cups of milk
    ## How many unit of x
    ### How much x do I use?
    
    
    #### Restructure ingredient webscraping to remove extra stuff
    ### Like in example sliced bread, to serve alongside
    ### or peppers and/or sweet peppers