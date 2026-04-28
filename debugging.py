# ─────────────────────────────────────────
# Task 4 – Debugging & Refactoring
# ─────────────────────────────────────────
from functools import lru_cache


def fib_buggy(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_buggy(n - 1) + fib_buggy(n - 2)


def fib_iterative(n: int) -> int:
    if n == 0: return 0
    if n == 1: return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b


@lru_cache(maxsize=None)
def fib_memoized(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_memoized(n - 1) + fib_memoized(n - 2)
