class Solution:
    def validUtf8(self, data) -> bool:
        i = 0
        while i < len(data):
            if not data[i] & int('80', 16):
                i += 1
                continue

            if not data[i] & int('e0', 16) ^ int('c0', 16):
                front = 1
            elif not data[i] & int('f0', 16) ^ int('e0', 16):
                front = 2
            elif not data[i] & int('f8', 16) ^ int('f0', 16):
                front = 3
            else:
                return False
            j = i+1
            if i+front >= len(data):
                return False

            while j <= i+front:
                if not data[j] & int('c0', 16) ^ int('80', 16):
                    j += 1
                else:
                    return False
            i = j

        return True


class Solution_best:
    def validUtf8(self, data) -> bool:
        ctn = 0
        for i in data:
            if ctn:
                if i >> 6 != 0b10:
                    return False
                ctn -= 1
                continue

            if i >> 5 == 0b110:
                ctn = 1
            elif i >> 4 == 0b1110:
                ctn = 2
            elif i >> 3 == 0b11110:
                ctn = 3
            elif i >> 7:
                return False
        return ctn == 0
