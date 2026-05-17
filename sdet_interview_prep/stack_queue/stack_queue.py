# =============================================================================
# TOPIC: STACK AND QUEUE
# =============================================================================
#
# WHAT IS A STACK?
# A Stack follows LIFO — Last In, First Out.
# Think of a stack of plates: you add and remove from the top.
#
# Stack operations:
# - push(x)   -> add to top             -> list: append(x)
# - pop()     -> remove from top        -> list: pop()
# - peek()    -> view top without remove -> list: stack[-1]
# - is_empty  -> len(stack) == 0
#
# WHAT IS A QUEUE?
# A Queue follows FIFO — First In, First Out.
# Think of a line at a checkout: first person in is first served.
#
# Queue operations:
# - enqueue(x) -> add to back           -> list: append(x)   or  deque: append(x)
# - dequeue()  -> remove from front     -> list: pop(0) O(n) or  deque: popleft() O(1)
# - front()    -> view front element    -> queue[0]
# - is_empty   -> len(queue) == 0
#
# BEST PRACTICE: Use collections.deque for queues — pop(0) on a list is O(n),
# but deque.popleft() is O(1).
#
# HOW TO THINK ABOUT STACK/QUEUE PROBLEMS:
# Stack — ask: "Do I need to process in reverse order or match brackets?"
# Queue — ask: "Do I need to process things level by level (BFS)?"
#
# COMMON STACK PATTERNS:
# - Matching brackets / valid parentheses
# - Undo/redo operations
# - Next greater element
# - Evaluate expressions
# - Backtracking (DFS)
#
# COMMON QUEUE PATTERNS:
# - Level order traversal of a tree (BFS)
# - Process tasks in order received
# - Sliding window maximum
#
# TIME COMPLEXITIES:
# Stack push/pop/peek  -> O(1)
# Queue enqueue        -> O(1)
# Queue dequeue        -> O(1) with deque, O(n) with list
#
# =============================================================================
# SOLVED EXAMPLES
# =============================================================================

# Q1: Check if a string has valid/balanced parentheses
# Input:  "({[]})"
# Output: True
# Input:  "({[})"
# Output: False

def is_valid_parentheses(s):
    stack = []
    matching = {')': '(', '}': '{', ']': '['}

    for ch in s:
        if ch in '({[':
            stack.append(ch)        # opening bracket — push
        elif ch in ')}]':
            if not stack or stack[-1] != matching[ch]:
                return False        # no match — invalid
            stack.pop()             # matched — pop

    return len(stack) == 0          # valid only if nothing left

print("Q1 - Valid '({[]})' :", is_valid_parentheses("({[]})"))
print("Q1 - Valid '({[})' :", is_valid_parentheses("({[})"))


# Q2: Implement a queue using two stacks
# enqueue and dequeue should work in amortized O(1)

class QueueUsingStacks:
    def __init__(self):
        self.inbox = []     # for enqueue
        self.outbox = []    # for dequeue

    def enqueue(self, x):
        self.inbox.append(x)

    def dequeue(self):
        if not self.outbox:             # transfer when outbox is empty
            while self.inbox:
                self.outbox.append(self.inbox.pop())
        return self.outbox.pop() if self.outbox else None

q = QueueUsingStacks()
q.enqueue(1)
q.enqueue(2)
q.enqueue(3)
print("Q2 - Dequeue order:", q.dequeue(), q.dequeue(), q.dequeue())


# =============================================================================
# PRACTICE QUESTIONS (Solve these yourself)
# =============================================================================

# Q3: Reverse a string using a stack
# Input:  "hello"
# Output: "olleh"

# Q4: Design a Min Stack that supports push, pop, and getMin in O(1)
# Operations: push(5), push(3), push(7), getMin() -> 3, pop(), getMin() -> 3

# Q5: Find the Next Greater Element for each element in an array
# Input:  [4, 5, 2, 10, 8]
# Output: [5, 10, 10, -1, -1]  (-1 if no greater element to the right)

# Q6: Evaluate a Reverse Polish Notation (postfix) expression
# Input:  ["2", "1", "+", "3", "*"]
# Output: 9  ((2 + 1) * 3)

# Q7: Sort a stack using only one additional stack (no other data structure)
# Input:  stack = [3, 1, 4, 2]
# Output: [4, 3, 2, 1]  (top = 1, bottom = 4)

# Q8: Implement a Stack using two Queues
# push and pop should work correctly

# Q9: Find the largest rectangle in a histogram
# Input:  heights = [2, 1, 5, 6, 2, 3]
# Output: 10  (rectangle using heights 5 and 6)

# Q10: Given a list of tasks processed in order, find duplicate tasks
# using a queue-based approach
# Input:  tasks = ["login", "search", "login", "checkout", "search"]
# Output: {"login": [0, 2], "search": [1, 4]}
