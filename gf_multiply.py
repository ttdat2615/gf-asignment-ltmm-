class FiniteFieldGF:
    def __init__(self, degree, irreducible_poly):
        """
        Khởi tạo trường GF(2^degree) với đa thức tối giản.
        - GF(2^4): degree=4, irreducible_poly=0x13 (x^4 + x + 1)
        - GF(2^8): degree=8, irreducible_poly=0x11B (x^8 + x^4 + x^3 + x + 1)
        """
        self.degree = degree
        self.poly = irreducible_poly
        self.mask = 1 << degree

    def multiply(self, a: int, b: int) -> int:
        """
        Thuật toán nhân hai đa thức trong trường hữu hạn (Shift-and-Add).
        """
        result = 0
        while b > 0:
            if b & 1:
                result ^= a
            b >>= 1
            
            carry = a & self.mask
            a <<= 1
            if carry:
                a ^= self.poly
                
        return result