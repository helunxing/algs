import collections


class Solution:
    def indexPairs(self, text: str, words: List[str]) -> List[List[int]]:
        d = collections.defaultdict(list)
        res = []
        for i, x in enumerate(text):
            d[x].append(i)
        for word in words:
            sta, end = word[0], word[-1]
            for i in d[sta]:
                for j in d[end]:
                    if j-i+1 == len(word) and text[i:j+1] == word:
                        res.append([i, j])
        return sorted(res)
