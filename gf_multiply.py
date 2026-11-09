

 * Nhan hai da thuc trong truong huu han GF(2^m), m = 4 va m = 8.
 * Da thuc duoc bieu dien bang so nguyen: bit i la he so cua x^i. Phep cong = XOR.
 *   GF(2^4): p(x) = x^4 + x + 1             -> 0x13
 *   GF(2^8): p(x) = x^8 + x^4 + x^3 + x + 1 -> 0x11B (da thuc cua AES)
 */
#include <stdio.h>
#include <stdint.h>
#include <string.h>
 
#define POLY_GF16  0x13u
#define POLY_GF256 0x11Bu
 
/* Bac cua da thuc (-1 neu a = 0). */
static int degree(uint32_t a) {
    int d = -1;
    while (a) { d++; a >>= 1; }
    return d;
}
 
/* Phan du cua a chia cho p tren GF(2). */
static uint32_t poly_mod(uint32_t a, uint32_t p) {
    int dp = degree(p);
    while (degree(a) >= dp)
        a ^= p << (degree(a) - dp);
    return a;
}
 
/* Nhan hai da thuc tren GF(2) (carry-less), chua rut gon. */
static uint32_t poly_mul(uint32_t a, uint32_t b) {
    uint32_t r = 0;
    while (b) {
        if (b & 1) r ^= a;
        a <<= 1;
        b >>= 1;
    }
    return r;
}
 
/* Kiem tra p co toi gian tren GF(2) khong (thu chia cho moi da thuc bac <= deg/2). */
static int is_irreducible(uint32_t p) {
    int deg = degree(p);
    if (deg < 1) return 0;
    for (uint32_t d = 2; degree(d) <= deg / 2; d++)
        if (poly_mod(p, d) == 0) return 0;
    return 1;
}
 
/* Nhan shift-and-add trong GF(2^m), rut gon ngay trong vong lap. */
uint32_t gf_mul(uint32_t a, uint32_t b, int m, uint32_t p) {
    uint32_t r = 0;
    for (int i = 0; i < m; i++) {
        if (b & 1) r ^= a;
        b >>= 1;
        a <<= 1;
        if (a & (1u << m)) a ^= p;
    }
    return r;
}
 
/* Nhan day du roi chia lay du (de doi chieu). */
uint32_t gf_mul_naive(uint32_t a, uint32_t b, uint32_t p) {
    return poly_mod(poly_mul(a, b), p);
}
 
/* In da thuc dang "x^3 + x + 1". */
void print_poly(uint32_t a) {
    if (a == 0) { printf("0"); return; }
    int first = 1;
    for (int i = degree(a); i >= 0; i--) {
        if (!((a >> i) & 1)) continue;
        if (!first) printf(" + ");
        if (i == 0) printf("1");
        else if (i == 1) printf("x");
        else printf("x^%d", i);
        first = 0;
    }
}