import regex as re
import spacy

def find_temperature(task, steps, current_step, ingredients, last_query):
   print("This has been interpreted as a temperature related task")
   nlp = spacy.load('en_core_web_sm')
   doc = nlp(task)
   tools = []
   for token in doc:
      ##Tools referenced in task are usually nsubj
      if token.dep_ == 'nsubj':
         tools.append(token.text)
   ##Do we need to specify Celsius vs fahrenheit if both are in the recipe?
   temperature_re = re.compile(r'\b(\d+)\s*((degrees|°) (F|C|Farenheit|Celsius))\b', re.IGNORECASE)
   temperature_match = re.search(temperature_re, steps[current_step-1]['step'])
   if temperature_match:
      temperature = temperature_match.group(1)
      unit = temperature_match.group(2)
      res = ''
      if tools != []:
         res = res + 'Set the ' + tools[0] + " to "
      if temperature != '':
         res = res + temperature + ' '
      if unit != '':
         res = res + unit
      print(res)
      last_query['query'] = task
      last_query['output'] = res
   else:
      print("Couldn't find a temperature in this step, try another query or navigate to another step")
      
   return current_step, last_query
