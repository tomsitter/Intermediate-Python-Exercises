"""
This is Part 1 of 2.

Part 1 is designed to test your ability to write code that is easy to read and understand.
It tests your comfort with OOP, functions, iteration, and use of Python language features.

Both parts will involve writing code that manipulates a list of ScheduleEvent objects.
ScheduleEvents represent content that has been scheduled to play on a streaming channel
You will be given a list of ScheduleEvents and asked to write functions that manipulate
them.

For each of the exercises below you are encouraged to modify the ScheduleEvent class to help solve the task,
but you are not allowed to modify the example_schedule variable.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime


@dataclass(frozen=True)
class ScheduleEvent:
    """
    ScheduleEvent class
    """

    asset_id: int
    start: datetime
    end: datetime


# Example data
example_schedule = [
    ScheduleEvent(
        asset_id=2,
        start=datetime.fromisoformat("2020-01-01 10:00:00"),
        end=datetime.fromisoformat("2020-01-01 10:30:00"),
    ),
    ScheduleEvent(
        asset_id=1,
        start=datetime.fromisoformat("2020-01-01 09:30:00"),
        end=datetime.fromisoformat("2020-01-01 10:15:00"),
    ),
    ScheduleEvent(
        asset_id=3,
        start=datetime.fromisoformat("2020-01-01 10:30:00"),
        end=datetime.fromisoformat("2020-01-01 11:30:00"),
    ),
    ScheduleEvent(
        asset_id=4,
        start=datetime.fromisoformat("2020-01-01 11:30:00"),
        end=datetime.fromisoformat("2020-01-01 11:35:00"),
    ),
]


# Exercise 1. Create a new list with the events sorted by start time.
#             Do not modify the original list.


# Exercise 2. Create a list with only events from example_schedule that have a duration
#             of less than 15 minutes.
#             Do not modify the original list.


# Exercise 3. Create a list of gaps between events. A gap is defined as a period of time
#             between two events where no event is scheduled.
#             Use your best judgement to create the returned data structure.
#             Do not modify the original list.
