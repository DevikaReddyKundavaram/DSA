# Find Length of Loop in a Linked List

## Problem

Given the head of a linked list, determine whether the list contains a loop.  
- If a loop is present, return the number of nodes in the loop.  
- If no loop is present, return `0`.

**Note:** Internally, `pos` (1-based index) denotes the position of the node where the tail’s `next` pointer is connected.  
- If `pos = 0`, it means the last node points to `null`, indicating there is no loop.  
- `pos` is not passed as a parameter.

---

## Examples
```text
Example 1
Input: pos = 2
Output: 4
Explanation: There exists a loop in the linked list and the length of the loop is `4`.

Example 2
Input: pos = 3
Output: 3
Explanation: The loop is from `19 → 33 → 10`, so the length of the loop is `3`.

Example 3
Input: pos = 0
Output: 0
Explanation: No loop exists.
```
---

## Constraints
- `1 ≤ number of nodes ≤ 10^5`  
- `1 ≤ node->data ≤ 10^4`  
- `0 ≤ pos < number of nodes`  

---
## Algorithm

1. Initialize two pointers: `slow` and `fast`, both pointing to the head of the linked list.  
2. Move `slow` one step at a time (`slow = slow.next`).  
3. Move `fast` two steps at a time (`fast = fast.next.next`).  
4. If at any point `slow == fast`, a loop is detected.  
5. To find the length of the loop:  
   - Keep one pointer fixed at the meeting point.  
   - Move the other pointer step by step until it comes back to the fixed pointer.  
   - Count the number of steps taken → this is the length of the loop.  
6. If no loop is found (`fast` or `fast.next` becomes `None`), return `0`.  
---
## Complexity Analysis

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | **O(N)** – At most two traversals of the linked list (one to detect the loop and one to count its length). |
| **Space Complexity** | **O(1)** – Only two pointers (`slow` and `fast`) are used, no extra space needed. |
---

## Code (Floyd’s Cycle Detection)

```python
class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class Solution:
    def lengthOfLoop(self, head):
        slow = fast = head

        # Detect loop using Floyd’s Cycle Detection
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

            if slow == fast:  # Loop detected
                return self.getLoopLength(slow)

        return 0

    def getLoopLength(self, node):
        count = 1
        temp = node.next
        while temp != node:
            count += 1
            temp = temp.next
        return count
```
---
## Applications

- **Cycle Detection in Linked Lists** – Prevents infinite traversal during iteration.  
- **Operating Systems** – Detecting cyclic dependencies in process scheduling or resource allocation.  
- **Networking** – Identifying routing loops in network paths.  
- **Blockchain / Distributed Systems** – Detecting repeated reference chains or circular dependencies.  
- **Compiler Design** – Finding cycles in dependency graphs (variables, modules, or functions).  
---
## Tags

`#LinkedList` `#CycleDetection` `#FloydAlgorithm` `#TwoPointers` `#DataStructures`

