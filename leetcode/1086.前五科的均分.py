class Solution:
    def highFive(self, items: List[List[int]]) -> List[List[int]]:
        dic = {}
        ids = []
        res = []
        for id, fen in items:
            if id not in dic:
                dic[id] = []
                ids.append(id)
            if len(dic[id]) < 5:
                dic[id].append(fen)
            else:
                rep = min(dic[id])
                if fen < rep:
                    continue
                for i in range(len(dic[id])):
                    if dic[id][i] == rep:
                        dic[id][i] = fen
                        break
        ids.sort()
        for id in ids:
            res.append([id, sum(dic[id])//5])
        return res
