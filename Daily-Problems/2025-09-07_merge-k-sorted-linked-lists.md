# 🔗 Merge K Sorted Linked Lists

## 📌 Problem Statement  
You are given an array `arr[]` of `n` sorted linked lists of different sizes.  
Your task is to merge all these lists into a single sorted linked list and return the head of the merged list.

---

## 📝 Examples  
```text
Example 1:
Input:  
1st list: 1 -> 3 -> 7
2nd list: 2 -> 4 -> 8
3rd list: 9
Output: 1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9

Example 2:
Input:
1st list: 1 -> 3
2nd list: 8
3rd list: 4 -> 5 -> 6
Output: 1 -> 3 -> 4 -> 5 -> 6 -> 8
```
---

## ✅ Constraints
- `1 ≤ total no. of nodes ≤ 10^5`  
- `1 ≤ node->data ≤ 10^3`

---

## ⚙️ Algorithm (Using Min Heap / Priority Queue)  
1. Create a **min-heap** to store the head nodes of all linked lists.  
2. Insert the first node of each list into the heap.  
3. Repeatedly extract the **minimum element** from the heap and add it to the result list.  
4. If the extracted node has a next node, insert it into the heap.  
5. Continue until the heap is empty.  
6. Return the head of the merged list.

---

## 🔄 Dry Run  

**Input:**  
Lists: [1 -> 3 -> 7], [2 -> 4 -> 8], [9]

**Process:**  
- Insert heads `[1, 2, 9]` → Heap = `[1, 2, 9]`  
- Pop 1 → Result = `1` → Push `3` → Heap = `[2, 3, 9]`  
- Pop 2 → Result = `1 -> 2` → Push `4` → Heap = `[3, 4, 9]`  
- Pop 3 → Result = `1 -> 2 -> 3` → Push `7` → Heap = `[4, 7, 9]`  
- Pop 4 → Result = `1 -> 2 -> 3 -> 4` → Push `8` → Heap = `[7, 8, 9]`  
- Pop 7 → Result = `1 -> 2 -> 3 -> 4 -> 7` → Heap = `[8, 9]`  
- Pop 8 → Result = `1 -> 2 -> 3 -> 4 -> 7 -> 8` → Heap = `[9]`  
- Pop 9 → Result = `1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9`  

✅ Final Result: `1 -> 2 -> 3 -> 4 -> 7 -> 8 -> 9`

---

## ⏱️ Time & Space Complexity  

- **Time Complexity:**  
  - Inserting & Extracting from Heap = `O(log k)`  
  - For `N` total nodes → `O(N log k)`  
- **Space Complexity:** `O(k)` (heap stores at most `k` nodes at a time)  
---


## 💻 Python Implementation  

```python
import heapq

class Node:
    def __init__(self, x):
        self.data = x
        self.next = None
    
    # For heap comparison
    def __lt__(self, other):
        return self.data < other.data

class Solution:
    def mergeKLists(self, arr):
        heap = []
        
        # Push first node of each list into min heap
        for head in arr:
            if head:
                heapq.heappush(heap, head)
        
        dummy = Node(0)
        curr = dummy
        
        while heap:
            # Get min node
            node = heapq.heappop(heap)
            curr.next = node
            curr = curr.next
            
            # Push next node if available
            if node.next:
                heapq.heappush(heap, node.next)
        return dummy.next
```
---
## 🌍 Applications  

- 📑 **Merging Sorted Logs:** Combine log files from multiple servers that are already sorted by timestamp.  
- 📊 **Data Stream Processing:** Merge real-time sorted streams of data (e.g., stock prices, sensor data).  
- 💾 **External Sorting:** Used in database systems and external merge sort when datasets are too large for memory.  
- 🔗 **Search Engines:** Merging sorted posting lists during query processing.  
- 🗂️ **File Systems / Backup Systems:** Combining multiple sorted snapshots or versions into one.  
- 🧮 **Divide & Conquer Algorithms:** Forms the basis for multi-way merge strategies in algorithms like **k-way merge sort**.  
---
## 🏷️ Tags  
`#LinkedList` `#Heap` `#DivideAndConquer` `#Merge` `#PriorityQueue` `#Sorting`


      

