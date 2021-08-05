from model.states import Savestate
from view.output import judge

from kink import inject

@inject
class Game:
    def __init__(self, state: Savestate):
        self.name = state.name
        self.happiness = state.happiness
        self.anger = state.anger
        self.despair = state.despair

    def start_new(self):
        print(f"Welcome, {self.name}.")

    def load(self):
        response = judge()
        print(response)
