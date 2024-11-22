import regex as re

async def navigation_handler(ctx, task, steps, current_step, last_query):
    #Assume steps is a list of strings, each string is a step in the recipe
    #possible special cases: start from the beginning/start over, read a step sentence by sentence, handle 1st vs first
    ordinal_dict = {"1st": "first", "2nd": "second", "3rd": "third", "4th": "fourth", "5th": "fifth", "6th": "sixth", "7th": "seventh", "8th": "eighth", "9th": "ninth", "10th": "tenth", "11th": "eleventh", "12th": "twelfth", "13th": "thirteenth", "14th": "fourteenth", "15th": "fifteenth", "16th": "sixteenth", "17th": "seventeenth", "18th": "eighteenth", "19th": "nineteenth", "20th": "twentieth"}
    # Create a pattern that includes both numeric and word-based ordinals
    ordinal_words = '|'.join(ordinal_dict.values())
    ordinal_numbers = '|'.join(ordinal_dict.keys())
    pattern = rf'\b((\d+)|{ordinal_words}|{ordinal_numbers})\b'
   
    next_step = re.compile(r'\bnext\b', re.IGNORECASE)

    prev_step = re.compile(r'\b(previous|last|back)\b', re.IGNORECASE)

    nth_step = re.compile(pattern, re.IGNORECASE)
    repeat = re.compile(r'\b(repeat|this step)\b', re.IGNORECASE)

    #if repeat is mentioned, print the current step
    repeat_flag = re.search(repeat, task)
    if repeat_flag:
        #re_print current step
        last_query['query'] = task
        last_query['output'] = steps[current_step-1]['step']
        return current_step, last_query
    
    
    #if next step is mentioned, print the next step
    if re.search(next_step, task):
        ## Can only print the next step if we are not on the last step
        if current_step == len(steps):
            await ctx.send("This is the last step, try again.")
            return current_step, last_query
        ## Increment current_step, print the corresponding sentence
        current_step = current_step + 1
        # await ctx.send(steps[current_step - 1]['step'])
        last_query['query'] = task
        last_query['output'] = steps[current_step-1]['step']
        return current_step, last_query
    
    previous = re.search(prev_step, task)
    #if previous step is mentioned, print the previous step
    if re.search(prev_step, task):
        print("PREVIOUS")
        ## Can only print the last step if we are not on the first step
        if current_step == 1:
            await ctx.send("There are no preceding steps, try again.")
            return current_step, last_query
        current_step -= 1
        last_query['query'] = task
        last_query['output'] = steps[current_step-1]['step']
        return current_step, last_query
    
    #if a specific step is mentioned, print that step
    n = re.search(nth_step, task)
    if n:
        step = n.group(1)
        if step.isdigit():
            n = int(step)
            if 1 <= n <= len(steps):
                current_step = n
                last_query['query'] = task
                last_query['output'] = steps[current_step - 1]['step']
                return current_step, last_query
            else:
                await ctx.send(f"Step {n} is out of range. Please try again.")
                return current_step, last_query
        else:
            # Find the numeric value corresponding to the word-based ordinal
            for key, value in ordinal_dict.items():
                if value == step.lower():
                    n = int(key[:-2])
                    if 1 <= n <= len(steps):
                        current_step = n
                        last_query['query'] = task
                        last_query['output'] = steps[current_step - 1]['step']
                        return current_step, last_query
                    else:
                        await ctx.send(f"Step {n} is out of range. Please try again.")
                        return current_step, last_query
                    
    print("HELLO")
    last_query['query'] = task
    last_query['output'] = steps[current_step-1]['step']
    return current_step, last_query