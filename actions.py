# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


from typing import Any, Text, Dict, List

import re

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher


class ActionFindStockPrice(Action):

    def name(self) -> Text:
        return "action_find_stock_price"

    def run(self, dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        
        resp = ""
        txt = (tracker.latest_message)['text']
        stock = re.search("(?<=the price of )[^?]*|$", txt).group()
# To make the actual version of the ticker bot that calls an api, you're going to want to call an api and see if the variable 'stock' equals
# a real stock symbol or name of a stock  
        if stock != "":
            resp = "The price of " + stock + " is $237.55."
        else:
            resp = "Sorry, I didn't catch that."
        dispatcher.utter_message(resp)

        return []
