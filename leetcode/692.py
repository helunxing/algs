# leetcode解，不知道怎么实现字典排序的。sort函数对元组值(x,y)比较时，x相等则根据y排序
import collections
import heapq

class Solution1(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]

class Solution2(object):
    def topKFrequent(self, words, k):
        count = collections.Counter(words)
        candidates = count.keys()
        candidates.sort(key = lambda w: (-count[w], w))
        return candidates[:k]

class Solution(object):
    def topKFrequent(self, words, k):
        """
        :type words: List[str]
        :type k: int
        :rtype: List[str]
        """
        count = collections.Counter(words)
        heap = [(-freq, word) for word, freq in count.items()]
        heapq.heapify(heap)
        return [heapq.heappop(heap)[1] for i in range(k)]

# 答案示例中有看起来不错的

# 自己写的
# class Solution2(object):
#     def topKFrequent(self, words, k):
#         """
#         :type words: List[str]
#         :type k: int
#         :rtype: List[str]
#         """

#         self.count = {}
#         for word in words:
#             if word in self.count:
#                 self.count[word] += 1
#             else:
#                 self.count[word] = 0

#         self.h_main = []
#         self.h_wait = []
#         k_counter = 0
#         for word in self.count:
#             if k_counter < k:  # 建立主堆
#                 heapq.heappush(self.h_main, [self.count[word], word, 0])
#                 k_counter += 1
#                 continue

#             if len(self.h_main) < k:
#                 # if len(self.h_wait) > 0 and self.count[word] > self.h_wait[0][0]:
#                 #     heapq.heappush(self.h_main, heapq.heappop(self.h_wait))
#                 # else:
#                     # heapq.heappush(self.h_main, [self.count[word], word])
#                 pass

#             else:
#                 if self.count[word] > self.h_main[0][0]:
#                     heapq.heappush(self.h_wait,
#                                    heapq.heappop(self.h_main)))

#                     if self.h_main[0][0] == self.h_wait[0][0]:
#                         heapq.heappush(self.h_wait,
#                                    heapq.heappop(self.h_main)))

#                     heapq.heappush(self.h_main, [self.count[word], word])
#                 elif self.count[word] == self.h_main[0][0]:
