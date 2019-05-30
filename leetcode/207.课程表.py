#
# @lc app=leetcode.cn id=207 lang=python3
#
# [207] 课程表
#


import collections


class Solution:
    def canFinish(self, numCourses: int, prerequisites) -> bool:
        frow = collections.defaultdict(set)
        back = collections.defaultdict(set)
        for a, b in prerequisites:
            frow[a].add(b)
            back[b].add(a)
        q = collections.deque([i for i in range(numCourses) if not back[i]])
        while q:
            curr = q.popleft()
            for next in frow[curr]:
                back[next].remove(curr)
                if not len(back[next]):
                    q.append(next)
            frow[curr] = set()
        for i in range(numCourses):
            if back[i]:
                return False
        return True
