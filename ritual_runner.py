import schedule
from datetime import datetime, timedelta
from aiy.audio import say
from aiy.leds import Leds, Color
from config_manager import update_config_times

button = aiy.voicehat.get_button()
leds = Leds()


def run_rituals(rituals: List[Dict]):
    print("Rituals Ran!")
    print(rituals)
    new_times = {}
    for ritual in rituals:
        time_taken = run_ritual(ritual)
        new_times[ritual.get("task")] = time_taken
    update_config_times(new_times)
    # CancelJob so that a new time can be created based on updated config file
    return schedule.CancelJob


def run_ritual(ritual) -> timedelta:
    name = ritual.get("task")
    _ready(name)
    button.wait_for_press()
    time_taken = _doing(name)
    # Todo: fix pluarlity of time
    if time_taken.hour > 0:
        say(f"That took you {time_taken.hour} hours")
    else:
        say(f"That took you {time_taken.minute} minutes")
    return time_taken

def _ready(name: str):
    say(f"Your next task is {name}!")
    leds.update(Leds.rgb_on(Color.GREEN))


def _doing(name: str) -> timedelta:
    say(f"Go {name}!")
    leds.update(Leds.rgb_on(Color.GREEN))
    start_time = datetime.now()
    button.wait_for_press()
    end_time = datetime.now()
    return diff
