# 🔄 Swap Kth Nodes from Ends

## 📌 Problem
Given the head of a singly linked list and an integer `k`, swap the `k`th node (1-based index) from the **beginning** and the `k`th node from the **end** of the linked list.  
Return the head of the final formed list.  
If it's not possible to swap, return the original list.

---

## 📝 Examples
```text
Example 1  
Input: 1 -> 2 -> 3 -> 4 -> 5, k = 1
Output: 5 -> 2 -> 3 -> 4 -> 1

Example 2  
Input: 5 -> 9 -> 8 -> 5 -> 10 -> 3, k = 2  
Output: 5 -> 10 -> 8 -> 5 -> 9 -> 3
```
---

## ⚙️ Constraints
- `1 ≤ list size ≤ 10^4`  
- `1 ≤ node->data ≤ 10^6`  
- `1 ≤ k ≤ 10^4`  

---

## 🎯 Approach
1. Count the number of nodes `n`.  
2. If `k > n`, no swap possible.  
3. If `2*k - 1 == n`, it’s the same node → no change.  
4. Find:
   - `x` = kth node from start  
   - `y` = kth node from end (`n-k+1` from start)  
5. Swap their **previous pointers** and their **next pointers** carefully.  
6. Handle head pointer separately when swapping involves the head.  

---
# ⏱️ Time & Space Complexities

| Operation / Approach | Time Complexity | Space Complexity |
|-----------------------|-----------------|------------------|
| Counting nodes        | O(n)            | O(1)             |
| Finding kth from start| O(k)            | O(1)             |
| Finding kth from end  | O(n-k)          | O(1)             |
| Swapping nodes        | O(1)            | O(1)             |
| **Overall**           | **O(n)**        | **O(1)**         |
---

## 💻 Code

```python
class Node:
    def __init__(self, x):
        self.data = x
        self.next = None

class Solution:
    def swapKth(self, head, k):
        n = 0
        curr = head
        while curr:
            n += 1
            curr = curr.next
        
        if k > n:
            return head  
        if 2*k - 1 == n:
            return head  
        
        x_prev, x = None, head
        for i in range(1, k):
            x_prev = x
            x = x.next

        y_prev, y = None, head
        for i in range(1, n-k+1):
            y_prev = y
            y = y.next
        
        if x_prev:
            x_prev.next = y
        else:
            head = y
        
        if y_prev:
            y_prev.next = x
        else:
            head = x
        
        x.next, y.next = y.next, x.next
        
        return head
```
---
# 🚀 Applications

- Useful in **Linked List manipulation** problems where node reordering is needed.  
- Can be applied in **reversing parts of lists** without using extra space.  
- Helpful in **data structures courses/interviews** to test understanding of pointers and traversal.  
- Real-world analogy: **queue/line management** where elements from both ends need to be swapped.  
---
# 🏷️ Tags  

`#LinkedList` `#Pointers` `#TwoPointerTechnique` `#DataStructures` `#Swapping`  
  
