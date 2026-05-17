# =============================================================================
# TOPIC: LINKED LISTS
# =============================================================================
#
# WHAT IS A LINKED LIST?
# A linked list is a linear data structure where each element (node) contains:
#   - data: the value stored
#   - next: a reference (pointer) to the next node
# Unlike arrays, nodes are NOT stored in contiguous memory.
#
# TYPES:
# - Singly Linked List: each node points to the next only
# - Doubly Linked List: each node points to both next and previous
# - Circular Linked List: last node points back to the first
#
# KEY OPERATIONS:
# - Traversal: start at head, follow .next until None
# - Insert at head: new_node.next = head; head = new_node
# - Insert at tail: traverse to last node, set last.next = new_node
# - Delete: find the node before the target, set prev.next = target.next
#
# HOW TO THINK ABOUT LINKED LIST PROBLEMS:
# 1. Always draw it out — boxes with arrows help visualize pointer changes
# 2. Track prev, curr, next when reversing or deleting
# 3. Use slow/fast pointers (Floyd's algorithm) for cycle detection or midpoint
# 4. Use a dummy head node to simplify edge cases (empty list, single node)
# 5. Many problems become easy if you just build a new list instead of modifying
#
# TIME COMPLEXITIES:
# Access by index   -> O(n)  (must traverse)
# Insert at head    -> O(1)
# Insert at tail    -> O(n) without tail pointer
# Search            -> O(n)
# Delete            -> O(n) to find, O(1) to remove
#
# COMMON PATTERNS IN INTERVIEWS:
# - Reverse a linked list (iterative and recursive)
# - Detect a cycle (Floyd's slow/fast pointers)
# - Find the middle node (slow/fast pointers)
# - Merge two sorted lists
# - Remove nth node from end
#
# =============================================================================
# NODE CLASS (Used in all problems below)
# =============================================================================

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

def build_list(values):
    if not values:
        return None
    head = Node(values[0])
    current = head
    for val in values[1:]:
        current.next = Node(val)
        current = current.next
    return head

def print_list(head):
    result = []
    while head:
        result.append(str(head.data))
        head = head.next
    print(" -> ".join(result))


# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Reverse a linked list
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5 -> 4 -> 3 -> 2 -> 1

def reverse_linked_list(head):
    prev = None
    current = head

    while current:
        next_node = current.next   # save next
        current.next = prev        # reverse the pointer
        prev = current             # move prev forward
        current = next_node        # move current forward

    return prev  # prev is now the new head

head = build_list([1, 2, 3, 4, 5])
print("Q1 - Reversed:", end=" ")
print_list(reverse_linked_list(head))


# Q2: Find the middle of a linked list
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 3  (middle node)
# For even length [1,2,3,4], return second middle node (3)

def find_middle(head):
    slow = head
    fast = head

    while fast and fast.next:
        slow = slow.next        # moves 1 step
        fast = fast.next.next   # moves 2 steps

    return slow.data  # when fast reaches end, slow is at middle

head = build_list([1, 2, 3, 4, 5])
print("Q2 - Middle of list:", find_middle(head))


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Detect a cycle in a linked list (return True/False)
# Hint: Use Floyd's slow/fast pointer algorithm

# Q4: Find the length of a linked list
# Input:  1 -> 2 -> 3 -> 4 -> 5
# Output: 5

# Q5: Remove duplicates from an unsorted linked list
# Input:  1 -> 2 -> 3 -> 2 -> 1
# Output: 1 -> 2 -> 3

# Q6: Delete the nth node from the end of the list
# Input:  1 -> 2 -> 3 -> 4 -> 5, n = 2
# Output: 1 -> 2 -> 3 -> 5

# Q7: Merge two sorted linked lists into one sorted list
# Input:  1 -> 3 -> 5  and  2 -> 4 -> 6
# Output: 1 -> 2 -> 3 -> 4 -> 5 -> 6

# Q8: Check if a linked list is a palindrome
# Input:  1 -> 2 -> 3 -> 2 -> 1
# Output: True

# Q9: Find the intersection point of two linked lists
# (the node where two lists merge into one)

# Q10: Rotate a linked list to the right by k positions
# Input:  1 -> 2 -> 3 -> 4 -> 5, k = 2
# Output: 4 -> 5 -> 1 -> 2 -> 3
