# Finite Field Multiplication in GF(2^4) and GF(2^8)

## 1. Giới thiệu

Dự án cài đặt thuật toán nhân hai phần tử trong trường hữu hạn GF(2^4) và GF(2^8), sử dụng thuật toán Shift-and-Add và phép rút gọn theo đa thức bất khả quy.

## 2. Đa thức bất khả quy

- **GF(2^4):** \(x^4 + x + 1\), biểu diễn `0x13`.
- **GF(2^8):** \(x^8 + x^4 + x^3 + x + 1\), biểu diễn `0x11B`.

## 3. Cấu trúc dự án

```text
gf-assignment-ltmm-/
├── gf_multiply.py
├── test_gf_multiply.py
└── README.md
```

