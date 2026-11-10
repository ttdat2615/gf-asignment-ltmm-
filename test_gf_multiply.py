#define GF2N_NO_MAIN
#include "gf2n.c"
#include <stdlib.h>
 
int main(int argc, char **argv) {
    (void)is_irreducible; /* tranh canh bao ham khong dung */
    if (argc != 4) { fprintf(stderr, "Dung: %s <m> <poly-hex> <file.csv>\n", argv[0]); return 2; }
    int m = atoi(argv[1]);
    uint32_t p = (uint32_t)strtoul(argv[2], NULL, 16);
    FILE *f = fopen(argv[3], "r");
    if (!f) { perror(argv[3]); return 2; }
 
    char line[128];
    int total = 0, failed = 0;
    while (fgets(line, sizeof line, f)) {
        if (line[0] == '#' || line[0] == '\n') continue;
        unsigned a, b, e;
        if (sscanf(line, "%x,%x,%x", &a, &b, &e) != 3) { printf("Dong loi dinh dang: %s", line); failed++; continue; }
        uint32_t got = gf_mul(a, b, m, p);
        total++;
        if (got != e) { failed++; printf("FAIL: 0x%X * 0x%X = 0x%X, mong doi 0x%X\n", a, b, got, e); }
    }
    fclose(f);
    printf("%s: %d/%d test case dat\n", argv[3], total - failed, total);
    return failed != 0;
}
 