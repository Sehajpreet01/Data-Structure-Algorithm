# =============================================================================
# TOPIC: HASHMAPS (Dictionaries)
# =============================================================================
#
# WHAT IS A HASHMAP?
# A hashmap (called dict in Python) stores key-value pairs.
# It uses hashing internally to give O(1) average time for insert/lookup/delete.
#
# KEY CONCEPTS TO KNOW:
# - Create:   freq = {}  or  freq = dict()
# - Insert:   freq[key] = value
# - Access:   freq[key]  — raises KeyError if missing
# - Safe get: freq.get(key, default)  — returns default if missing
# - Check:    key in freq
# - Delete:   del freq[key]
# - Iterate:  for k, v in freq.items()
# - Keys:     freq.keys()
# - Values:   freq.values()
#
# HOW TO THINK ABOUT HASHMAP PROBLEMS:
# 1. If you need to COUNT something — use a dict (frequency map)
# 2. If you need to LOOK UP something fast — use a dict
# 3. If you need to GROUP things — use a dict of lists
# 4. If you need to CHECK EXISTENCE — use a set (dict without values)
# 5. Trade space for time: O(n) space for O(1) lookup
#
# TIME COMPLEXITIES:
# Insert    -> O(1) average
# Lookup    -> O(1) average
# Delete    -> O(1) average
# Iteration -> O(n)
#
# COMMON PATTERNS IN INTERVIEWS:
# - Frequency counting: count how many times each element appears
# - Two Sum: store seen values to find complement in one pass
# - Grouping: group elements by a property (e.g., anagrams by sorted key)
# - De-duplication: track visited/seen elements
# - Caching: store computed results (memoization)
#
# SDET RELEVANCE:
# - Count test failures by category
# - Group log entries by error type
# - Track unique IDs or duplicate entries in test data
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Find two numbers in an array that add up to a target (Two Sum)
# Input:  arr = [2, 7, 11, 15], target = 9
# Output: [0, 1]  (indices of 2 and 7)

def two_sum(arr, target):
    seen = {}  # stores {value: index}

    for i, num in enumerate(arr):
        complement = target - num
        if complement in seen:
            return [seen[complement], i]
        seen[num] = i

    return []

print("Q1 - Two Sum:", two_sum([2, 7, 11, 15], 9))


# Q2: Group a list of words by their anagram family
# Input:  ["eat", "tea", "tan", "ate", "nat", "bat"]
# Output: [['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat']]

def group_anagrams(words):
    groups = {}

    for word in words:
        key = "".join(sorted(word))  # sorted chars = same for all anagrams
        if key not in groups:
            groups[key] = []
        groups[key].append(word)

    return list(groups.values())

print("Q2 - Group Anagrams:", group_anagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Count the frequency of each element in a list
# Input:  [1, 2, 2, 3, 3, 3, 4]
# Output: {1: 1, 2: 2, 3: 3, 4: 1}

# Q4: Find all elements that appear more than once
# Input:  [4, 3, 2, 7, 8, 2, 3, 1]
# Output: [2, 3]

# Q5: Find the element that appears most frequently
# Input:  [1, 3, 2, 1, 4, 1, 3]
# Output: 1  (appears 3 times)

# Q6: Find the intersection of two lists (common elements, no duplicates)
# Input:  [1, 2, 2, 3, 4], [2, 2, 3, 5]
# Output: [2, 3]

# Q7: Check if two strings are anagrams using a frequency map
# Input:  "anagram", "nagaram"
# Output: True

# Q8: Find the first element that appears exactly once
# Input:  [9, 4, 9, 6, 7, 4]
# Output: 6

# Q9: Given a list of test results (pass/fail), count how many of each
# Input:  ["pass", "fail", "pass", "pass", "fail", "error"]
# Output: {"pass": 3, "fail": 2, "error": 1}

# Q10: Find all pairs in an array with a given difference
# Input:  arr = [1, 5, 3, 4, 2], diff = 2
# Output: [(1, 3), (3, 5), (2, 4)]
