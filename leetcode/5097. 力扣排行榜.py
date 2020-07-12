class Leaderboard:
    def __init__(self):
        self.arr = []
        self.d = {}

    def addScore(self, playerId: int, score: int) -> None:
        if playerId not in self.d:
            self.d[playerId] = [score, playerId]
            self.arr.append(self.d[playerId])
        else:
            self.d[playerId][0] += score
        self.arr.sort(reverse=True)

    def top(self, K: int) -> int:
        s = 0
        for i in range(0, min(len(self.arr), K)):
            s += self.arr[i][0]
        return s

    def reset(self, playerId: int) -> None:
        self.d[playerId][0] = 0
        self.arr.sort(reverse=True)


# Your Leaderboard object will be instantiated and called as such:
# obj = Leaderboard()
# obj.addScore(playerId,score)
# param_2 = obj.top(K)
# obj.reset(playerId)
