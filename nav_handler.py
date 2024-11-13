import regex as re

def navigation_handler(task, steps, current_step):
    #Assume steps is a list of strings, each string is a step in the recipe
    #possible special cases: start from the beginning/start over, read a step sentence by sentence, handle 1st vs first
    ordinal_dict = {"1st": "first", "2nd": "second", "3rd": "third", "4th": "fourth", "5th": "fifth", "6th": "sixth", "7th": "seventh", "8th": "eighth", "9th": "ninth", "10th": "tenth", "11th": "eleventh", "12th": "twelfth", "13th": "thirteenth", "14th": "fourteenth", "15th": "fifteenth", "16th": "sixteenth", "17th": "seventeenth", "18th": "eighteenth", "19th": "nineteenth", "20th": "twentieth"}
    # Create a pattern that includes both numeric and word-based ordinals
    ordinal_words = '|'.join(ordinal_dict.values())
    ordinal_numbers = '|'.join(ordinal_dict.keys())
    pattern = rf'\b(?:take me to the|go to the|take me to step|go to step|what is step) (\d+|{ordinal_words}|{ordinal_numbers})\b'
   
    next_step = re.compile(r'\bnext\b', re.IGNORECASE)
    prev_step = re.compile(r'\b(previous|last)\b', re.IGNORECASE)
    nth_step = re.compile(pattern, re.IGNORECASE)
    repeat = re.compile(r'\b(repeat|this step)\b', re.IGNORECASE)

    #if repeat is mentioned, print the current step
    repeat_flag = re.search(repeat, task)
    if repeat_flag:
        #re_print current step
        print('repeat the current step')
    #if next step is mentioned, print the next step
    if re.search(next_step, task):
        next = current_step + 1
        print('The next step, ' + str(next) + ', is: ' + steps[next])
    #if previous step is mentioned, print the previous step
    elif re.search(prev_step, task):
        prev = current_step - 1
        print('The previous step, ' + str(prev) + ', is: ' + steps[prev])
    
    #if a specific step is mentioned, print that step
    n = re.search(nth_step, task)
    if n:
        step = n.group(1)
        if step.isdigit():
            n = int(step)
        else:
            # Find the numeric value corresponding to the word-based ordinal
            for key, value in ordinal_dict.items():
                if value == step.lower():
                    n = int(key[:-2])  # Convert "1st" to 1, "2nd" to 2, etc.
                    break
        print('Step ' + str(n) + 'is: ' + steps[n])

    '''
    Would be nice to add sentence by sentence reading here!
    Can be done by splitting the step into sentences and reading them one by one
    '''
    '''
    Would be nice to add a "start over" option here!
    '''
    return