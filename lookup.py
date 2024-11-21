import regex as re
#### lookup_re = re.compile(r"\b(what is|what's|whats|define|how do i|how is|show me how to|show me what)\b", re.IGNORECASE)

"""
File containing lookup_handler, which is called for any search related query (whats a spoon, how do i do that, etc.)

lookup_handler splits queries based on if they contain a specific tool/process/ingredient to lookup or if they reference
earlier queries, then creates and returns a youtube link
"""
    
def lookup_handler(task, steps, current_step, ingredients, last_query):
    url_type = ''
    while url_type == '':
        print(('Select the type of search you prefer:\n'
               '[1] Google\n'
               '[2] Youtube'))
        url_type = input('Input response > ')
        if (url_type != '1') & (url_type != '2'):
            url_type = ''
            print("Didn't understand selection. Please try again, entering only a number")
    no_specific_item = re.compile(r"\b(do that|do this|is that|is this|what's that|whats that)\b", re.IGNORECASE)
    if re.search(no_specific_item, task):
        ###lookup last task
        print("Lookup_handler has determined there is no specific task mentioned, parsing last query to find noun/verb to lookup")
        print("UNIMPLEMENTED")
        ##### 
        #
        #TODO
        #
        #####
        url = ''
    else:
        tokens = task.split()
        if url_type == '1':
            url = "https://www.google.com/search?q="
        else:
            url = "https://www.youtube.com/results?search_query="
        for word in tokens:
            url = url + '+' + word
        print(url)
    last_query['query'] = task
    last_query['output'] = url
    return current_step, last_query