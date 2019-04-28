from datetime import date, datetime, timedelta

from goodnight import get_start_time

BEDTIME_HOUR = 22
BEDTIME_MINUTE = 0
TEST_DATE = date(2019, 4, 26)
TOMORROW = date(TEST_DATE.year, TEST_DATE.month, TEST_DATE.day + 1)


class TestGetStartTime:

    def test_is_bedtime_tomorrow_when_no_rituals(self):
        no_ritual_config = {
            "rituals": [],
            "bedtime": {
                "hour": BEDTIME_HOUR,
                "minute": BEDTIME_MINUTE
            }
        }
        expected = datetime(
            year=TOMORROW.year,
            month=TOMORROW.month,
            day=TOMORROW.day,
            hour=BEDTIME_HOUR,
            minute=BEDTIME_MINUTE
        )
        actual = get_start_time(
            config=no_ritual_config, current_date=TEST_DATE)
        assert expected == actual

    def test_is_bedtime_x_minutes_back_from_one_ritual(self):
        one_ritual_config = {
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
                "hour": BEDTIME_HOUR,
                "minute": BEDTIME_MINUTE
            }
        }
        expected = datetime(
            year=TOMORROW.year,
            month=TOMORROW.month,
            day=TOMORROW.day,
            hour=BEDTIME_HOUR-2,
            minute=50
        )
        actual = get_start_time(
            config=one_ritual_config, current_date=TEST_DATE)
        assert expected == actual

