from matplotlib import colors
import re
from dataclasses import dataclass

from kink import di, inject

@dataclass
class Savestate:
    name: str
    happiness: int
    anger: int
    despair: int

def load_savestate(username: str, savestate: str) -> Savestate:
    number_state: str = str(colors.to_rgba(savestate))
    raw_numbers: str = re.search(r'\((.*?)\)', number_state).group(1)
    state_string: list = raw_numbers.split(",")
    loaded_happiness: int = int(float(state_string[0])*10)
    loaded_anger: int = int(float(state_string[1])*10)
    loaded_despair: int = int(float(state_string[2])*10)
    loaded_state: Savestate = Savestate(
        name=username,
        happiness=loaded_happiness,
        anger=loaded_anger,
        despair=loaded_despair)

    return loaded_state

def new_savestate(username: str) -> Savestate:
    new_state: Savestate = Savestate(
        name=username,
        happiness=3,
        anger=3,
        despair=3)

    return new_state

@inject
def modify_emotions(emotion: str, increase: bool, state: Savestate) -> None:
    print(emotion)
    if increase:
      modifier = 1
    else:
      modifier = -1
    if emotion == "happiness":
      print("increasing happiness")
      state.happiness += modifier
    elif emotion == "despair":
      print("increasing despair")
      state.despair += modifier
    elif emotion == "anger":
      print("increasing anger")
      state.anger += "modifier"

    di["states"] = state


@inject
def get_state(state: Savestate) -> None:
  print(state.happiness)
  print(state.anger)
  print(state.despair)

