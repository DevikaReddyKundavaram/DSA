# Queue Reversal

## Problem Statement

Given a queue `q` containing integer elements, your task is to **reverse the queue**.

### Examples
```text
Input: q[] = [5, 10, 15, 20, 25]
Output: [25, 20, 15, 10, 5]
Explanation: After reversing the given elements of the queue, the resultant queue will be `25 20 15 10 5`.

Input: q[] = [1, 2, 3, 4, 5]
Output: [5, 4, 3, 2, 1]
Explanation: After reversing the given elements of the queue, the resultant queue will be `5 4 3 2 1`.

---
### Constraints
- `1 ≤ q.size() ≤ 10^3`  
- `0 ≤ q[i] ≤ 10^5`  

---
## Algorithm: Reverse a Queue

**Input:** A queue `q` containing integer elements.  
**Output:** The queue `q` with its elements reversed.

### Steps:

1. **Initialize a stack**:
   - Create an empty stack `stack`.

2. **Transfer elements from the queue to the stack**:
   - While the queue `q` is not empty:
     - Dequeue an element from `q` (using `q.popleft()` in Python).
     - Push the dequeued element onto `stack`.

3. **Transfer elements back from the stack to the queue**:
   - While the stack is not empty:
     - Pop an element from `stack`.
     - Enqueue the popped element back to `q` (using `q.append()` in Python).

4. **Return the queue**:
   - The queue now contains the elements in reverse order
---
### Complexity Analysis:

- **Time Complexity:** `O(n)` (each element is moved twice: once to stack, once back to queue)  
- **Space Complexity:** `O(n)` (for storing elements in the stack)
---

## Python Solution

```python
from collections import deque

class Solution:
    def reverseQueue(self, q):
        stack = []
        
        # Push all elements of the queue into the stack
        while q:
            stack.append(q.popleft())
        
        # Pop all elements from the stack and put them back in the queue
        while stack:
            q.append(stack.pop())
        
        return q
```
---

## Applications of Queue Reversal

Reversing a queue is a fundamental operation and can be applied in various scenarios:

1. **Undo Operations in Software**  
   - Many software applications, like text editors or graphic editors, use queues or stacks to track user actions. Reversing the queue helps in implementing undo/redo functionality efficiently.

2. **Palindrome Checking**  
   - By reversing a queue and comparing it with the original, we can check if a sequence of elements forms a palindrome.

3. **Task Scheduling**  
   - In certain scheduling algorithms, tasks may need to be processed in the reverse order of their arrival. Reversing the queue helps in handling such cases.

4. **Algorithmic Problems**  
   - Many competitive programming or coding interview problems require queue reversal as a subroutine, such as reversing first `k` elements of a queue.

5. **Expression Evaluation**  
   - In some cases, reversing the order of elements in a queue can simplify parsing or evaluating expressions (e.g., converting infix to postfix).

6. **Data Stream Processing**  
   - When processing streams of data where the latest elements need priority, reversing a queue can help in processing the newest items first.

---

## Tags

- `#Stack`, `#Queue` ,`#DataStructures`, `#Easy`, `#ProblemSolving`, `#Recursion`, `#Algorithms`, `#CompetitiveProgramming`, `#InterviewPreparation`
