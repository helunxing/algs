# 46
class Solution:
    def reconstructQueue(self, people):
        def mycmp(k):
            return (-k[0], k[1])
        people.sort(key=mycmp)
        ans = []
        for pir in people:
            # if pir[1] == len(ans):
            #     ans.append(pir)
            #     continue
            ans = ans[:pir[1]]+[pir]+ans[pir[1]:]

        return ans


people = [[7, 0], [4, 4], [7, 1], [5, 0], [6, 1], [5, 2]]

s = Solution()
print(s.reconstructQueue(people))
print(s.reconstructQueue([]))

# 1.10