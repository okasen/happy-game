from model.states import Savestate
import sys
import time

from kink import inject


def pause(time_period: int):
    for dot in range(time_period):
        sys.stdout.write(".")
        sys.stdout.flush()
        time.sleep(.5)
    print("")


@inject
def judge(state: Savestate):
        response = f"Okay, let's pick up where we left off, {state.name}. "
        pause(3)
        if state.happiness > state.anger & state.despair:
            response += "You seem happy. "
            if state.happiness > 8:
                response += "ecstatic, even. "
            elif state.happiness < 4:
                response += "just a little. "
        elif state.anger > state.happiness & state.despair:
            response += "You seem angry. "
            if state.anger > 8:
                response = "Very angry. Please calm down. "
            elif state.anger < 4:
                response = "A little anger is normal. "
        elif state.despair > state.happiness & state.anger:
            response += "You don't seem well. "
            if state.despair > 8:
                response += "In fact, you seem downright despondent. "
            elif state.despair < 4:
                response += "Not too bad though, right? Right. "

        return response

def generic_line(text: str, pause_time: int):
    pause(pause_time)
    print(text)
