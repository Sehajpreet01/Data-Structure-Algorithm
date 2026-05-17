# =============================================================================
# TOPIC: TWO POINTERS
# =============================================================================
#
# WHAT IS THE TWO POINTERS TECHNIQUE?
# Two pointers is a pattern where you use two index variables that move
# through the array to solve a problem more efficiently than nested loops.
#
# TYPES OF TWO POINTER SETUPS:
# 1. Left & Right (opposite ends):
#    - Start left=0, right=len-1 and move toward center
#    - Used for: palindrome check, pair sum, reversing
#
# 2. Slow & Fast (same direction):
#    - Both start at 0, fast moves ahead
#    - Used for: removing duplicates, cycle detection
#
# 3. Two arrays, one pointer each:
#    - One pointer per array, advance based on comparison
#    - Used for: merging sorted arrays, intersection
#
# HOW TO THINK ABOUT TWO POINTER PROBLEMS:
# 1. Is the array sorted? (many two-pointer problems require sorted input)
# 2. Am I looking for a pair, triplet, or subarray?
# 3. Should I move left, right, or both pointers based on a condition?
# 4. What's my stopping condition? (left < right, or i < j, etc.)
#
# TIME COMPLEXITY:
# Most two pointer solutions are O(n) — single pass through the array.
# This replaces the brute force O(n^2) nested loop.
#
# COMMON PATTERNS IN INTERVIEWS:
# - Find pair with given sum in sorted array
# - Remove duplicates in-place
# - Move zeros / move negatives
# - Reverse a string or array
# - Check palindrome
# - Partition array (like Dutch National Flag)
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Check if a sorted array has a pair that sums to a target
# Input:  arr = [1, 2, 4, 7, 11, 15], target = 9
# Output: True  (2 + 7 = 9)

def has_pair_with_sum(arr, target):
    left = 0
    right = len(arr) - 1

    while left < right:
        current_sum = arr[left] + arr[right]

        if current_sum == target:
            return True
        elif current_sum < target:
            left += 1   # need bigger sum, move left pointer right
        else:
            right -= 1  # need smaller sum, move right pointer left

    return False

print("Q1 - Pair with sum 9:", has_pair_with_sum([1, 2, 4, 7, 11, 15], 9))


# Q2: Move all negative numbers to the left, positives to the right
# (order within each side doesn't matter)
# Input:  [1, -2, 3, -4, 5, -6]
# Output: [-2, -4, -6, 1, 5, 3]  (any valid partition)

def move_negatives(arr):
    left = 0
    right = len(arr) - 1

    while left <= right:
        if arr[left] < 0:
            left += 1       # already negative, move on
        elif arr[right] >= 0:
            right -= 1      # already positive, move on
        else:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    return arr

print("Q2 - Move Negatives:", move_negatives([1, -2, 3, -4, 5, -6]))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Reverse an array in-place using two pointers
# Input:  [1, 2, 3, 4, 5]
# Output: [5, 4, 3, 2, 1]

# Q4: Remove duplicates from a SORTED array in-place, return new length
# Input:  [1, 1, 2, 3, 3, 4]
# Output: 4  (array becomes [1, 2, 3, 4, ...])

# Q5: Move all zeros to the end while keeping non-zero order intact
# Input:  [0, 1, 0, 3, 12]
# Output: [1, 3, 12, 0, 0]

# Q6: Find if a string is a palindrome using two pointers (ignore spaces/case)
# Input:  "A man a plan a canal Panama"
# Output: True

# Q7: Find a triplet in a sorted array that sums to zero
# Input:  [-4, -1, -1, 0, 1, 2]
# Output: [-1, -1, 2] and [-1, 0, 1]

# Q8: Merge two sorted arrays (with two pointers, no built-in merge)
# Input:  [1, 3, 5], [2, 4, 6]
# Output: [1, 2, 3, 4, 5, 6]

# Q9: Find the container with most water (given heights array)
# (Two pointers from both ends, maximize width * min_height)
# Input:  [1, 8, 6, 2, 5, 4, 8, 3, 7]
# Output: 49

# Q10: Sort an array of 0s, 1s, and 2s (Dutch National Flag)
# Input:  [2, 0, 1, 2, 1, 0]
# Output: [0, 0, 1, 1, 2, 2]
