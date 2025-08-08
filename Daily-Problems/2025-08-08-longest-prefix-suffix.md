# 📝 Problem: Longest Prefix Suffix


---

## 📜 Problem Statement
Given a string `s` consisting of lowercase English alphabets, find the **length of the longest prefix** which is also a **suffix**.  

> **Note:** Prefix and suffix can be overlapping but should not be equal to the entire string.

---

## 📥 Input
- A single string `s`.

---

## 📤 Output
- An integer representing the length of the longest prefix that is also a suffix.

---

## 🔍 Examples
```text
### Example 1:
**Input:**
abab

**Output:**

2

**Explanation:** The string `"ab"` is the longest prefix and suffix.

---

### Example 2:
**Input:**

aabcdaabc

**Output:**

4
**Explanation:** The string `"aabc"` is the longest prefix and suffix.
```


## 📚 Constraints
- `1 ≤ s.length ≤ 10^6`
- `s` contains only lowercase English alphabets.

---

## 🛠 Algorithm

1. **Initialize** an array `lps[]` of length `n` (where `n = len(s)`) to store the longest prefix-suffix values for each index.
2. Use two pointers:
   - `len` → tracks the current longest prefix length.
   - `i` → iterates through the string starting from index 1.
3. If characters match:
   - Increase `len` by 1.
   - Store it in `lps[i]` and increment `i`.
4. If characters don’t match:
   - If `len != 0`, update `len` to `lps[len - 1]`.
   - Else, set `lps[i] = 0` and move `i` forward.
5. Return the last value in `lps` array as the result.

---

## ⏳ Time & Space Complexity
- **Time Complexity:** `O(n)` — Single pass using KMP preprocessing.
- **Space Complexity:** `O(n)` — For storing the LPS array.

---

## 💻 Code Implementation (Python)
```python
class Solution:
    def getLPSLength(self, s):
        n = len(s)
        lps = [0] * n
        length = 0  # length of the previous longest prefix suffix
        i = 1

        while i < n:
            if s[i] == s[length]:
                length += 1
                lps[i] = length
                i += 1
            else:
                if length != 0:
                    length = lps[length - 1]
                else:
                    lps[i] = 0
                    i += 1

        return lps[-1]
```
---
## 🎯 Applications
- **Pattern Matching** — Used in KMP (Knuth–Morris–Pratt) algorithm for efficient substring search.
- **Data Compression** — Detect repeated patterns to reduce storage.
- **Bioinformatics** — DNA/RNA sequence alignment detection.
- **Plagiarism Detection** — Identify repeated patterns in text.
- **String Periodicity Checks** — To find smallest repeating units in a string.
---
`#StringMatching`, `#KMPAlgorithm`, `#PrefixSuffix`, `#PatternDetection`, `#StringProcessing`, `#InterviewPrep`, `#HardProblems`
