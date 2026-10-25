import sys
import os

# Thêm đường dẫn để import module từ thư mục src
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '../src')))
from gf_multiply import FiniteFieldGF

def run_tests():
    print("========================================")
    print(" KIỂM THỬ PHÉP NHÂN TRONG TRƯỜNG HỮU HẠN")
    print("========================================")
    
    # 1. Kiểm thử GF(2^4) với đa thức tối giản x^4 + x + 1 (0x13)
    gf4 = FiniteFieldGF(degree=4, irreducible_poly=0x13)
    a4, b4 = 0xD, 0x2
    res4 = gf4.multiply(a4, b4)
    print(f"[GF(2^4)] {hex(a4)} * {hex(b4)} = {hex(res4)}")

    # 2. Kiểm thử GF(2^8) với đa thức tối giản chuẩn AES x^8 + x^4 + x^3 + x + 1 (0x11B)
    gf8 = FiniteFieldGF(degree=8, irreducible_poly=0x11B)
    a8, b8 = 0x57, 0x83
    res8 = gf8.multiply(a8, b8)
    print(f"[GF(2^8)] {hex(a8)} * {hex(b8)} = {hex(res8)} (Kỳ vọng: 0xc1)")
    print("========================================")

if __name__ == "__main__":
    run_tests()