# Maximum Non-Overlapping Odd Palindrome Sum

## Problem Statement
Given a string `s` consisting of lowercase English letters, find the **maximum possible sum** of the lengths of any two **non-empty** and **non-overlapping** palindromic substrings of **odd length**.

Formally, choose any two substrings `s[i...j]` and `s[k...l]` such that:

- `1 ≤ i ≤ j < k ≤ l ≤ s.size()`
- Both substrings are **palindromes** of **odd length**
- They do **not** overlap

Return the **maximum sum** of their lengths.

### Notes:
- A **palindrome** is a string that reads the same forward and backward.
- A **substring** is a contiguous sequence of characters within the string.

---

## Examples

### Example 1:
Input:  s = "xyabacbcz" Output: 6 Explanation: "aba" (length 3) and "cbc" (length 3) are non-overlapping odd-length palindromes. Sum = 3 + 3 = 6.

### Example 2:

Input:  s = "gfgforgeeks" Output: 4 Explanation: "gfg" (length 3) and "g" (length 1) are non-overlapping odd-length palindromes. Sum = 3 + 1 = 4.

---

## Constraints

2 ≤ s.size() ≤ 10^5 s consists only of lowercase English letters

---

## Approach

### 1. Key Observations
- Only **odd-length palindromes** are considered.
- Need **two non-overlapping** palindromes with maximum sum.
- Brute force (`O(n^3)`) is **too slow** for `n = 10^5`.
- Use **Manacher’s Algorithm** to find maximum odd palindrome length centered at each position in `O(n)` time.

### 2. Steps
1. **Find all odd-length palindromes** using Manacher’s algorithm.
2. Build:
   - `left_max[i]`: max palindrome length in `s[0..i]`
   - `right_max[i]`: max palindrome length in `s[i..n-1]`
3. Iterate split points `i`:
   - Take `left_max[i] + right_max[i+1]`
   - Keep track of maximum sum.
---
### 3. Complexity
- **Time:** `O(n)` (Manacher’s + prefix/suffix arrays)
- **Space:** `O(n)`

---

## Code Implementation (Python)

```python
class Solution:
    def maxSum(self, s: str) -> int:
        n = len(s)

        # Manacher's algorithm for odd-length palindromes
        d = [0] * n
        l, r = 0, -1
        for i in range(n):
            k = 1 if i > r else min(d[l + r - i], r - i + 1)
            while i - k >= 0 and i + k < n and s[i - k] == s[i + k]:
                k += 1
            d[i] = k
            if i + k - 1 > r:
                l, r = i - k + 1, i + k - 1

        # Left max array
        left_max = [0] * n
        for i in range(n):
            length = 2 * d[i] - 1
            left_idx = i - d[i] + 1
            right_idx = i + d[i] - 1
            left_max[right_idx] = max(left_max[right_idx], length)
        for i in range(1, n):
            left_max[i] = max(left_max[i], left_max[i - 1])

        # Right max array
        right_max = [0] * n
        for i in range(n):
            length = 2 * d[i] - 1
            left_idx = i - d[i] + 1
            right_idx = i + d[i] - 1
            right_max[left_idx] = max(right_max[left_idx], length)
        for i in range(n - 2, -1, -1):
            right_max[i] = max(right_max[i], right_max[i + 1])

        # Find max sum of non-overlapping
        ans = 0
        for i in range(n - 1):
            ans = max(ans, left_max[i] + right_max[i + 1])
        return ans


---

## 📌 Applications

- **Text Analysis & NLP** – Identifying symmetric patterns in large text data for linguistic analysis.
- **DNA/Genome Sequencing** – Detecting palindromic structures in biological sequences for mutation analysis.
- **Data Compression** – Finding repeating palindromic patterns to optimize storage.
- **Cybersecurity** – Pattern detection in encrypted or obfuscated text streams.
- **Competitive Programming** – Common interview and contest problem for practicing Manacher’s algorithm & substring partitioning.
- **Search Engines** – Efficient substring pattern recognition in query optimization.
---
**🏷️Tags:** `#String`, `#Palindrome`, `#OddLength`, `#NonOverlapping`, `#DynamicProgramming`, `#ManachersAlgorithm`, `#TwoPointer`, `#CompetitiveProgramming`
