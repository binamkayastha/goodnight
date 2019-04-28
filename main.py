#!/usr/bin/env python3
"""A voicekit application to optimize your bedtime ritual.

Voice Command:
- Reads from a list from the current state file, which can be edited manually if wanted
Task; minutes estimated it will take; fixed (optional)
bedtime, fixed time value
- Bedtime in another file.
- Logs in format of
Version Date
Data

Example yaml file:
rituals:
  - task: brush teeth
    time: 2 minutes
    algorithm: fixed # optional, defaults to moving average
bedtime:
  - hour: 22
  - minute: 10 # optional

Data is logged as a list of json files
{
    date: {
        ritual [
            {
                task: string
                time: int minutes
                algorithm: algorithm enum
                actual_time: int minutes
            },
        ],
        bedtime: unixtimestamp
        actual_bedtime: unixtimestamp
    }
}
"""
import schedule
from datetime import datetime
from time import sleep, strftime
from typing import Dict, List

import goodnight
import ritual_runner
import config_manager


def main():
    """Entrypoint of application

    Tech-debt:
    Using default Timezone which is probably a bad idea but whatevs.
    """
    while True:
        config: Dict = config_manager.get_config()
        rituals: List[Dict] = config.get("rituals")
        validate(config)
        current_date = datetime.now().date()
        start_time: datetime = goodnight.get_start_time(config, current_date)
        schedule_ritual(start_time, rituals)
        run_while_scheduled_job_exists()


def validate(config: Dict):
    """Raises errors if the dictionary doesn't fit the template"""
    pass


def schedule_ritual(start_time: datetime, rituals: List[Dict]):
    value = start_time.strftime("%H:%M")
    value = "03:04"
    print(f"Scheduling job for: {value}")
    schedule.every().day.at(value).do(
            ritual_runner.run_rituals, rituals=rituals)

def run_while_scheduled_job_exists():
    while schedule.jobs:
        schedule.run_pending()
        sleep(1)

if __name__ == '__main__':
    main()
