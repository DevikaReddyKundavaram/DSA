# 🔀 Merge Sort for Linked List

## 📌 Problem Statement  
You are given the head of a linked list.  
Sort the linked list using **Merge Sort** and return the head of the sorted list.

---

## 📝 Examples  
```text
Example 1:
Input: Linked List: 30 -> 10 -> 50 -> 20 -> 60 -> 40
Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60

Example 2:
Input: 
Linked List: 5 -> 2 -> 8 -> 9
Output: 2 -> 5 -> 8 -> 9
```
---

## ✅ Constraints
- `1 ≤ number of nodes ≤ 10^5`  
- `0 ≤ node->data ≤ 10^6`  

---

## ⚙️ Algorithm (Merge Sort on Linked List)  
1. If the list is empty or has only one node, return head.  
2. Split the list into two halves using **slow and fast pointers**.  
3. Recursively sort both halves.  
4. Merge the two sorted halves using a **merge procedure** similar to merging two sorted lists.  
5. Return the head of the merged sorted list.

---

## 🔄 Dry Run  

**Input:**  
Linked List: 30 -> 10 -> 50 -> 20 -> 60 -> 40


**Process:**  
- Split: `30 -> 10 -> 50` and `20 -> 60 -> 40`  
- Recursively sort left half: `10 -> 30 -> 50`  
- Recursively sort right half: `20 -> 40 -> 60`  
- Merge halves: `10 -> 20 -> 30 -> 40 -> 50 -> 60`  

✅ Output:  
10 -> 20 -> 30 -> 40 -> 50 -> 60

---

## ⏱️ Time & Space Complexity  

| Complexity | Explanation |
|------------|-------------|
| **Time Complexity** | `O(N log N)` – Splitting takes log N levels, merging N nodes at each level. |
| **Space Complexity** | `O(log N)` – Recursive stack space for dividing the list. |

---


## 💻 Python Implementation  

```python
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Solution:
    def mergeSort(self, head):
        if not head or not head.next:
            return head

        # Split list into halves
        middle = self.getMiddle(head)
        next_to_middle = middle.next
        middle.next = None

        # Recursively sort halves
        left = self.mergeSort(head)
        right = self.mergeSort(next_to_middle)

        # Merge sorted halves
        sorted_list = self.sortedMerge(left, right)
        return sorted_list

    def getMiddle(self, head):
        slow = head
        fast = head.next
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow

    def sortedMerge(self, a, b):
        if not a:
            return b
        if not b:
            return a
        if a.data <= b.data:
            result = a
            result.next = self.sortedMerge(a.next, b)
        else:
            result = b
            result.next = self.sortedMerge(a, b.next)
        return result
```
---
## 🌍 Applications  
- Sorting **linked lists** efficiently without using extra arrays.  
- Handling **large datasets** where arrays may be inefficient.  
- Used in **external sorting** where data cannot fit in memory.  
- Basis for **efficient multi-way merging** in linked structures.  

---

## 🏷️ Tags  
`#LinkedList` `#MergeSort` `#DivideAndConquer` `#Sorting` `#Recursive`

---
