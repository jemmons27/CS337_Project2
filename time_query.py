import regex as re
import spacy

async def find_time(ctx, task, steps, current_step, ingredients, last_query):
    doc = steps[current_step - 1]['doc']
    response = []
    rest_of_phrase = False
    until_re = re.compile(r'\buntil\b', re.IGNORECASE)
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
        await ctx.send('No response found, please restructure your query')
        return current_step, last_query
    response = ' '.join(response)
    await ctx.send(response)
    last_query['query'] = task
    last_query['output'] = response
    return current_step, last_query