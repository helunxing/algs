class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        l = len(gas)
        sta = 0
        while sta < l:
            sG, sC = 0, 0
            cnt = 0
            while cnt < l:
                curr = (sta+cnt) % l
                sG += gas[curr]
                sC += cost[curr]
                if sG < sC:
                    break
                # 没比较通过就不能加一
                cnt += 1
            if cnt == l:
                return sta
            sta += cnt + 1
        return -1
