import regex as re


def find_temperature(task, steps, current_step, ingredients, last_query, referenced_term):
    print("This has been interpreted as a temperature related task")
    temperature_re = re.compile(r'\b(\d+)\s*((degrees|°)F|C|Farenheit|Celsius)\b', re.IGNORECASE)
    temperature_match = re.search(temperature_re, steps[current_step-1]['step'])
    temperature = temperature_match.group(1)
    unit = temperature_match.group(2)
    print(temperature)
    print(unit)
    
    return current_step, last_query
    #i = index
    #if temperature_match:
       # print(f'In step {i}, the recipe says the {tool} needs to be set at {temperature} {unit}.')
    #else:
       # level = re.search(r'\b(high|medium+(?: |-)high|medium (?: |-)low|low)\b', step, re.IGNORECASE)
        #if level:
          #  print(f'In step {i}, the recipe says the {tool} needs to be set to {level.group(1)}')
    

    #if not temperature_match:
       # print(f"The recipe doesn't say what temperature to set the {tool} to.")