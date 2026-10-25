
class FiniteFieldGF:
    def __init__(self, degree, irreducible_poly):
        self.degree = degree
        self.poly = irreducible_poly
        self.mask = 1 << degree

    def multiply(self, a: int, b: int) -> int:
        result = 0

        while b > 0:
            if b & 1:
                result ^= a

            b >>= 1
            a <<= 1

            if a & self.mask:
                a ^= self.poly

        return result & (self.mask - 1)
