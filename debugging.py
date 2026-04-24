# ─────────────────────────────────────────
# Task 4 – Debugging & Refactoring
# ─────────────────────────────────────────

# --- Buggy version (do not change — identify the bug(s) and explain them) ---
def fib_buggy(n: int) -> int:
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib_buggy(n - 1) + fib_buggy(n - 2)  # Bug(s) somewhere in this function


# --- Your fixed, iterative version ---
def fib_iterative(n: int) -> int:
    """Return the nth Fibonacci number using iteration."""
    # 1. Handle base cases
    # 2. Build up the result iteratively
    pass


# --- Your memoized recursive version ---
def fib_memoized(n: int) -> int:
    """Return the nth Fibonacci number using memoized recursion."""
    # Hint: use functools.lru_cache or a cache dict
    pass
