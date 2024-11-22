import regex as re
import spacy
from nltk.corpus import verbnet
from discord.ext import commands
#### lookup_re = re.compile(r"\b(what is|what's|whats|define|how do i|how is|show me how to|show me what)\b", re.IGNORECASE)

"""
File containing lookup_handler, which is called for any search related query (whats a spoon, how do i do that, etc.)

lookup_handler splits queries based on if they contain a specific tool/process/ingredient to lookup or if they reference
earlier queries, then creates and returns a youtube link
"""
    
async def lookup_handler(ctx, task, steps, current_step, ingredients, last_query):
    """
    Handles lookup requests in a Discord bot context.
    Replaces print and input with bot message interactions.
    """
    url_type = ''
    while url_type == '':
        await ctx.send(
            "Select the type of search you prefer:\n"
            "[1] Google\n"
            "[2] YouTube\n"
            "Please type the number of your choice:"
        )

        def check(message):
            return message.author == ctx.author and message.channel == ctx.channel

        try:
            response = await ctx.bot.wait_for("message", check=check, timeout=60)
            url_type = response.content.strip()
            if url_type not in ['1', '2']:
                url_type = ''
                await ctx.send("Didn't understand selection. Please try again, entering only a number.")
        except Exception as e:
            await ctx.send("Timeout or error occurred. Please try the command again.")
            return current_step, last_query

    # Identify if there's no specific item in the task
    no_specific_item = re.compile(
        r"\b(.*)\s+\b(do that|do this|is that|is this|what's that|whats that)\b",
        re.IGNORECASE
    )

    if re.search(no_specific_item, task):
        await ctx.send(
            "Lookup handler determined there is no specific task mentioned. Parsing last query to find a noun/verb to lookup."
        )
        matches = re.search(no_specific_item, task)
        last_output = last_query['output']

        # Construct a new task combining matches with the last output
        task = matches.group(1) + last_output

    # Tokenize task and build search URL
    tokens = task.split()
    url = "https://www.google.com/search?q=" if url_type == '1' else "https://www.youtube.com/results?search_query="
    url += '+'.join(tokens)

    # Send the constructed URL
    await ctx.send(f"Here is your search result: {url}")

    # Update last query
    last_query['query'] = task
    last_query['output'] = url

    return current_step, last_query