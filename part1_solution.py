"""
This is the SOLUTION to Part 1 of 2.

Part 1 is designed to test your ability to write code that is easy to read and understand.
It tests your comfort with OOP, functions, iteration, and use of Python language features.

Both parts will involve writing code that manipulates a list of ScheduleEvent objects.
ScheduleEvents represent content that has been scheduled to play on a streaming channel
You will be given a list of ScheduleEvents and asked to write functions that manipulate
them.

For each of the exercises below you are allowed to:
    - Import any packages from the standard library
    - Modify the ScheduleEvent class

You are *not* allowed to modify the example_schedule variable or use a third-party library.
"""

from __future__ import annotations

from dataclasses import dataclass
from datetime import datetime, timedelta


@dataclass(frozen=True)
class ScheduleEvent:
    """
    Represents a scheduled event
    """

    asset_id: int
    start: datetime
    end: datetime

    @property
    def duration(self):
        """
        Return the duration of the event
        """
        return self.end - self.start

    def __lt__(self, other: ScheduleEvent) -> bool:
        """
        Compare two events for sorting
        """
        return self.start < other.start
    

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
        end=datetime.fromisoformat("2020-01-01 09:45:00"),
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


def sort_schedule(schedule: list[ScheduleEvent]) -> list[ScheduleEvent]:
    """
    Sort the schedule by start time
    :param schedule: list of scheduled events
    :return: sorted list of scheduled events
    """

    return sorted(schedule, key=lambda e: e.start)


sorted_schedule = sort_schedule(example_schedule)

assert [event.asset_id for event in sorted_schedule] == [1, 2, 3, 4]

# Exercise 2. Create a list with only events from example_schedule that have a duration
#             of less than 15 minutes.
#             Do not modify the original list.


def find_events_under_duration(
    schedule: list[ScheduleEvent], duration: timedelta
) -> list[ScheduleEvent]:
    """
    Find events under a certain duration
    :param schedule: list of scheduled events
    :param duration: duration to check
    :return: list of events under the duration
    """
    return [e for e in schedule if e.duration < duration]


events_under_threshold = find_events_under_duration(
    example_schedule, timedelta(minutes=15)
)

assert len(events_under_threshold) == 1 and events_under_threshold[0].asset_id == 4

# Exercise 3. Create a list of gaps between events. A gap is defined as a period of time
#             between two events where no event is scheduled.
#             Use your best judgement to create the returned data structure.
#             Do not modify the original list.


@dataclass(frozen=True)
class ScheduleGap:
    """
    Represents a gap in the schedule
    """

    start: datetime
    end: datetime


def find_gaps(schedule: list[ScheduleEvent]) -> list[ScheduleGap]:
    """
    Find gaps between events
    :param schedule: list of scheduled events
    :return: list of ScheduleGap objects
    """
    schedule = sorted(schedule)
    return [
        ScheduleGap(start=e1.end, end=e2.start)
        for e1, e2 in zip(schedule, schedule[1:])
        if e2.start - e1.end > timedelta(seconds=0)
    ]


schedule_gaps = find_gaps(example_schedule)

assert len(schedule_gaps) == 1
assert schedule_gaps[0] == ScheduleGap(
    start=datetime.fromisoformat("2020-01-01 09:45:00"),
    end=datetime.fromisoformat("2020-01-01 10:00:00"),
)
