#!/usr/bin/env python2
# -*- coding: utf-8 -*-
import random
from hermes_python.hermes import Hermes

INTENT_HOW_ARE_YOU = "terezaif:how_are_you"
INTENT_GOOD = "terezaif:yes_dino"
INTENT_BAD = "terezaif:no_dino"

INTENT_FILTER_FEELING = [INTENT_GOOD, INTENT_BAD]


def main():
    with Hermes("localhost:1883") as h:
        h.subscribe_intent(INTENT_HOW_ARE_YOU, how_are_you_callback) \
         .subscribe_intent(INTENT_GOOD, feeling_good_callback) \
         .subscribe_intent(INTENT_BAD, feeling_bad_callback) \
         .start()

jokes = ["What is a dinosaur's least favorite reindeer? Comet!",
        'How do you ask a tyrannosaur out to lunch? Tea, Rex?. Are you a dinosaur?', 
"What's the best way to talk to a velociraptor? Long distance!! Are you a dinosaur?", 
"Why can't you hear a pterosaur using the bathroom? Because the p is silent! Are you a dinosaur?"]


def how_are_you_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = random.choice(jokes)
    hermes.publish_continue_session(session_id, response, INTENT_FILTER_FEELING)


def feeling_good_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "That's awesome! I love dinosoaurs."
    hermes.publish_end_session(session_id, response)


def feeling_bad_callback(hermes, intent_message):
    session_id = intent_message.session_id
    response = "Sorry to hear that. Nobody is perfect."
    hermes.publish_end_session(session_id, response)




if __name__ == "__main__":
    main()
