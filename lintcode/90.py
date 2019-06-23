class Solution:
    """
    @param: A: an integer array
    @param: k: a postive integer <= length(A)
    @param: targer: an integer
    @return: A list of lists of integer
    """

    def kSumII(self, A, k, target):
        # write your code here
        A.sort()
        self.res = []
        n = len(A)

        def findnext(sta, k, target, tmp):
            if k > n-sta:
                return
            if k == 2:
                findtwo(sta, target, tmp)
            else:
                i = sta
                while i < n:
                    if i != sta and A[i-1] == A[i]:
                        i += 1
                        continue
                    findnext(i+1, k-1, target-A[i], tmp+[A[i]])
                    i += 1

        def findtwo(sta, target, tmpl):
            i = sta
            end = n-1
            while i < end:
                s = A[i]+A[end]
                if s < target:
                    i += 1
                elif s > target:
                    end -= 1
                else:
                    self.res.append(tmpl+[A[i], A[end]])
                    while A[i] == A[i+1]:
                        i += 1
                    i += 1
                    while A[end] == A[end-1]:
                        end -= 1
                    end -= 1
        if k == 1:
            return [[target]] if target in A else []
        findnext(0, k, target, [])
        return self.res
