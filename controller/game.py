from model.states import Savestate, get_state
from view.output import judge, generic_line, choices

from kink import inject

@inject
class Game:
    def __init__(self, state: Savestate):
        self.name = state.name
        self.happiness = state.happiness
        self.anger = state.anger
        self.despair = state.despair

    def start_new(self):
        generic_line(f"Welcome, {self.name}.", 3)
        generic_line("Why don't you tell me what brings you here?", 0)
        generic_line("To make things easier, I'll give you some examples.", 0)
        generic_line("Just tell me the number of your response:", 0)
        choices({"despair": "I feel tired all of the time", "anger": "I get angry too easily","happiness": "I don't remember"}, True)
        get_state()
    def load(self):
        response = judge()
        print(response)
