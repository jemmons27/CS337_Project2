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
    print(ingredients)
    #all trailing,
    has_ingredient = re.compile(r'\b(how many|how much|what quantity of|what amount of)\s+(.*)\b', re.IGNORECASE)
    #has_ingredient = re.compile(r'\b(how many|how much|what quantity of|what amount of)\s+(\w+\s*)', re.IGNORECASE)
    max = 0
    ##Currently removing trailing words, can change. So "how many sweet potatoes" gives 'sweet' as one group
    ing_search = re.search(has_ingredient, task)
    max = {'diff': 0, 'ing': {}}
    for ing in ingredients:
        res = []
        words_to_keep = ing['name'].split()
        for word in words_to_keep:
            if any(word in task_word for task_word in ing_search.group(2).split()):
                res.append(word)
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
        print("Use", closest_match['quantity'], closest_match['unit'], 'of', closest_match['name'])
    else:
        ##find_process of last output related to ingredients
        print('no ingredient, refer to previous output/instruction')
    return


def time_find_process(task, ingredients):
    ##maybe makes sense to add temperature here
    has_process = re.compile(r'\b(how long|how many|when)\s+(.*)\b', re.IGNORECASE)
    process_search = re.search(has_process, task)
    print(process_search.group(2))
    if process_search:
        print("Find time for", process_search.group(2))
    else:
        print('no process found')
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