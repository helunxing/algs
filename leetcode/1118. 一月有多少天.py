class Solution:
    def numberOfDays(self, Y: int, M: int) -> int:
        big = [1, 3, 5, 7, 8, 10, 12]
        sml = [4, 6, 9, 11]
        if M in big:
            return 31
        elif M in sml:
            return 30
        else:
            return 29 if (Y % 4 == 0 and Y % 100 != 0) or Y % 400 == 0 else 28
