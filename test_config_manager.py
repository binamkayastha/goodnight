from copy import deepcopy

from config_manager import create_new_config

# Todo: Switch to fixture so we don't have to do deepcopies
ARBITRARY_CONFIG = {
    "rituals": [
        {
            "task": "brush teeth",
            "time": 20
        }, {
            "task": "wash dishes",
            "time": 50
        },
    ],
    "bedtime": {
        "hour": 22,
        "minute": 00
    }
}

class TestCreateNewConfig():

    def test_faulty(self):
        assert True

    def test_no_change_on_empty_ritual_times(self):
        actual = create_new_config(
            file_config=ARBITRARY_CONFIG,
            app_config=ARBITRARY_CONFIG,
            ritual_times=[]
        )
        expected = ARBITRARY_CONFIG
        assert expected == actual

    def test_time_updates_on_new_ritual_time(self):
        ritual_times = [{
            "task": "brush teeth",
            "time": 2
        }]
        actual = create_new_config(
            file_config=ARBITRARY_CONFIG,
            app_config=ARBITRARY_CONFIG,
            ritual_times=ritual_times
        )
        expected = deepcopy(ARBITRARY_CONFIG)
        expected["rituals"][0]["time"] = 2
        assert expected == actual

    def test_time_does_not_update_if_manually_changed(self):
        ritual_times = [{
            "task": "brush teeth",
            "time": 2
        }]
        file_config = deepcopy(ARBITRARY_CONFIG)
        file_config["rituals"][0]["time"] = 4
        actual = create_new_config(
            file_config=file_config,
            app_config=ARBITRARY_CONFIG,
            ritual_times=ritual_times
        )
        expected = deepcopy(ARBITRARY_CONFIG)
        expected["rituals"][0]["time"] = 4
        assert expected == actual

