# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/core/actions/#custom-actions/


# This is a simple example for a custom action which utters "Hello World!"

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

        txt = (tracker.latest_message)['text']
        stock = re.search("(?<=find the price of ).*|$", txt).group()
        dispatcher.utter_message(stock)

        return []
