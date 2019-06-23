class Solution:
    def carPooling(self, trips, capacity: int) -> bool:
        trips.sort(key=lambda x: x[1])

        FIN, REL = 0, 1

        waiting = []
        curr = -1

        for pas_num, sta, end in trips:
            curr = sta

            while waiting and waiting[-1][FIN] <= curr:
                capacity += waiting[-1][REL]
                waiting.pop()

            capacity -= pas_num
            if capacity < 0:
                return False
            waiting.append((end, pas_num))
            waiting.sort(reverse=True)

        return True
