from enum import Enum


class PostedDate(Enum):
    ANY_DATE = "Any Date"
    TODAY = "Today"
    LAST_3_DAYS = "Last 3 Days"
    LAST_7_DAYS = "Last 7 Days"