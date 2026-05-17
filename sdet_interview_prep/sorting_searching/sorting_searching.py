# =============================================================================
# TOPIC: SORTING AND SEARCHING
# =============================================================================
#
# WHY SORTING MATTERS IN INTERVIEWS:
# Many problems become much easier after sorting the input.
# Sorting costs O(n log n) but can reduce the overall solution complexity.
#
# BUILT-IN PYTHON SORTING:
# - sorted(arr)           -> returns new sorted list, O(n log n)
# - arr.sort()            -> sorts in-place, O(n log n)
# - sorted(arr, reverse=True)           -> descending
# - sorted(arr, key=lambda x: x[1])     -> sort by custom key
# - sorted(words, key=lambda w: len(w)) -> sort by length
#
# BINARY SEARCH — THE MOST IMPORTANT SEARCH ALGORITHM:
# - Only works on SORTED arrays
# - Repeatedly halves the search space
# - Time: O(log n), Space: O(1)
# - Template:
#     left, right = 0, len(arr) - 1
#     while left <= right:
#         mid = (left + right) // 2
#         if arr[mid] == target: return mid
#         elif arr[mid] < target: left = mid + 1
#         else: right = mid - 1
#
# SORTING ALGORITHMS (know the basics):
# Bubble Sort    -> O(n^2)   — simple, swap adjacent elements
# Selection Sort -> O(n^2)   — find min, place at front each pass
# Insertion Sort -> O(n^2)   — build sorted portion left to right
# Merge Sort     -> O(n log n) — divide, sort halves, merge
# Quick Sort     -> O(n log n) avg — pivot and partition
#
# HOW TO THINK ABOUT SORTING/SEARCHING PROBLEMS:
# 1. Is the array sorted? If yes, think binary search.
# 2. Does sorting first help? (e.g., finding pairs, duplicates, median)
# 3. Do I need stability? (Python's sort is stable — equal elements keep order)
# 4. Do I need to sort by a custom key?
#
# SDET RELEVANCE:
# - Sort test results by severity/duration
# - Binary search for a specific log entry by timestamp
# - Rank failing tests by frequency
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Binary Search — find index of target in sorted array
# Input:  arr = [1, 3, 5, 7, 9, 11], target = 7
# Output: 3  (index of 7)
# Output: -1 if not found

def binary_search(arr, target):
    left = 0
    right = len(arr) - 1

    while left <= right:
        mid = (left + right) // 2

        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1    # target is in right half
        else:
            right = mid - 1   # target is in left half

    return -1

print("Q1 - Binary Search for 7 :", binary_search([1, 3, 5, 7, 9, 11], 7))
print("Q1 - Binary Search for 6 :", binary_search([1, 3, 5, 7, 9, 11], 6))


# Q2: Sort an array of 0s, 1s, and 2s (Dutch National Flag Problem)
# Input:  [2, 0, 1, 2, 1, 0, 0, 1]
# Output: [0, 0, 0, 1, 1, 1, 2, 2]
# Constraint: O(n) time, O(1) space, single pass

def sort_0_1_2(arr):
    low = 0
    mid = 0
    high = len(arr) - 1

    while mid <= high:
        if arr[mid] == 0:
            arr[low], arr[mid] = arr[mid], arr[low]
            low += 1
            mid += 1
        elif arr[mid] == 1:
            mid += 1
        else:
            arr[mid], arr[high] = arr[high], arr[mid]
            high -= 1

    return arr

print("Q2 - Sort 0s 1s 2s:", sort_0_1_2([2, 0, 1, 2, 1, 0, 0, 1]))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Find the first and last position of a target in a sorted array
# Input:  arr = [1, 2, 2, 2, 3, 4], target = 2
# Output: [1, 3]  (first at index 1, last at index 3)

# Q4: Find the element in a rotated sorted array
# Input:  arr = [4, 5, 6, 7, 0, 1, 2], target = 0
# Output: 4  (index of 0)

# Q5: Implement Bubble Sort
# Input:  [5, 3, 1, 4, 2]
# Output: [1, 2, 3, 4, 5]

# Q6: Find the kth smallest element in an unsorted array
# Input:  arr = [7, 2, 1, 6, 5, 3, 4], k = 3
# Output: 3

# Q7: Sort a list of strings by their length
# Input:  ["banana", "apple", "fig", "cherry", "date"]
# Output: ["fig", "date", "apple", "banana", "cherry"]

# Q8: Merge two sorted arrays without extra space
# Input:  arr1 = [1, 4, 7, 8, 10], arr2 = [2, 3, 9]
# Output: arr1 = [1, 2, 3, 4, 7], arr2 = [8, 9, 10]

# Q9: Find the peak element (greater than both neighbors) in an array
# Input:  [1, 3, 20, 4, 1, 0]
# Output: 20  (index 2)

# Q10: Count inversions in an array
# (an inversion is a pair where arr[i] > arr[j] and i < j)
# Input:  [2, 4, 1, 3, 5]
# Output: 3  (pairs: (2,1), (4,1), (4,3))
