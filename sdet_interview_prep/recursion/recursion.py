# =============================================================================
# TOPIC: RECURSION
# =============================================================================
#
# WHAT IS RECURSION?
# Recursion is when a function calls itself to solve a smaller version of the
# same problem. Every recursive solution has:
# 1. BASE CASE   — the condition to STOP recursion (prevents infinite loop)
# 2. RECURSIVE CASE — where the function calls itself with smaller input
#
# HOW TO THINK ABOUT RECURSION:
# Step 1: What is the simplest/smallest version of this problem? (base case)
# Step 2: How can I reduce the problem to a smaller version of itself?
# Step 3: Trust that the recursive call works — focus on the current step only
#
# RECURSION vs ITERATION:
# - Recursion is elegant but uses call stack memory -> risk of stack overflow
# - Iteration is usually faster and uses O(1) extra space
# - Any recursion can be converted to iteration using an explicit stack
#
# TIME AND SPACE:
# - Time depends on how many recursive calls are made
# - Space: O(depth of recursion) — each call adds a frame to the call stack
# - Fibonacci naive recursion: O(2^n) time — exponential! (use memoization)
#
# COMMON RECURSION PATTERNS:
# - Divide and Conquer: split into halves (merge sort, binary search)
# - Tree traversal: process node, recurse left and right
# - Backtracking: try all options, undo bad ones
# - Accumulator: pass running result into recursive call
#
# TAIL RECURSION TIP:
# If your last action is the recursive call, it's tail recursion.
# Python doesn't optimize tail recursion, but it's still a clean pattern.
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Calculate factorial of n using recursion
# Input:  5
# Output: 120  (5 * 4 * 3 * 2 * 1)

def factorial(n):
    if n == 0 or n == 1:    # base case
        return 1
    return n * factorial(n - 1)  # recursive case

print("Q1 - Factorial of 5:", factorial(5))


# Q2: Find the nth Fibonacci number
# Fibonacci: 0, 1, 1, 2, 3, 5, 8, 13, 21 ...
# fib(0) = 0, fib(1) = 1, fib(n) = fib(n-1) + fib(n-2)

def fibonacci(n, memo={}):
    if n <= 1:              # base case
        return n
    if n in memo:           # use cached result (memoization)
        return memo[n]
    memo[n] = fibonacci(n - 1, memo) + fibonacci(n - 2, memo)
    return memo[n]

print("Q2 - Fibonacci(10):", fibonacci(10))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Sum of all digits of a number using recursion
# Input:  1234
# Output: 10  (1 + 2 + 3 + 4)

# Q4: Calculate x raised to the power n recursively
# Input:  x = 2, n = 10
# Output: 1024

# Q5: Reverse a string using recursion
# Input:  "hello"
# Output: "olleh"

# Q6: Check if a string is a palindrome using recursion
# Input:  "racecar"
# Output: True

# Q7: Find the GCD (Greatest Common Divisor) of two numbers using Euclid's algorithm
# Input:  48, 18
# Output: 6
# Hint: gcd(a, b) = gcd(b, a % b), base case: gcd(a, 0) = a

# Q8: Generate all subsets of a list (Power Set)
# Input:  [1, 2, 3]
# Output: [[], [1], [2], [3], [1,2], [1,3], [2,3], [1,2,3]]

# Q9: Count the number of ways to climb n stairs (1 or 2 steps at a time)
# Input:  n = 4
# Output: 5  (1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2)

# Q10: Flatten a nested list using recursion
# Input:  [1, [2, [3, 4], 5], [6, 7]]
# Output: [1, 2, 3, 4, 5, 6, 7]
