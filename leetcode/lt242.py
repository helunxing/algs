class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        if len(s) != len(t):
            return False
        s_dic = {}
        t_dic = {}
        for i in range(len(s)):
            s_dic[s[i]] = s_dic.get(s[i], -1)+1
            t_dic[t[i]] = t_dic.get(t[i], -1)+1
        for key in s_dic:
            if s_dic[key] != t_dic.get(key, 0):
                return False
        return True
