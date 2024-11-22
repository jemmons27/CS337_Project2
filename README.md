# CS337_Project2
Project 2 - Parsing recipes to support conversational interaction

Hi! Welcome to our conversational recipe bot. To run this app, use the discord token in the Canvas submission and in replace bot.run(TOKEN), replace the token with the string token. Then, you can run bot.py which runs the backend. The user interface is through discord. Simon, you should be added to the Recipes server with the bot. Navigate to **DMs** with the bot. To start the interaction, type !start_recipe. Then, you should be able to interact with it. Here are a list of questions that work for each of the conversational goals. 

Recipe retrieval and display (see example above, including "Show me the ingredients list")

Entering the URL will also show you the ingredients list.

Navigation utterances ("Go back one step", "Go to the next step", "Repeat please", "Take me to the 1st step", "Take me to the n-th step")

Next, go back to previous, repeat, go to step [n] are all supported, amongst others. 

Asking about the parameters of the current step ("How much of <ingredient> do I need?", "What temperature?", "How long do I <specific technique>?", "When is it done?", "What can I use instead of <ingredient or tool>")

How much <ingredient> do i need: answers only for the step, will be inaccurate if the ingredient isnt mentioned in the current step
How much <ingredient> do i need in the recipe for broader questions
How high heat
How long do I <action>

Simple "what is" questions ("What is a <tool being mentioned>?")

This would take you to a search query but you can enter that question. 

Specific "how to" questions ("How do I <specific technique>?").

This would take you to a search query but you can enter that question. 

Vague "how to" questions ("How do I do that?" – use conversation history to infer what “that” refers to)

This would take you to a search query based on what the step is but you can enter that question. 

Hi! Welcome to our conversational recipe bot. To run this app, use the discord token in the Canvas submission and in replace bot.run(TOKEN), replace the token with the string token. Then, you can run bot.py which runs the backend. The user interface is through discord. Simon, you should be added to the Recipes server with the bot. Navigate to **DMs** with the bot. To start the interaction, type !start_recipe. Then, you should be able to interact with it. Here are a list of questions that work for each of the conversational goals. 

Recipe retrieval and display (see example above, including "Show me the ingredients list")

Entering the URL will also show you the ingredients list.

Navigation utterances ("Go back one step", "Go to the next step", "Repeat please", "Take me to the 1st step", "Take me to the n-th step")

Next, go back to previous, repeat, go to step [n] are all supported, amongst others. 

Asking about the parameters of the current step ("How much of <ingredient> do I need?", "What temperature?", "How long do I <specific technique>?", "When is it done?", "What can I use instead of <ingredient or tool>")

How much <ingredient> do i need: answers only for the step, will be inaccurate if the ingredient isnt mentioned in the current step
How much <ingredient> do i need in the recipe for broader questions
How high heat
How long do I <action>

Simple "what is" questions ("What is a <tool being mentioned>?")

This would take you to a search query but you can enter that question. 

Specific "how to" questions ("How do I <specific technique>?").

This would take you to a search query but you can enter that question. 

Vague "how to" questions ("How do I do that?" – use conversation history to infer what “that” refers to)

This would take you to a search query based on what the step is but you can enter that question. 