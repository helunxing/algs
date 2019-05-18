#
# @lc app=leetcode.cn id=378 lang=python3
#
# [378] 有序矩阵中第K小的元素
#

import heapq


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        # 使用两个堆一个数组
        # 数组：等待访问的第一列
        # 小顶堆：当前待访问线
        # 大顶堆：已计算在K排名的元素
        fc_wait = [(matrix[i][0], i, 0) for i in range(len(matrix)-1, 0, -1)]
        inc = [(-matrix[0][0], 0, 0)]
        lin = []
        if len(matrix[0]) != 1:
            lin.append((matrix[0][1], 0, 1))
        heapq.heapify(lin)
        heapq.heapify(inc)
        while len(inc) < k:
            if fc_wait and (not lin or lin[0][0] > fc_wait[-1][0]):
                n, r, c = fc_wait.pop()
                if c+1 < len(matrix[r]):
                    heapq.heappush(lin, (matrix[r][c+1], r, c+1))
                new_inc = (-n, r, c)
            else:
                n, r, c = heapq.heappop(lin)
                if c+1 < len(matrix[r]):
                    heapq.heappush(lin, (matrix[r][c+1], r, c+1))
                new_inc = (-n, r, c)
            heapq.heappush(inc, new_inc)
        return -inc[0][0]
