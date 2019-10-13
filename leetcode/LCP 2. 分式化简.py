class Solution:
    def fraction(self, cont):
        mu = cont.pop()
        if not cont:
            return [mu, 1]
        zi = cont.pop()*mu+1
        while cont:
            zi, mu = mu, zi
            zi += cont.pop()*mu

        def gcd(a, b):
            a, b = (a, b) if a >= b else (b, a)
            while b:
                a, b = b, a % b
            return a
        g = gcd(mu, zi)
        res = [zi//g, mu//g]
        return res
