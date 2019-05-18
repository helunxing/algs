#
# @lc app=leetcode.cn id=218 lang=python3
#
# [218] 天际线问题
#

import collections
import bisect
import heapq


# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = sorted([(L, -H, R) for L, R, H in buildings] +
                        list({(R, 0, None) for _, R, _ in buildings}))
        res, hp = [[0, 0]], [(0, float("inf"))]
        for x, negH, R in events:
            while x >= hp[0][1]:
                heapq.heappop(hp)
            if negH:
                heapq.heappush(hp, (negH, R))
            if res[-1][1]+hp[0][0]:
                res.append([x, -hp[0][0]])
        return res[1:]


class Solution_give_up:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        # 10:59

        # 等待遍历的高度列表
        h_nums = [0]

        # 每个高度对应的左右上角
        h_dict = collections.defaultdict(list)
        # h_set = collections.defaultdict(set)

        # 已占用的x坐标范围
        covered_range = []
        top_occed = set()
        btn_occed = set()

        # 图形凸角列表
        cons = []

        # 构造高度列表
        for b in buildings:
            if b[2] not in h_dict:
                h_nums.append(b[2])
            h_dict[b[2]].append((b[0], b[1]))
            # h_set[b[2]].add(b[0])
            # h_set[b[2]].add(b[1])

        # 从上到下依次计算
        h_nums.sort(reverse=True)
        for i in h_nums:
            h_dict[i].sort()

        # 根据已占用坐标构建角坐标
        def cre_cor(occed, height):
            for x in covered_range:
                for i in range(2):
                    if x[i] not in occed:
                        cons.append([x[i], height])
                        occed.add(x[i])

        # 合并原有区间和新区间
        def merge(covered, now):
            nl = []

            def findtmp(covered, now):
                if covered and now:
                    return list(now[0]) if now[0][0] < covered[0][0] else list(covered[0])
                if covered:
                    return list(covered[0])
                if now:
                    return list(now[0])
                return []
            i, j = 0, 0
            tmp = findtmp(covered[i:], now[j:])
            while i != len(covered) and j != len(now):
                if i < len(covered) and covered[i][0] < tmp[1]:
                    tmp[1] = max(covered[i][1], tmp[1])
                    i += 1
                if j < len(now) and now[j][0] < tmp[1]:
                    tmp[1] = max(now[j][1], tmp[1])
                    j += 1
                if tmp[1] < covered[i][0] and tmp[1] < now[j][0]:
                    nl.append(tmp[:])
                    tmp = findtmp(covered[i:], now[j:])

            return nl
            # TODO
            # 仅剩此功能未完成时1：00

        # 遍历待处理的高度
        for height in h_nums:

            i = 1
            l = h_dict[height]
            nl = [l[0]]

            # 按值合并待处理的屋顶
            while i < len(l):
                if l[i][0] <= nl[-1][1]:
                    nl[-1][1] = max(l[i][1], nl[-1][1])
                else:
                    nl.append(list(l[i]))
                i += 1
            h_dict[height] = nl

            # 根据已占用坐标构建底部角坐标
            cre_cor(top_occed, height)

            # 现有屋顶 和 已经占用的坐标范围 合并
            if not covered_range:
                covered_range = h_dict[height][:]
            else:
                covered_range = merge(covered_range, h_dict[height])

            # 根据已占用坐标构建顶部角坐标
            cre_cor(btn_occed, height)

        cons.sort()

        # 构建答案
        return [cons for i in range(1, len(cons), 2)]


class Solution_time_out:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        ans = []
        if not buildings:
            return ans
        lines = []
        l, r, hei = 0, 1, 2
        for b in buildings:
            lines.append([b[l], -b[hei]])
            lines.append([b[r], b[hei]])
        lines.sort()

        h = [0]
        m = 0
        for lin in lines:
            if lin[1] < 0:
                bisect.insort(h, -lin[1])
                # h.append(-lin[1])
            else:
                for i in range(len(h)-1, 0, -1):
                    if h[i] == lin[1]:
                        del h[i]
                        break
            h.sort()
            if m != h[-1]:
                ans.append([lin[0], h[-1]])
            m = h[-1]
        return ans
