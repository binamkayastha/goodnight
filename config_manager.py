from copy import deepcopy
from typing import Dict, List
import yaml

CONFIG_FILE = "bedtime.yaml"
config = {}


def get_config() -> Dict:
    """Returns Dict from config.yaml in current file.

    Returns a copied dict so application can't modify config directly"""
    global config
    if not config:
        config = get_new_config()
    copied_config = deepcopy(config)
    return copied_config


def get_new_config():
    with open(CONFIG_FILE, 'r') as stream:
        try:
            config = yaml.safe_load(stream)
            print(f"Retrieved new config from {CONFIG_FILE}")
            print(config)
            return config
        except yaml.YAMLError as exc:
            print(exc)
            return {}


def update_config_times(ritual_times: Dict) -> Dict:
    """Updates the config files ritual times, and also returns the config.

    Will not update the ritual time, if it has been modfied by the user
    since the last time the config was updated.
    current_config will be different from config if the user
    modified the yaml file."""
    new_config = create_new_config(
        file_config=get_new_config(),
        app_config=config,
        ritual_times=ritual_times)
    with open(CONFIG_FILE, 'w') as filetowrite:
        filetowrite.write(yaml.dump(new_config))


# Todo: Test a while bunch of edge cases
def create_new_config(
        file_config: Dict, app_config: Dict, ritual_times: List[Dict]):
    # current_rituals = file_config.get("rituals")
    app_rituals = app_config.get("rituals")
    new_config = deepcopy(app_config)
    for new_ritual in ritual_times:
        index, matching_ritual = next(
            (i, ritual) for (i, ritual) in enumerate(new_config["rituals"])
            if ritual.get("task") == new_ritual.get("task"))
        file_not_changed = file_config["rituals"][index] == new_config["rituals"][index]
        if file_not_changed and matching_ritual:
            new_config["rituals"][index]["time"] = new_ritual.get("time")
        else:
            new_config["rituals"][index]["time"] = file_config["rituals"][index]["time"]

    return new_config


# Todo: save todays config
