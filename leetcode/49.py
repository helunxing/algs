import collections

# class Solution(object):
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             count = [0]*26
#             for l in s:
#                 count[ord(l)-ord('a')] += 1
#             ans[tuple(count)].append(s)
#         return ans.values()


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        mp = collections.defaultdict(list)
        for s in strs:
            k=''.join(sorted(s))
            mp[k].append(s)
        return list(mp.values())




# 以上官方答案
# 以下自己写的
# class Solution(object):
#     def groupAnagrams(self, strs):
#         """
#         :type strs: List[str]
#         :rtype: List[List[str]]
#         """
#         # 24分
#         strs_no_rep = list(set(strs))
#         ltter_dics = [[0 for i in range(26)] for i in range(len(strs_no_rep))]
#         dic_of_ldic = {}

#         for i in range(len(strs_no_rep)):
#             ltter_dic = ltter_dics[i]
#             for ltter in strs_no_rep[i]:
#                 ltter_dic[ord(ltter)-ord('a')] += 1

#             if ltter_dic in dic_of_ldic:
#                 dic_of_ldic[ltter_dic].append(strs_no_rep[i])
#             else:
#                 dic_of_ldic[ltter_dic] = [strs_no_rep[i]]

#         T_ans = []
#         for key in dic_of_ldic.keys():
#             T_ans.extend(dic_of_ldic[key])

#         return T_ans
#         # 44分
