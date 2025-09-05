# 🎨 Sort a Linked List of 0s, 1s and 2s

## Problem Statement

Given the head of a linked list where nodes can contain values **0s, 1s, and 2s only**, rearrange the list so that all **0s** appear at the beginning, followed by all **1s**, and all **2s** at the end.
---
Examples:
```text
Example 1
Input: head = 1 → 2 → 2 → 1 → 2 → 0 → 2 → 2
Output: 0 → 1 → 1 → 2 → 2 → 2 → 2 → 2

Example 2
Input: head = 2 → 2 → 0 → 1
Output: 0 → 1 → 2 → 2
```
### Constraints
- `1 ≤ no. of nodes ≤ 10^6`
- `0 ≤ node->data ≤ 2`

---

## Algorithm

We can solve this problem using two approaches:

### 🔹 Counting Approach (Efficient & Simple)
1. Traverse the linked list once and count the number of 0s, 1s, and 2s.  
2. Traverse again and overwrite node values with the counted number of 0s, then 1s, then 2s.  

### 🔹 Pointer Approach (In-place Rearrangement)
1. Create three dummy nodes: `zeroD`, `oneD`, `twoD` to represent sublists.  
2. Maintain pointers `zero`, `one`, `two` to build these lists.  
3. Traverse the original list:  
   - Append each node to its respective list (0, 1, or 2).  
4. Merge the three sublists: `zero → one → two`.  
5. Return the new head (`zeroD.next`).  

---
## Complexity Analysis

- **Time Complexity**:  
  - First traversal to count elements → `O(N)`  
  - Second traversal to overwrite values → `O(N)`  
  - Total = **O(N)**  

- **Space Complexity**:  
  - Only extra variables for counts (`0s, 1s, 2s`) → **O(1)**  

---


## Code Solution

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def segregate(self, head):
        if not head or not head.next:
            return head
        
        zeroD = Node(-1)
        oneD = Node(-1)
        twoD = Node(-1)

        zero = zeroD
        one = oneD
        two = twoD

        curr = head
        while curr:
            if curr.data == 0:
                zero.next = curr
                zero = zero.next
            elif curr.data == 1:
                one.next = curr
                one = one.next
            else:  # curr.data == 2
                two.next = curr
                two = two.next
            curr = curr.next

        zero.next = oneD.next if oneD.next else twoD.next
        one.next = twoD.next
        two.next = None
```
## Applications

This algorithm is useful in scenarios where linked data must be rearranged efficiently:

- **Data Classification** – Segregating categorical data (e.g., 0 = low, 1 = medium, 2 = high priority tasks).  
- **Memory Management** – Organizing linked memory blocks into different states (free, allocated, reserved).  
- **Network Packet Processing** – Grouping packets into priority levels (low/medium/high) for scheduling.  
- **Sorting Limited Range Values** – When the dataset only has a fixed set of values (like 0, 1, 2), this algorithm provides an optimized solution.  
- **Operating System Scheduling** – Tasks/jobs with states `waiting`, `running`, `completed` can be grouped efficiently.  
---
## Tags

`#LinkedList` `#Sorting` `#Pointers` `#DataStructures` `#Simulation`

---

        return zeroD.next
