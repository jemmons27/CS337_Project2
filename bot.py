# bot.py
# import os
# import random
# import web_scraping
# import task_navigation

# import discord
# from dotenv import load_dotenv

# load_dotenv()
# TOKEN = os.getenv('DISCORD_TOKEN')
# GUILD = "Recipes!"


import discord
from discord.ext import commands

# Mocking external dependencies for the example
import web_scraping
import task_navigation


bot = commands.Bot(command_prefix="!", intents=discord.Intents.default())

# Dictionary to hold user sessions
user_sessions = {}

@bot.event
async def on_ready():
    print(f'{bot.user.name} has connected to Discord!')

@bot.command(name="start_recipe")
async def start_recipe(ctx):
    user_id = ctx.author.id

    # Prompt the user to enter a recipe URL
    await ctx.send("Enter a recipe URL from Allrecipes.com:")

    def check(message):
        return message.author == ctx.author and message.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=60)
        url = msg.content

        # Fetch recipe details
        soup, steps, ingredients = web_scraping.fetch_recipe(url)
        
        # Initialize user session
        user_sessions[user_id] = {
            "steps": steps,
            "ingredients": ingredients,
            "current_step": 1,
            "last_query": {"task": "", "output": ""}
        }
        
        # Send ingredients list
        ingredient_list = '\n'.join(
            [f"{ingredient['quantity']} {ingredient['unit']} {ingredient['name']}" for ingredient in ingredients]
        )
        await ctx.send(f"You need the following ingredients:\n{ingredient_list}")
        
        await ctx.send("Press any key to start cooking! (Type anything and send it)")
        _ = await bot.wait_for('message', check=check, timeout=60)

        await proceed_to_step(ctx, user_id)

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")

async def proceed_to_step(ctx, user_id):
    session = user_sessions.get(user_id)
    if not session:
        await ctx.send("Session not found. Please start a new recipe using `!start_recipe`.")
        return

    current_step = session["current_step"]
    steps = session["steps"]

    if current_step > len(steps):
        await ctx.send("You've completed the recipe! Enjoy your meal!")
        user_sessions.pop(user_id, None)  # Clear session
        return

    step_text = steps[current_step - 1]["step"]
    session["last_query"]["output"] = step_text

    await ctx.send(f"||| Step {current_step}: {step_text}")
    await ctx.send("Ask a question, request a different step, or type '0' to exit.")

    def check(message):
        return message.author.id == user_id and message.channel == ctx.channel

    try:
        msg = await bot.wait_for('message', check=check, timeout=300)  # Wait for user input
        task = msg.content
        if task == "0":
            await ctx.send("You've exited the recipe. Have a great day!")
            user_sessions.pop(user_id, None)  # Clear session
            return

        # Navigate to resolve task
        current_step, last_query = await task_navigation.direct_task(ctx,
            task, session["steps"], session["current_step"], steps, session["ingredients"], session["last_query"]
        )

        # Update session
        session["current_step"] = current_step
        session["last_query"] = last_query

        await proceed_to_step(ctx, user_id)

    except Exception as e:
        await ctx.send(f"An error occurred: {e}")
        user_sessions.pop(user_id, None)  # Clear session

bot.run(TOKEN)

# def main():
#     url = input('Enter a recipe url from Allrecipes.com > ')
#     soup, steps, ingredients = web_scraping.fetch_recipe(url)
#     task = '' # Task holds the current query, and is overwritten each time a new query is input
#     last_query= {'task': task, 'output': ''} #last_query is a dict with keys 'task' and 'output', which store the query and output of the most
#     #recent interaction. it is overwritten each time the bot outputs in response to a query
#     current_step = 1
#     ## curr_step is an int marking current step. Always use curr_step-1 when indexing steps, as "step 1" corresponds to steps[0]
    
#     print('Welcome to the Recipe Bot! Press enter to start the recipe. Type "0" to exit.')
#     input()
#     print('You need the following ingredients:')
#     for ingredient_info in ingredients:
#         print(ingredient_info['quantity'] + " " + ingredient_info['unit'] + " " + ingredient_info['name'])  

#     print('\n')
#     input('Press enter to start cooking!')
#     print('Get ready to cook!\n\n')
#     while current_step <= len(steps) and task != '0':
#         print(f'||| Step {current_step}: {steps[current_step-1]["step"]}\n\n')
#         print(f'Ask a question or ask me to move to a different step!')
#         last_query['output'] = steps[current_step-1]['step']
        
#         task = input('||| Type here > ')
#         #### Navigate and resolve task, heading first to task_navigation.py at the direct_task function
#         current_step, last_query = task_navigation.direct_task(task, soup, current_step, steps, ingredients, last_query)
#     print("You've completed the recipe! Enjoy your meal!")
    
    
    
    
# if __name__ == "__main__":
#     main()
