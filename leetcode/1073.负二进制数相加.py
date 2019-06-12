import math


class Solution:
    def addNegabinary(self, arr1, arr2):
        i, j = len(arr1)-1, len(arr2)-1
        arrb = []
        carry = 0
        pos = -2

        while i >= 0 or j >= 0 or carry:
            if i >= 0:
                carry += arr1[i]
            if j >= 0:
                carry += arr2[j]
            mod = carry % pos
            carry //= pos

            if mod < 0:
                mod -= pos
                carry += 1

            arrb.append(mod)

            i -= 1
            j -= 1

        while len(arrb) > 1:
            if arrb[-1]:
                break
            else:
                arrb.pop()

        return list(reversed(arrb))
