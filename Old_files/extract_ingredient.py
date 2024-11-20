import regex as re
from difflib import SequenceMatcher
'''

    if re.search(quantity, task):
        print('find ingredient specified, find quantity, display')
        ##How much [ingredient], how many [ingredient], what amount of [ingredient], what quantity of [ingredient]
        ##Possible confusions: how much time, how many minutes/seconds/hours
        return
        
''' 
## Maybe should remove stop words from ing names?
def quantity_find_process(task, ingredients):
    #TODO specific quantity for a given step, or a given ingredient within a step
    #Logical concern - Could use the current step if no specific step mentioned, but this doesn't cover
    #the most general questions like 'How many yams do I boil' if not on a specific step and multiple steps use yams
    #Question: How to also extract any processes mentioned
    # print(ingredients)
    #all trailing,
    has_ingredient = re.compile(r'\b(how many|how much|what quantity of|what amount of)\s+(.*)\s+(do|should|is|for|does)\b', re.IGNORECASE)
    #has_ingredient = re.compile(r'\b(how many|how much|what quantity of|what amount of)\s+(\w+\s*)', re.IGNORECASE)
    max = 0  
    #Does it match the has_ingredient pattern
    ing_search = re.search(has_ingredient, task)
    print(ing_search.group(2))
    max = {'diff': 0, 'ing': {}}
    #Find closest ingredient
    for ing in ingredients:
        res = []
        diff = SequenceMatcher(None, ing['name'], ing_search.group(2)).ratio()
        split = ing['name'].split()
        
        print(ing['name'])
        print(diff)
        # Filter the second string to include only words that are in the set
        filtered_string = ' '.join(res)
        
        # Check result against ingredient name
        if filtered_string:
            diff = SequenceMatcher(None, ing['name'], filtered_string).ratio()
            if diff > max['diff']:
                max = {'diff': diff, 'ing': ing}
                
                
    closest_match = max['ing']
    if closest_match:
        print("Find quantity of found ingredient term: " + closest_match['name'])
        print("The recipe requires", closest_match['quantity'], closest_match['unit'], 'of', closest_match['name'])
    else:
        ##TODO find_quantity of last output related to ingredients
        print('no ingredient, refer to previous output/instruction')
    return


def time_find_process(task, ingredients, current_step, steps, verbs):
    
    ##has_time_and_unit = re.compile(r'\b\d+\b\s*(minute|minutes|second|seconds|hour|hours|day|days)\b', re.IGNORECASE)
    ##time_unit_search = re.search(has_time_and_unit, task)
    
    has_ingredient = re.compile(r'\b(how long|how many|when)\s+(.*)\b', re.IGNORECASE)
    has_ingredient_search = re.search(has_ingredient, task)
    print(ingredients)
    closest_match = {}
    if has_ingredient_search:
        ## This is a bit messy if processes and ingredient names are similar, i.e. boil vs olive oil
        max = {'diff': 0, 'ing': {}}
        #Find closest ingredient
        for ing in ingredients:
            res = []
            words_to_keep = ing['name'].split()
            for word in words_to_keep:
                if any(word in task_word for task_word in has_ingredient_search.group(2).split()):
                    res.append(word)
            # Filter the second string to include only words that are in the set
            filtered_string = ' '.join(res)
        
            # Check result against ingredient name
            if filtered_string:
                diff = SequenceMatcher(None, ing['name'], filtered_string).ratio()
                if diff > max['diff']:
                    max = {'diff': diff, 'ing': ing}
                
                
        closest_match = max['ing']
        print('Is this the correct ingredient?', closest_match)
    has_process = re.compile(r'\b(do i|should i|can i|done|is)\s+(.*)\b', re.IGNORECASE)
    has_process_search = re.search(has_process, task)
    processes = []
    for i in range(len(verbs)):
        curr = list(verbs[i])
        for j in range(len(curr)):
            processes.append(curr[j])
    process_guess = {}
    if has_process:
        max = {'diff': 0, 'process': ''}
        print(has_process_search.group(2))
        for process in processes:
            res = []
            print(process)
            words_to_keep = str(process).split()
            for word in words_to_keep:
                if any(word in task_word for task_word in has_process_search.group(2).split()):
                    res.append(word)
            filtered_string = ' '.join(res)
            if filtered_string:
                diff = SequenceMatcher(None, process, filtered_string).ratio()
                if diff > max['diff']:
                    max = {'diff': diff, 'process': process}
        process_guess = {'process':max['process'], 'time': 0}
        print("Is this the correct process?",process_guess)
    if (closest_match):
        if (process_guess):
        ## If we have a guess for ingredient and process, can find exact step being referred to and return that step
            print('Find step with both closest_match and process_guess, then return')
        else:
            print('Find all steps about ingredient=closest_match. If 1, return that. If more than 1, find which contains either numbers or time related words')
    elif (process_guess):
        print('Find all steps which include this process. If there is a reference to an ambiguous ingredient (that, this, it, etc), refer to previous step, otherwise do the same as above')
    else:
        print('No reasonable guesses ')
    ## No ingredients, find best guess from task/steps
    return


#'\b(how long|minutes?|seconds?|hours?|when|time)\b'
 #How long do I [process] [ingredient], how many seconds do i [process] ingredient, etc.
    #When is [ingredient/process] done? When do I take [ingredient] out?
def main():
    task = ''
    while task != '0':
        task = input('next > ')
        #time_find_process(task, [])
        #quantity_find_process(task)

if __name__ == "__main__":
    main()