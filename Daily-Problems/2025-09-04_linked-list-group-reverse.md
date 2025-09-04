# Linked List Group Reverse

## Problem Statement

You are given the head of a **singly linked list**. You have to reverse every `k` nodes in the linked list and return the head of the modified list.

**Note:**  
If the number of nodes is not a multiple of `k`, then the leftover nodes at the end should also be considered as a group and must be reversed.

## Examples
```text
Example 1
Input: head = [1, 2, 3, 4, 5], k = 2
Output: [2, 1, 4, 3, 5]

Example 2
Input: head = [1, 2, 3, 4, 5], k = 3
Output: [3, 2, 1, 5, 4]
```
### Constraints
- The number of nodes in the list is in the range `[1, 5000]`.
- `0 <= Node.val <= 1000`
- `1 <= k <= size of list`

---
## Algorithm

1. Create a dummy node pointing to the head.  
2. Initialize a pointer `group_prev` at dummy.  
3. For each group of `k` nodes:  
   - Find the `kth` node starting from `group_prev`.  
   - If less than `k` nodes remain → stop (end of list).  
   - Store `group_next = kth.next` (start of next group).  
   - Reverse the current group of `k` nodes.  
   - Connect `group_prev.next` to the new head of the reversed group.  
   - Move `group_prev` pointer to the tail of the reversed group.  
4. Continue until the list ends.  
5. Return `dummy.next` (new head).  

---
## Complexity Analysis

| Complexity Type   | Value  | Explanation |
|-------------------|--------|-------------|
| **Time**          | O(n)   | Each node is processed and reversed exactly once. |
| **Space**         | O(1)   | Reversal is done in-place using only pointers.   |

---

## Code Solution

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        def reverse(start, end):
            prev, curr = None, start
            while curr != end:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        dummy = ListNode(0, head)
        group_prev = dummy

        while True:
            kth = group_prev
            for _ in range(k):
                kth = kth.next
                if not kth:
                    return dummy.next

            group_next = kth.next
            prev, curr = group_next, group_prev.next

            while curr != group_next:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt

            temp = group_prev.next
            group_prev.next = prev
            group_prev = temp
```
## Applications

- **Batch Processing**  
  Reversing linked list nodes in groups is useful in batch-processing tasks where data is processed in fixed-size chunks.

- **Streaming Data**  
  Helpful in handling streams where elements arrive continuously but need to be rearranged in blocks.

- **Networking**  
  Used in packet manipulation, where packets of fixed size are reversed or reordered before transmission.

- **Operating Systems**  
  In memory management, block-wise operations sometimes require reversing or reordering memory blocks.

- **Encryption / Decryption**  
  Applied in block ciphers where data is encrypted/decrypted in chunks.
---
## Tags

- `#LinkedList`
- `#TwoPointers`
- `#Simulation`
- `#DataStructures`
---
