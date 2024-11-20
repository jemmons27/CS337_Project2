def find_ingredients(task, steps, current_step, ingredients, last_query, referenced_item=''):
    print("interpreted as a query about the ingredients")
    ### Logic for this statement is looking for query with both ingredient(s) and recipes
    recipe_re = re.compile(r'\b(?=.*\bingredients?\b)(?=.*\brecipe\b).*', re.IGNORECASE)
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
        #print(remaining_ing)
        for ingredient_name in remaining_ing:
            split_ing = ingredient_name.split() ## rolled oats -> [rolled, oats]
            split_step = re.findall(r'\b\w+\b', step['step'])
            duplicates = [word2 for word1 in split_ing for word2 in split_step if word2 == word1]
            if duplicates != []:
                ingredient_list.append(ingredient_name)
        
        str = "For this step, you need the following ingredients: \n{"
        for ing in ingredient_list:
            str = str + '\n' + ing
        str = str + '\n}'
        print(str)
        last_query['query'] = task
        last_query['output'] = str
    ###Ingredients for full recipe
    ###Ingredients for step
    ###Amount of a single ingredient
    
    #### Restructure ingredient webscraping to remove extra stuff
    ### Like in example sliced bread, to serve alongside
    ### or peppers and/or sweet peppers
    print('UNIMPLEMENTED')    
    
    return current_step, last_query