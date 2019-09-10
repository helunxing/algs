import collections


class Solution:
    def beforeAndAfterPuzzles(self, phrases: List[str]) -> List[str]:
        sta_d = collections.defaultdict(list)
        res = set()
        for i, p in enumerate(phrases):
            words = p.split()
            sta_d[words[0]].append(i)

        for i, p in enumerate(phrases):
            words = p.split()
            end_w = words[-1]
            for j in sta_d[end_w]:
                if i == j:
                    continue
                if len(p) != len(end_w):
                    new_w = p[:len(p)-len(end_w)]+phrases[j]
                else:
                    new_w = phrases[j]
                res.add(new_w)
        return sorted(list(res))


["a chip off the old block party",
 "a man on a mission impossible",
 "a man on a mission statement",
 "a quick bite to eat my words",
 "chocolate bar of soap"]

["a chip off the old block party",
 "a man on a mission impossible",
 "a man on a mission statement",
 "a quick bite to eat my words",
 "chocolate bar of soap"]
