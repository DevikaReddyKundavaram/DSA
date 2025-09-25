# 🔢 Generate Binary Numbers


## 📌 Problem Statement
Given a number **n**, the task is to generate all binary numbers with decimal values from **1 to n**.

---

## ✨ Examples
```text
Example1:
Input: n = 4
Output: ["1", "10", "11", "100"]
Explanation:** Binary numbers from 1 to 4 are 1, 10, 11 and 100.  

Example2:
Input: n = 6
Output: ["1", "10", "11", "100", "101", "110"]
Explanation:** Binary numbers from 1 to 6 are 1, 10, 11, 100, 101 and 110.  
```
---

## ✅ Constraints
- 1 ≤ n ≤ 10^6  

---

## 💡 Optimized Approach (Using Queue - BFS Style)

Instead of repeatedly converting numbers with `bin(i)`, we generate binary numbers directly using a queue.  
This gives a **linear time solution**.

---
---

## 📝 Algorithm

1. **Initialize**  
   - Create an empty result list `result`.  
   - Initialize a queue `q` and enqueue the first binary number `"1"`.  

2. **Process n times**  
   - For each iteration from `1` to `n`:  
     a. Dequeue the front element `curr`.  
     b. Append `curr` to the result list.  
     c. Enqueue `curr + "0"`.  
     d. Enqueue `curr + "1"`.  

3. **Return Result**  
   - After processing `n` iterations, return the result list.  

---

### 🔄 Example Walkthrough (n = 6)

| Step | Queue State               | Dequeued | Result             |
|------|----------------------------|----------|--------------------|
| 1    | ["1"]                     | "1"      | ["1"]              |
|      | enqueue "10", "11"        |          |                    |
| 2    | ["10", "11"]              | "10"     | ["1", "10"]        |
|      | enqueue "100", "101"      |          |                    |
| 3    | ["11", "100", "101"]      | "11"     | ["1", "10", "11"]  |
|      | enqueue "110", "111"      |          |                    |
| 4    | ["100", "101", "110", "111"] | "100"  | ["1","10","11","100"] |
| 5    | ["101", "110", "111", "1000"] | "101" | ["1","10","11","100","101"] |
| 6    | ["110", "111", "1000", "1001"] | "110" | ["1","10","11","100","101","110"] |

Final Output: `["1", "10", "11", "100", "101", "110"]`

---
---

## ⏳ Complexities

- **Time Complexity:**  
  - Each element is enqueued and dequeued exactly once.  
  - String concatenation happens only twice per iteration.  
  - **Overall:** `O(n)`  

- **Space Complexity:**  
  - The queue stores at most `O(n)` elements.  
  - The result list also holds `n` binary strings.  
  - **Overall:** `O(n)`  

---


## 🧑‍💻 Code (Python)

```python
from collections import deque

class Solution:
    def generateBinary(self, n):
        result = []
        q = deque()
        q.append("1")   
        
        for _ in range(n):
            curr = q.popleft()
            result.append(curr)
            
            q.append(curr + "0")
            q.append(curr + "1")
        
        return result
```
---
---

## 🚀 Applications

- ✅ **Digital Systems** – Generating binary sequences is fundamental in computer architecture and digital electronics.  
- ✅ **Testing & Simulation** – Useful in test case generation for binary input systems.  
- ✅ **Networking** – Binary sequences are the base of IP addressing and subnet calculations.  
- ✅ **Data Compression & Encoding** – Binary representation is applied in encoding schemes.  
- ✅ **Algorithmic Problems** – Helps in solving problems involving subsets, bitmasking, and combinatorial enumeration.  

---
---

## 🏷️ Tags

`#Queue` `#Binary` `#StringGeneration` `#BFS` `#BitManipulation` `#ProblemSolving` `#Easy` `#CompetitiveProgramming` `#InterviewPreparation`

---
