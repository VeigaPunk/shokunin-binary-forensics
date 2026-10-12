#include <stdint.h>
#include <stdio.h>
#include <string.h>

static uint32_t rolling_checksum(const unsigned char *bytes, size_t len) {
    uint32_t state = 0x13579bdfu;
    for (size_t i = 0; i < len; ++i) {
        state = (state << 5) | (state >> 27);
        state ^= (uint32_t)(bytes[i] + 17u);
    }
    return state;
}

static void rotate_ascii(char *out, const char *in) {
    size_t i = 0;
    for (; in[i] && i < 127; ++i) {
        unsigned char c = (unsigned char)in[i];
        out[i] = (c >= 'a' && c <= 'z') ? (char)('a' + (c - 'a' + 13) % 26) : (char)c;
    }
    out[i] = 0;
}

int main(int argc, char **argv) {
    const char *input = argc > 1 ? argv[1] : "amber";
    char transformed[128];
    rotate_ascii(transformed, input);
    printf("r1:%s:%08x\n", transformed,
           rolling_checksum((const unsigned char *)transformed, strlen(transformed)));
    return 0;
}
