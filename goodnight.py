#!/usr/bin/env python3
from datetime import date, datetime, timedelta
from typing import Dict, List


def get_start_time(config: Dict, current_date: date) -> datetime:
    ritual_time = get_ritual_time(config.get("rituals"))
    bedtime_hour = config.get("bedtime").get("hour")
    bedtime_minute = config.get("bedtime").get("minute")
    bedtime = datetime(
        year=current_date.year,
        month=current_date.month,
        day=current_date.day + 1,
        hour=bedtime_hour,
        minute=bedtime_minute
    )
    start_time = bedtime - timedelta(minutes=ritual_time)
    return start_time


def get_ritual_time(rituals: List[Dict]) -> int:
    return sum([ritual.get("time") for ritual in rituals])

