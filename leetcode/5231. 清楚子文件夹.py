class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        def j(a, b):
            return b.startsWith(a+'/')
        folder.sort()
        res = []

        for path in folder:
            if not res or not j(res[-1], path):
                res.append(path)
        return res
