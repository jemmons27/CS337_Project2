import regex as re
import spacy

def find_temperature(task, steps, current_step, ingredients, last_query):
   print("This has been interpreted as a temperature related task")
   nlp = spacy.load('en_core_web_sm')
   tools = re.findall(r'\b(oven|stove|burner|pot|pan|grill|microwave)\b', task, re.IGNORECASE)
   ##Do we need to specify Celsius vs fahrenheit if both are in the recipe?
   temperature_re = re.compile(r'\b(\d+)\s*((degrees|°) (F|C|Farenheit|Celsius))\b', re.IGNORECASE)
   # Regular expression to match temperature levels
   level_re = re.compile(r'\b(high|medium(?: |-)high|medium(?: |-)low|low)\b', re.IGNORECASE)
   
   temperature_match = re.search(temperature_re, steps[current_step-1]['step'])
   if temperature_match:
      temperature = temperature_match.group(1)
      unit = temperature_match.group(2)
      res = ''
      if tools:
            res += 'Set the ' + tools[0] + " to "
      if temperature:
         res += temperature + ' '
      if unit:
         res += unit
      print(res)
      last_query['query'] = task
      last_query['output'] = res
   else:
      # Search for temperature levels in the current step
        level_match = re.search(level_re, steps[current_step-1]['step'])
        if level_match:
            level = level_match.group(1)
            res = ''
            if tools:
                res += 'Set the ' + tools[0] + " to "
            res += level
            print(res)
            last_query['query'] = task
            last_query['output'] = res
        else:
            print("Couldn't find a temperature in this step, try another query or navigate to another step")
    
   return current_step, last_query
