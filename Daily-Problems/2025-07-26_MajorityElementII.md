# 📊 Majority Element II

## 🧩 Problem Statement

You are given an array of integers `arr[]`, where each element represents a vote to a candidate.  
Return all candidates that received **more than ⌊n/3⌋ votes**.  
If no such candidates exist, return an **empty list**.  
The output must be in **increasing order**.

---

## 📝 Input Format

- An integer array `arr[]`
- `1 ≤ arr.length ≤ 10⁶`
- `1 ≤ arr[i] ≤ 10⁵`

---

## 📤 Output Format

- A list of all elements that appear more than ⌊n/3⌋ times, sorted in ascending order.

---

## 🔍 Examples

### Example 1

**Input:**
```python
arr = [2, 1, 5, 5, 5, 5, 6, 6, 6, 6, 6]
```
**Output:**
[5,6]
---
## ⚙️ Algorithm

### 🔍 Core Idea: Extended Boyer-Moore Voting Algorithm

We aim to find all elements in the array that appear more than ⌊n/3⌋ times. There can be **at most 2 such elements**.

### ✅ Steps:

1. **Initialization**:
   - Two candidate variables (`candidate1`, `candidate2`)
   - Two counters (`count1`, `count2`)

2. **First Pass – Find Potential Candidates**:
   - Traverse the array and apply the voting mechanism:
     - If the current number equals `candidate1`, increment `count1`.
     - Else if it equals `candidate2`, increment `count2`.
     - Else if `count1 == 0`, assign `candidate1 = num` and `count1 = 1`.
     - Else if `count2 == 0`, assign `candidate2 = num` and `count2 = 1`.
     - Else decrement both `count1` and `count2`.

3. **Second Pass – Validate Candidates**:
   - Re-count the actual frequency of `candidate1` and `candidate2`.
   - Only include them in the result if their count exceeds ⌊n/3⌋.

4. **Sort and Return** the result.

---

### ⏱️ Time & Space Complexity

| Metric     | Value        |
|------------|--------------|
| Time       | O(n)         |
| Space      | O(1)         |
| Extra Space for Output | O(1) to O(2) depending on result size |

---

## 💻 Code (Python)

```python
class Solution:
    def findMajority(self, arr):
        n = len(arr)
        if not arr:
            return []

        # Step 1: Find two potential candidates
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0

        for num in arr:
            if candidate1 == num:
                count1 += 1
            elif candidate2 == num:
                count2 += 1
            elif count1 == 0:
                candidate1 = num
                count1 = 1
            elif count2 == 0:
                candidate2 = num
                count2 = 1
            else:
                count1 -= 1
                count2 -= 1

        # Step 2: Verify candidates
        result = []
        if arr.count(candidate1) > n // 3:
            result.append(candidate1)
        if candidate2 != candidate1 and arr.count(candidate2) > n // 3:
            result.append(candidate2)

        return sorted(result)
```
---
## 🚀 Applications

### 🗳️ Voting & Elections
- Used in vote counting systems to identify candidates that have significant support (more than one-third of the total votes).
- Can be applied in polling systems to shortlist popular choices.

### 📊 Market Analysis
- Identifying top-selling products that constitute more than 33% of sales in a category.
- Tracking dominant user behavior patterns or trends in a dataset.

### 🧠 Recommendation Systems
- Helpful in detecting strong preferences among users (e.g., products, movies, etc., that are repeatedly chosen).

### 📈 Data Stream Processing
- Useful in streaming data (e.g., logs, telemetry) to detect elements that are frequently appearing without storing the full history.

### 🔍 Social Media & Sentiment Analysis
- Detecting repeated keywords, hashtags, or entities that dominate a conversation in a large dataset.

### 🔄 Compression & Optimization
- Identifying dominant elements can help in data compression, caching strategies, or memory optimization by focusing on frequently used values.

---
## 🏷️ Tags

`#Array`  
`#Hashing`  
`#Greedy`  
`#BoyerMooreVotingAlgorithm`  
`#MajorityElement`  
`#FrequencyCounting`  
`#MathBased`  
`#OptimizedLinearScan`
