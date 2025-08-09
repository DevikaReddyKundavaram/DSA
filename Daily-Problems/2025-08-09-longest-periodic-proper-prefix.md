# 📝 Problem: Longest Periodic Proper Prefix

---

## 📄 Problem Statement

Given a string `s`, find the length of the **longest periodic proper prefix** of `s`.  

A **periodic proper prefix** is a non-empty prefix of `s` (but not the whole string) such that repeating this prefix enough times produces a string that **starts with** `s`.  

If no such prefix exists, return **-1**.

---

## 📥 Input

- A single string `s` containing lowercase English letters.

---

## 📤 Output

- An integer representing the length of the longest periodic proper prefix, or `-1` if it doesn’t exist.

---

## 🔍 Examples
```text
### Example 1
Input:  s = "aaaaaa" 
Output: 5 
Explanation: The prefix "aaaaa" repeated forms "aaaaaaaa...", which starts with "aaaaaa".

### Example 2

Input:  s = "abcab" 
Output: 3 
Explanation: The prefix "abc" repeated forms "abcabc...", which starts with "abcab".

### Example 3

Input:  s = "ababd" 
Output: -1 
Explanation: No periodic proper prefix exists.
```
---


## 📚 Constraints
- `1 ≤ |s| ≤ 10^6`
- `s` contains only lowercase English letters.

---

## 💡 Algorithm

We use the **Z-Algorithm** to compute the length of the longest substring starting at each position that matches the prefix of `s`.  
Then, we check from longest to shortest possible prefix length whether repeating that prefix covers the string `s` without mismatches.

---

### **Steps**
1. Compute the Z-array for string `s`.
2. Iterate from `n-1` down to `1` (longest possible prefix length to shortest).
3. For each length `L`:
   - Simulate moving in jumps of size `L` through the string.
   - At each step, check if the substring matches the prefix using the Z-array.
4. Return the first valid `L` found; if none found, return `-1`.

---

## ⏱ Complexity

- **Time Complexity:** `O(n)` (Z-algorithm + scanning)  
- **Space Complexity:** `O(n)` (Z-array)

---

## 🖥 Code (Python)

```python
class Solution:
    def getLongestPrefix(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return -1

        # Step 1: Compute Z-array
        z = [0] * n
        z[0] = n
        l = r = 0
        for i in range(1, n):
            if i <= r:
                z[i] = min(r - i + 1, z[i - l])
            while i + z[i] < n and s[z[i]] == s[i + z[i]]:
                z[i] += 1
            if i + z[i] - 1 > r:
                l, r = i, i + z[i] - 1

        # Step 2: Check longest to shortest possible prefix
        for L in range(n - 1, 0, -1):
            j = L
            ok = True
            while j < n:
                need = min(L, n - j)
                if z[j] < need:
                    ok = False
                    break
                j += L
            if ok:
                return L

        return -1
```
---

## 📦 Applications

- **Pattern detection in strings** — helps identify repeated segments in text data.
- **DNA/protein sequence analysis** — detects recurring genetic patterns.
- **Text compression** — finds repetitive substrings for better compression ratios.
- **Data validation** — ensures strings follow a required periodic pattern.
- **Music analysis** — identifies repeating rhythmic or melodic patterns.
- **Cybersecurity** — detects repeating sequences in encrypted or malicious code.


---
## 🏷️ Tags
`#Strings` `#ZAlgorithm` `#PatternMatching` `#StringProcessing` `#PrefixSuffix` `#PeriodicStrings` `#CompetitiveProgramming` `#InterviewPrep` `#HardProblems` `#AlgorithmOptimization`
---
