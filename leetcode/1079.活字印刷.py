class Solution:
    def numTilePossibilities(self, tiles: str) -> int:
        stamps = [ch for ch in tiles]
        self.seq = set()

        def dfs(word, stamps, l):
            # if not stamps:
            if l == len(word):
                self.seq.add(word)
                return
            for i, ch in enumerate(stamps):
                dfs(word+ch, stamps[:i]+stamps[i+1:], l)
        for l in range(1, len(stamps)+1):
            dfs('', stamps, l)
        return len(self.seq)
