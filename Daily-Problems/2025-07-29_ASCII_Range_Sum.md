# 🧩 ASCII Range Sum

## 📝 Problem Statement

Given a string `s` consisting of lowercase English letters, for **every character** whose first and last occurrences are at **different positions**, calculate the **sum of ASCII values** of characters **strictly between** its first and last occurrence.

Return all such **non-zero sums**. The **order of the output doesn't matter**.

---

## 🔢 Input

- A string `s` of length `n` (1 ≤ n ≤ 10⁵)
- Only lowercase English letters

---

## 🎯 Output

- A list of non-zero ASCII sums for each applicable character.

---

## 🧪 Examples

### ✅ Example 1


```python
**Input:**
s = "abacab"

**Output:**
[293,294]
```
---
## ⚙️ Algorithm

1. **Initialize two dictionaries**:
   - `first_index`: to store the first occurrence of each character.
   - `last_index`: to store the last occurrence of each character.

2. **Traverse the string `s`**:
   - For each character `ch` at index `i`:
     - If `ch` is not in `first_index`, store `i` as its first occurrence.
     - Always update `last_index[ch]` to `i` (ensures it holds the last position).

3. **Iterate through all characters in `first_index`**:
   - For each character `ch`, get its `start = first_index[ch]` and `end = last_index[ch]`.
   - If `start != end`, compute the **ASCII sum** of characters strictly between:
     ```python
     total = sum(ord(s[i]) for i in range(start + 1, end))
     ```

4. **Add `total` to the result** list if it is non-zero.

5. **Return the list** of all such ASCII sums.

---

### 🔁 Example Flow

For `s = "abacab"`:
- 'a' occurs at index 0 and 5 → characters in between: `b`, `a`, `c` → ASCII = 98 + 97 + 99 = 294
- 'b' occurs at index 1 and 6 → characters in between: `a`, `c`, `a` → ASCII = 97 + 99 + 97 = 293
---
## ⏱️ Time & Space Complexities

### ⌛ Time Complexity: `O(n)`

- One pass to traverse the string and record first/last positions → `O(n)`
- One pass through each unique character (at most 26), and for each, a range sum over a substring → total at most `O(n)`
- Overall: **Linear time**

---

### 🧠 Space Complexity: `O(1)` (or `O(26)`)

- `first_index` and `last_index` dictionaries store only lowercase English letters → max 26 entries
- `result` list can store at most 26 ASCII sums
- Hence, considered **constant extra space** in terms of input size
---
## 💻 Code (Python)

```python
class Solution:
    def asciirange(self, s):
        first_index = {}
        last_index = {}

        # Step 1: Record first and last occurrence of each character
        for i, ch in enumerate(s):
            if ch not in first_index:
                first_index[ch] = i
            last_index[ch] = i  # always update to latest index

        result = []

        # Step 2: For each char with multiple occurrences, calculate ASCII sum between
        for ch in first_index:
            start = first_index[ch]
            end = last_index[ch]
            if start != end:
                total = sum(ord(s[i]) for i in range(start + 1, end))
                if total > 0:
                    result.append(total)

        return result
```
---
## 🌐 Applications

### 1. **Text Analysis & Processing**
- Useful in analyzing character positions, patterns, or frequency distributions in strings.
- Can be adapted for tasks like encryption, checksum verification, or detecting anomalies in sequences.

### 2. **Compiler Design / Lexical Analysis**
- Helps understand token boundaries by analyzing character ranges between repeated symbols or keywords.

### 3. **Pattern Matching & Substring Profiling**
- Core idea applies to problems involving range-based analysis of substrings between repeated characters.

### 4. **Hashing Techniques**
- The ASCII sum concept is often used in custom hash functions and character-weighted checksums.

### 5. **Bioinformatics (DNA/RNA sequence analysis)**
- Similar logic can be applied in analyzing repeated elements in genomic sequences where each character has a symbolic "weight".

### 6. **Palindromic / Symmetry Based Problems**
- Identifying character blocks between repeated instances aids in exploring symmetry or balance in strings.

---

## Tags

`#string` ,`#ascii`  ,`#hashing` ,`#character-counting`  ,`#range-query`  ,#`greedy`  ,`#dictionary`  ,`#two-pointer`  ,`#string-analysis`  ,`#simulation`
