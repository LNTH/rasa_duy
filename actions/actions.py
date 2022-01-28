from re import T
from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker, FormValidationAction
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import (
    EventType
)
import random
import time

import logging
logger = logging.getLogger(__name__)

class ValidateRestaurantForm(FormValidationAction):
    def name(self) -> Text:
        return "validate_form_restaurant"

    def validate_ent_cuisine(self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return {"ent_cuisine": slot_value}
    
    def validate_ent_num_people(self,
        slot_value: Any, 
        dispatcher: CollectingDispatcher,
        tracker: Tracker,
        domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
        return {"ent_num_people": slot_value}


class ActionVerifyRestaurant(Action):
    def name(self) -> Text:
        return "action_verify_restaurant"
    
    def run(
        self, dispatcher: CollectingDispatcher, tracker: Tracker, domain: Dict
    ) -> List[EventType]:
        time.sleep(5)
        random_number = random.randint(0,1)
        if random_number == 0:
            dispatcher.utter_message(response="utter_booking_successfull")
        else:
            dispatcher.utter_message(response="utter_can_not_find_restaurant")
        return []

