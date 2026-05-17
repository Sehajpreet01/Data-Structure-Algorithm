# =============================================================================
# TOPIC: SLIDING WINDOW
# =============================================================================
#
# WHAT IS SLIDING WINDOW?
# Sliding window is a technique where you maintain a "window" (a subarray or
# substring) and slide it across the input to compute results efficiently.
# Instead of recalculating from scratch each time, you ADD the new element
# entering the window and REMOVE the element leaving it.
#
# TYPES OF SLIDING WINDOW:
# 1. Fixed Size Window:
#    - Window size k is given
#    - Slide one step at a time: add arr[right], remove arr[right - k]
#    - Used for: max sum of k elements, average of subarrays
#
# 2. Variable Size Window:
#    - Window expands/shrinks based on a condition
#    - Use left and right pointers; expand right, shrink left when invalid
#    - Used for: longest substring with unique chars, smallest subarray with sum >= target
#
# HOW TO THINK ABOUT SLIDING WINDOW PROBLEMS:
# 1. Does the problem involve a contiguous subarray or substring?
# 2. Is there a fixed size k, or do I need to find the optimal size?
# 3. What's my "window state"? (a sum, a frequency map, a count)
# 4. When is the window invalid? That's when to shrink from the left.
# 5. What am I maximizing or minimizing? (length, sum, count)
#
# TIME COMPLEXITY:
# O(n) — each element enters and exits the window at most once.
# Much better than O(n^2) brute force nested loops.
#
# COMMON PATTERNS IN INTERVIEWS:
# - Maximum/minimum sum of subarray of size k
# - Longest substring without repeating characters
# - Smallest subarray with sum >= target
# - Count of anagram occurrences in a string
# - Longest substring with at most k distinct characters
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Find the maximum sum of a subarray of size k
# Input:  arr = [2, 1, 5, 1, 3, 2], k = 3
# Output: 9  (subarray [5, 1, 3])

def max_sum_subarray(arr, k):
    window_sum = sum(arr[:k])   # sum of first window
    max_sum = window_sum

    for i in range(k, len(arr)):
        window_sum += arr[i] - arr[i - k]   # slide: add new, remove old
        max_sum = max(max_sum, window_sum)

    return max_sum

print("Q1 - Max Sum Subarray of size 3:", max_sum_subarray([2, 1, 5, 1, 3, 2], 3))


# Q2: Find the length of the longest substring without repeating characters
# Input:  "abcabcbb"
# Output: 3  ("abc")

def longest_unique_substring(s):
    seen = set()
    left = 0
    max_len = 0

    for right in range(len(s)):
        while s[right] in seen:     # shrink window until no duplicate
            seen.remove(s[left])
            left += 1
        seen.add(s[right])
        max_len = max(max_len, right - left + 1)

    return max_len

print("Q2 - Longest Unique Substring in 'abcabcbb':", longest_unique_substring("abcabcbb"))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Find the average of every subarray of size k
# Input:  arr = [1, 3, 2, 6, -1, 4, 1, 8, 2], k = 5
# Output: [2.2, 2.8, 2.4, 3.6, 2.8]

# Q4: Find the smallest subarray with sum >= target
# Input:  arr = [2, 1, 5, 2, 3, 2], target = 7
# Output: 2  (subarray [5, 2] has length 2)

# Q5: Find the number of times an anagram of pattern p appears in string s
# Input:  s = "cbaebabacd", p = "abc"
# Output: 2  (at index 0 "cba" and index 6 "bac")

# Q6: Longest substring with at most k distinct characters
# Input:  s = "eceba", k = 2
# Output: 3  ("ece")

# Q7: Maximum number of 1s in a subarray after flipping at most k zeros
# Input:  arr = [1, 1, 0, 0, 1, 1, 1, 0, 1, 1], k = 2
# Output: 9

# Q8: Find all starting indices of substrings that are anagrams of pattern
# Input:  s = "abaacbabc", p = "abc"
# Output: [3, 4, 6]

# Q9: Minimum window substring — smallest substring of s containing all chars of t
# Input:  s = "ADOBECODEBANC", t = "ABC"
# Output: "BANC"

# Q10: Find the longest subarray with sum equal to k
# Input:  arr = [1, -1, 5, -2, 3], k = 3
# Output: 4  (subarray [1, -1, 5, -2])
