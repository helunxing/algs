class Solution:
    """
    @param source: 
    @param target: 
    @return: return the index
    """

    def strStr(self, source, target):
        # Write your code here
        m, n = len(source), len(target)
        if not n:
            return 0
        if not m:
            return -1
        for i in range(m-n+1):
            for j in range(n):
                if source[i+j] == target[j]:
                    if j == n-1:
                        return i
                    continue
                else:
                    break

        return -1
