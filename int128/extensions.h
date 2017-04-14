// I need this module to extend native C (Cython) types
// and perform transformation with 64 and 128 bits integers.
// From my perspective, it's the only way I can do it.

typedef __uint128_t int128;
typedef __uint64_t int64;
