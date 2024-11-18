# actions.py

from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from questions import fetch_recipe, interpret_task 

class ActionProvideRecipe(Action):
    """
    Custom action to provide a recipe based on a URL provided by the user.
    """

    def name(self) -> Text:
        return "action_provide_recipe"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        # Extract the latest user message
        user_message = tracker.latest_message.get('text')
        
        # Interpret the task to extract the URL
        recipe_url = interpret_task(user_message)
        
        if recipe_url:
            # Fetch the recipe details
            recipe_details = fetch_recipe(recipe_url)
            dispatcher.utter_message(text=recipe_details)
        else:
            dispatcher.utter_message(text="I'm sorry, I couldn't find a valid recipe URL in your message. Could you please provide a valid link?")
        
        return []
