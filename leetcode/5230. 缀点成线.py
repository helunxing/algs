class Solution:
    def checkStraightLine(self, coordinates) -> bool:
        def gcd(a, b):
            a, b = (a, b) if a >= b else (b, a)
            while b:
                a, b = b, a % b
            return a

        def rab(ca, cb):
            a = (ca[0]-cb[0])
            b = (ca[1]-cb[1])
            if abs(a) < abs(b):
                a, b = b, a
            c = gcd(a, b)
            a //= c
            b //= c
            if a < 0:
                a *= -1
                b *= -1
            return a, b

        aa, bb = rab(coordinates[0], coordinates[-1])
        for i in range(1, len(coordinates)):
            a, b = rab(coordinates[0], coordinates[i])
            if a < 0:
                a *= -1
                b *= -1
            if a != aa or b != bb:
                return False

        return True
