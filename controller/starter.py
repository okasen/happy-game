from view.output import generic_line
from model.states import load_savestate, new_savestate
from controller.game import Game

from kink import di

class Loadscreen:
    def name_getter():
        generic_line("Can you remind me of your name?", 3)
        name = input()
        return name

    def save_getter():
        generic_line("I'm sorry, I'm getting patients mixed up. Is this your first session?", 3)
        generic_line("say 'yes' or 'no'", 0)
        first = input()
        if first == "no":
            generic_line("do you remember the color I mentioned at the end of the last session?", 3)
            generic_line("(enter your color or 'no', please)", 0)
            save = input()
        elif first == "yes":
            generic_line("Ah, I see.", 3)
            save = "new"
        else:
            generic_line("I don't think I understand you; please try to cooperate. Let's start from scratch.", 0)
            save = "new"
        return save


def start():
    generic_line("Hello there. ", 3)
    username = Loadscreen.name_getter()
    saved_game = Loadscreen.save_getter().lower()
    if saved_game == "new":
        state = new_savestate(username)
        di["state"] = state
        game = Game()
        di["game"] = game
        game.start_new()
    else:
        state = load_savestate(username, saved_game)
        di["state"] = state
        game = Game()
        di["game"] = game
        game.load()
