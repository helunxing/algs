import calendar


class Solution:
    def ordinalOfDate(self, date: str) -> int:
        d = date.split('-')
        res = 0
        for mou in range(1, int(d[1])):
            res += calendar.monthrange(int(d[0]), mou)[1]
        return res+int(d[2])
