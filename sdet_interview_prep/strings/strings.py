# =============================================================================
# TOPIC: STRINGS
# =============================================================================
#
# WHAT IS A STRING?
# A string is a sequence of characters. In Python, strings are immutable —
# you cannot change them in-place; you always create a new string.
#
# KEY CONCEPTS TO KNOW:
# - Indexing/Slicing works same as arrays: s[0], s[-1], s[1:4], s[::-1]
# - Strings are iterable: for ch in s
# - Common methods: lower(), upper(), strip(), split(), replace(), find(), count()
# - Join: "".join(list_of_chars)
# - Check type: isdigit(), isalpha(), isalnum(), isspace()
#
# HOW TO THINK ABOUT STRING PROBLEMS:
# 1. Convert to a list if you need to modify characters
# 2. Use a frequency dict (Counter) for character counting problems
# 3. Sorting characters helps in anagram problems
# 4. Two pointers work well for palindrome checks
# 5. Sliding window helps for substring problems
#
# TIME COMPLEXITIES:
# Access by index   -> O(1)
# Search (find)     -> O(n)
# Slicing           -> O(k) where k = slice length
# Concatenation     -> O(n) — use "".join() for efficiency
#
# COMMON PATTERNS IN INTERVIEWS:
# - Frequency map of characters
# - Reverse the string / check palindrome
# - Anagram detection (sort both or use frequency map)
# - Substring search
# - Parsing and validating format (useful for SDET: CSV, JSON, logs)
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Check if a string is a palindrome
# Input:  "racecar"
# Output: True
# Input:  "hello"
# Output: False

def is_palindrome(s):
    s = s.lower()
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        left += 1
        right -= 1

    return True

print("Q1 - Is Palindrome 'racecar':", is_palindrome("racecar"))
print("Q1 - Is Palindrome 'hello'  :", is_palindrome("hello"))


# Q2: Check if two strings are anagrams
# Input:  "listen", "silent"
# Output: True
# Input:  "hello", "world"
# Output: False

def are_anagrams(s1, s2):
    if len(s1) != len(s2):
        return False

    freq = {}

    for ch in s1:
        freq[ch] = freq.get(ch, 0) + 1

    for ch in s2:
        if ch not in freq or freq[ch] == 0:
            return False
        freq[ch] -= 1

    return True

print("Q2 - Anagram 'listen'/'silent':", are_anagrams("listen", "silent"))
print("Q2 - Anagram 'hello'/'world'  :", are_anagrams("hello", "world"))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Reverse words in a sentence (not individual characters)
# Input:  "hello world how are you"
# Output: "you are how world hello"

# Q4: Count the frequency of each character in a string
# Input:  "aabbccdde"
# Output: {'a': 2, 'b': 2, 'c': 2, 'd': 2, 'e': 1}

# Q5: Find the first non-repeating character in a string
# Input:  "aabbcde"
# Output: "c"

# Q6: Remove all duplicate characters from a string (keep first occurrence)
# Input:  "programming"
# Output: "progamin"

# Q7: Check if a string contains only digits
# Input:  "12345"
# Output: True
# Input:  "123a5"
# Output: False

# Q8: Count vowels and consonants in a string
# Input:  "hello world"
# Output: Vowels: 3, Consonants: 7

# Q9: Find the longest common prefix in a list of strings
# Input:  ["flower", "flow", "flight"]
# Output: "fl"

# Q10: Check if a string is a valid email format
# (must have exactly one @, at least one dot after @, no spaces)
# Input:  "test@example.com"
# Output: True
# Input:  "testexample.com"
# Output: False
