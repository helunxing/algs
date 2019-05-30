# 元素可能相等
# 一些词交换后能得到字典序列小于


class Solution:
    def prevPermOpt1(self, A):
        n = len(A)

        rev = True
        for i in reversed(range(n-1)):
            if A[i+1] < A[i]:
                swa = i
                rev = False
                break
        if rev:
            return A

        l_s = n-1
        for i in reversed(range(swa, n)):
            if A[l_s] < A[i] < A[swa] or A[swa] <= A[l_s] and A[i] < A[swa]:
                l_s = i

        A[l_s], A[swa] = A[swa], A[l_s]

        return A


class Solution_too_complicate:
    def prevPermOpt1(self, A: List[int]) -> List[int]:
        n = len(A)
        larg, smal = 0, 0
        rev = True

        for i in range(1, n):
            if A[i-1] > A[i]:
                rev = False
            larg = i if A[i] > A[larg] else larg
            smal = i if A[i] < A[smal] else smal

        if rev:
            return A

        # 在某数后面找一个比它小的最大值
        for i in range(n-1):
            if A[i] == A[smal]:
                continue
            l_s = n-1
            for j in reversed(range(i, n)):
                if A[i] > A[j] and A[j] > A[l_s]:
                    l_s = j
                if A[i] == A[l_s] and A[j] < A[i]:
                    l_s = j
            if A[l_s] < A[i]:
                A[l_s], A[i] = A[i], A[l_s]
                return A

        return A
