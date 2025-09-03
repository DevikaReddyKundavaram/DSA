# 🔄 Reverse a Doubly Linked List
---

## 📌 Problem Statement  
You are given the head of a doubly linked list. You have to reverse the doubly linked list and return its head.

---

## 📝 Examples  
```text
Example 1:
Input: 1 <-> 2 <-> 3 <-> 4 <-> 5
Output: 5 <-> 4 <-> 3 <-> 2 <-> 1
Explanation: After reversing, the new list is `5 <-> 4 <-> 3 <-> 2 <-> 1`.

Example 2: 
Input: 75 <-> 122 <-> 59 <-> 196
Output: 196 <-> 59 <-> 122 <-> 75
Explanation: After reversing, the new list is `196 <-> 59 <-> 122 <-> 75`.
```
---

## 🎯 Constraints  
- 1 ≤ number of nodes ≤ 10^6  
- 0 ≤ node->data ≤ 10^4  

---

## 💡 Approach  
1. Traverse the list node by node.  
2. Swap each node’s `next` and `prev` pointers.  
3. Continue until traversal ends.  
4. The last visited node becomes the **new head**.  

---
## ⏱️ Complexities
- **Time Complexity:** O(N) → Each node is visited once.  
- **Space Complexity:** O(1) → In-place reversal without extra data structures.
---

## 🖥️ Code (Python)

```python
class Solution:
    def reverse(self, head):
        if not head:
            return head

        curr = head
        prev = None

        while curr:
            # Swap next and prev
            curr.prev, curr.next = curr.next, curr.prev
            prev = curr
            curr = curr.prev  # move using swapped pointer

        return prev  # new head

```
---
## 🚀 Applications
- **Undo/Redo functionality** → Used in editors where traversing forward/backward is required.  
- **Browser History Management** → Moving back and forth between pages.  
- **Playlist Management** → Switching songs in forward and reverse order.  
- **Navigation Systems** → Reversing paths or traversals.  
- **Data Structure Utilities** → Base operation for many advanced linked list manipulations.
---
## 🏷️ Tags
`#LinkedList` `#DoublyLinkedList` `#Reversal` `#TwoPointers` `#InPlace`
