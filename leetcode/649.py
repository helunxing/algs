from typing import Collection, Deque


import collections


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        qd = collections.deque([i for i, s in enumerate(senate) if s == 'D'])
        qr = collections.deque([i for i, s in enumerate(senate) if s == 'R'])

        while qd and qr:
            if qd[0] < qr[0]:
                qr.popleft()
                qd.append(qd.popleft()+len(senate))
            else:
                qd.popleft()
                qr.append(qr.popleft()+len(senate))
        return "Radiant" if qr else "Dire"
