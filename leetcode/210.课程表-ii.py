#
# @lc app=leetcode.cn id=210 lang=python3
#
# [210] 课程表 II
#


import collections


class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        back = collections.defaultdict(set)
        frow = collections.defaultdict(set)
        for crs, pre in prerequisites:
            frow[pre].add(crs)
            back[crs].add(pre)
        q = collections.deque([i for i in range(numCourses) if not back[i]])
        res = []

        while q:
            curr = q.popleft()
            res.append(curr)
            for n in frow[curr]:
                back[n].remove(curr)
                if not back[n]:
                    q.append(n)

        return res if len(res) == numCourses else []
