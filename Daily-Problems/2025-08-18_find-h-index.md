# Find H-Index
---

## 📌 Problem Statement
You are given an array `citations[]`, where each element `citations[i]` represents the number of citations received by the `i-th` paper of a researcher.  
You need to calculate the researcher’s **H-Index**.

The **H-Index** is defined as the maximum value `H` such that the researcher has published at least `H` papers, and all those papers have citation value **greater than or equal to `H`**.

---

## 📝 Examples
```text
Example1:
Input: citations = [3, 0, 5, 3, 0]
Output: 3
Explanation: There are at least 3 papers with citation counts `[3, 5, 3]`, all having citations ≥ 3.

Example2:
Input: citations = [5, 1, 2, 4, 1]
Output: 2
Explanation: The H-index is 0 because there are no papers with at least 1 citation.
```
---

## 🔒 Constraints
- `1 ≤ citations.size() ≤ 10^6`  
- `0 ≤ citations[i] ≤ 10^6`

---

## 💡 Approach 1 (Sorting Based)
1. Sort the citations array in **descending order**.  
2. Traverse the array and check the largest `h` such that at least `h` papers have citations ≥ `h`.  
3. Return that `h` as the **H-Index**.

---
# ⏱️ Complexity Analysis

- **Time Complexity:** `O(n log n)` (due to sorting the citations array)  
- **Space Complexity:** `O(1)` (in-place sorting, ignoring input storage)  
---

## ✅ Python Solution
```python
class Solution:
    def hIndex(self, citations):
        # Sort in descending order
        citations.sort(reverse=True)
        
        h = 0
        for i, c in enumerate(citations):
            if c >= i + 1:
                h = i + 1
            else:
                break
        return h
```
---
### Approach 2: Bucket Counting (Optimized)
Instead of sorting, we can use a counting array (bucket) to directly count citation frequencies.  
- Any paper with citations ≥ `n` is bucketed into `n`.  
- Then, we scan from high to low to find the largest `h`.  
---

# ⏱️ Complexity Analysis
- **Time Complexity:** `O(n)`  
- **Space Complexity:** `O(n)` (for the counting array)  

---
##Python Solution
```python
class Solution:
    def hIndex(self, citations):
        n = len(citations)
        bucket = [0] * (n + 1)

        # Count citations into buckets
        for c in citations:
            if c >= n:
                bucket[n] += 1
            else:
                bucket[c] += 1

        total = 0
        # Traverse from high to low
        for h in range(n, -1, -1):
            total += bucket[h]
            if total >= h:
                return h
        return 0
```
---

## Applications
- **Academic Research:** Used to measure the productivity and citation impact of researchers.  
- **Journal Ranking:** Helps in evaluating the impact factor of journals.  
- **Hiring & Promotions:** Considered in academic hiring, tenure, and funding decisions.  
- **Bibliometrics:** Forms the basis for many metrics in libraries and digital repositories.  
- **General Threshold Problems:** Can be adapted to ranking systems where entities must satisfy a minimum performance threshold.  
---
## Tags
- `#Sorting`  
- `#BinarySearch`  
- `#Greedy`  
- `#BucketCounting`  
- `#Array`  
- `#Bibliometrics`  
