import calendar


class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        s = ["Monday", "Tuesday", "Wednesday",
             "Thursday", "Friday", "Saturday", "Sunday"]
        return s[calendar.weekday(year, month, day)]
