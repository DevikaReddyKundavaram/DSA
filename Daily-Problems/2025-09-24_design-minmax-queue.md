# 🛤️ Design MinMax Queue

## Problem Statement

Design a **SpecialQueue** data structure that functions like a normal queue but with additional support for retrieving the **minimum** and **maximum** element efficiently.  

The SpecialQueue must support the following operations:

- `enqueue(x)`: Insert an element `x` at the rear of the queue.  
- `dequeue()`: Remove the element from the front of the queue.  
- `getFront()`: Return the front element without removing.  
- `getMin()`: Return the minimum element in the queue in **O(1)** time.  
- `getMax()`: Return the maximum element in the queue in **O(1)** time.  

There will be a sequence of queries `queries[][]`.  
The queries are represented in numeric form:  

- `1 x` : Call `enqueue(x)`  
- `2` : Call `dequeue()`  
- `3` : Call `getFront()`  
- `4` : Call `getMin()`  
- `5` : Call `getMax()`  

You only need to implement the above five functions.  

---

## Examples
```text
Example1:
Input: q = 6, queries = [[1, 4], [1, 2], [3], [4], [2], [5]]
Output: [4, 2, 2]
Explanation:
- `enqueue(4)` → queue = [4]  
- `enqueue(2)` → queue = [4,2]  
- `getFront()` → 4  
- `getMin()` → 2  
- `dequeue()` → removes 4 → queue = [2]  
- `getMax()` → 2  

Example2:
Input: q = 4, queries = [[1, 3], [4], [1, 5], [5]]
Output: [3, 5]
Explanation: 
- `enqueue(3)` → queue = [3]  
- `getMin()` → 3  
- `enqueue(5)` → queue = [3,5]  
- `getMax()` → 5  
```
---

## Constraints

- `1 ≤ queries.size() ≤ 10^5`  
- `0 ≤ values in the queue ≤ 10^9`  

---

## Algorithm

1. Maintain **three deques**:
   - A **normal queue** (`q`) to store elements in order.  
   - A **monotonic increasing deque** (`minQ`) to track the minimum.  
   - A **monotonic decreasing deque** (`maxQ`) to track the maximum.  

2. **enqueue(x):**
   - Add `x` to `q`.  
   - Maintain increasing order in `minQ` (pop back until last > x).  
   - Maintain decreasing order in `maxQ` (pop back until last < x).  

3. **dequeue():**
   - Remove element from front of `q`.  
   - If it equals the front of `minQ`, pop from `minQ`.  
   - If it equals the front of `maxQ`, pop from `maxQ`.  

4. **getFront():**
   - Return `q[0]`.  

5. **getMin():**
   - Return `minQ[0]`.  

6. **getMax():**
   - Return `maxQ[0]`.  
---
## Complexities

- **Enqueue:** O(1) amortized  
- **Dequeue:** O(1)  
- **GetFront:** O(1)  
- **GetMin:** O(1)  
- **GetMax:** O(1)  

**Overall Time Complexity:** O(1) per operation (amortized)  
**Space Complexity:** O(n) for storing elements in the queue and auxiliary deques  
(n)`  

---

## Python Solution

```python
from collections import deque

class SpecialQueue:
    def __init__(self):
        self.q = deque()     
        self.minQ = deque()  
        self.maxQ = deque()  

    def enqueue(self, x):
        self.q.append(x)

        while self.minQ and self.minQ[-1] > x:
            self.minQ.pop()
        self.minQ.append(x)

        while self.maxQ and self.maxQ[-1] < x:
            self.maxQ.pop()
        self.maxQ.append(x)

    def dequeue(self):
        if not self.q:
            return None
        val = self.q.popleft()

        if val == self.minQ[0]:
            self.minQ.popleft()
        if val == self.maxQ[0]:
            self.maxQ.popleft()
        return val

    def getFront(self):
        return None if not self.q else self.q[0]

    def getMin(self):
        return None if not self.minQ else self.minQ[0]

    def getMax(self):
        return None if not self.maxQ else self.maxQ[0]
```
---

## Applications

1. **Streaming Analytics**  
   - Track real-time minimum and maximum values in a continuous stream of data.  

2. **Sliding Window Problems**  
   - Used in algorithms where you need to find min/max values of elements in a moving window efficiently.  

3. **Stock Market Analysis**  
   - Helps in quickly retrieving the highest and lowest stock prices in a given timeframe.  

4. **Task Scheduling and Load Balancing**  
   - Assign tasks based on minimum or maximum priority values.  

5. **Data Monitoring Systems**  
   - Useful in IoT or logging systems to monitor whether values cross thresholds (min/max).  

6. **Competitive Programming & Interviews**  
   - Commonly asked problem type to test data structure design and optimization skills.  
---
## 🏷️Tags

`#Queue` `#Deque` `#Stack` `#DataStructures` `#MonotonicQueue` `#Algorithms` `#ProblemSolving` `#CompetitiveProgramming` `#InterviewPreparation`
