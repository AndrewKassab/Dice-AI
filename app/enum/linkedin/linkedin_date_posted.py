from enum import Enum


class LinkedinDatePosted(Enum):

    # Values are indices of the filter input
    ANY_TIME = 0
    PAST_MONTH = 1
    PAST_WEEK = 2
    PAST_24_HOURS = 3
