"""
This is Part 2 of 2.

Part 2 is designed to test your ability to read and understands some else's code and
to troubleshoot and fix it.

You will be given a list of ScheduleEvents and asked to write functions that manipulate
them.
"""

from __future__ import annotations

import unittest
from dataclasses import dataclass
from datetime import datetime

# -------------------
# Exercise
#
# A co-worker is trying to find any events that overlap in time.
# An event that ends at the same time another starts is not considered an overlap.
# He has provided the following implementation and tests.
# Read and write any additional tests to determine whether his implementation is correct.
# If it is not correct, fix it.
# -------------------


@dataclass(frozen=True)
class ScheduleEvent:
    """
    ScheduleEvent class
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

    def overlaps(self, other: ScheduleEvent) -> bool:
        """
        Check if two events overlap
        """
        return self.start <= other.end and self.end >= other.start


def find_overlapping_events(schedule: list[ScheduleEvent]) -> list[ScheduleEvent]:
    """
    Find overlapping events
    :param schedule: list of scheduled events
    :return: list of overlapping events. Only returns the first overlapping event.
    """
    schedule = sorted(schedule)
    overlapping = []
    for e1, e2 in zip(schedule, schedule[1:]):
        if e1.overlaps(e2):
            overlapping.append(e1)
    return overlapping


# -------------------
# Tests
# -------------------


class TestFindOverlappingEvents(unittest.TestCase):
    """
    Tests for find_overlapping_events function
    """

    def test_no_overlaps(self):
        """
        Test that no overlapping events are found
        """
        no_overlap_schedule = [
            ScheduleEvent(
                asset_id=1,
                start=datetime.fromisoformat("2020-01-01 10:00:00"),
                end=datetime.fromisoformat("2020-01-01 10:30:00"),
            ),
            ScheduleEvent(
                asset_id=2,
                start=datetime.fromisoformat("2020-01-01 11:30:00"),
                end=datetime.fromisoformat("2020-01-01 12:30:00"),
            ),
        ]
        self.assertEqual(find_overlapping_events(no_overlap_schedule), [])

    def test_overlaps(self):
        """
        Test that overlapping events are found
        """
        overlapping_schedule = [
            ScheduleEvent(
                asset_id=1,
                start=datetime.fromisoformat("2020-01-01 10:00:00"),
                end=datetime.fromisoformat("2020-01-01 10:30:00"),
            ),
            ScheduleEvent(
                asset_id=2,
                start=datetime.fromisoformat("2020-01-01 10:15:00"),
                end=datetime.fromisoformat("2020-01-01 11:00:00"),
            ),
        ]
        self.assertTrue(len(find_overlapping_events(overlapping_schedule)) == 1)
        self.assertTrue(find_overlapping_events(overlapping_schedule)[0].asset_id == 1)


unittest.main()
