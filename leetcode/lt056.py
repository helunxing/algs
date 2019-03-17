# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e


class Solution:
    def merge(self, intervals: List[Interval]) -> List[Interval]:
        # 34
        if not intervals:
            return intervals

        intervals.sort(key=lambda i: i.start)

        tmp = []
        i = 1
        tmps, tmpe = intervals[0].start, intervals[0].end
        while i < len(intervals):
            if intervals[i].start == tmps:
                tmpe = max(tmpe, intervals[i].end)
            else:
                tmp.append(Interval(tmps, tmpe))
                tmps, tmpe = intervals[i].start, intervals[i].end
            i += 1
        tmp.append(Interval(tmps, tmpe))

        ans = []
        i = 1
        tmps, tmpe = tmp[0].start, tmp[0].end
        while i < len(tmp):
            if tmp[i].start <= tmpe:
                tmpe = max(tmpe, tmp[i].end)
            else:
                ans.append(Interval(tmps, tmpe))
                tmps, tmpe = tmp[i].start, tmp[i].end
            i += 1
        ans.append(Interval(tmps, tmpe))

        return ans
        # 10
