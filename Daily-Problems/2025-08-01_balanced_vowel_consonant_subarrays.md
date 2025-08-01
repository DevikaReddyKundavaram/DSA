# 🧮 Problem: Balancing Consonants and Vowels Ratio

  

---

## 📝 Problem Statement

You are given an array of strings `arr[]`, where each `arr[i]` consists of lowercase English alphabets.  
You need to find the number of **balanced strings** in `arr[]` which can be formed by **concatenating one or more contiguous strings** of `arr[]`.

A **balanced string** is a string where the **number of vowels equals the number of consonants**.

---

## 📥 Input

- `1 ≤ arr.length ≤ 10^5`
- `1 ≤ len(arr[i]) ≤ 10^5`
- Total number of characters in all strings of `arr[]` ≤ 10^5

---

## ✅ Examples

### Example 1:
```text
Input:  arr[] = ["aeio", "aa", "bc", "ot", "cdbd"]
Output: 4

Explanation: 
The balanced concatenations are:
1. arr[0..4]
2. arr[1..2]
3. arr[1..3]
4. arr[3..3]
```
###Example 2:
```text
Input:  arr[] = ["ab", "be"]
Output: 3

Explanation: 
The balanced substrings are:
1. arr[0..0]
2. arr[0..1]
3. arr[1..1]
```

---
## 🧠 Algorithm: Count Balanced Strings

We want to count how many **contiguous subarrays** of strings, when concatenated, result in equal number of **vowels and consonants**.

---

### 🔄 Step-by-Step Algorithm:

1. **Initialize**:
   - A function `get_balance(s)` that returns:
     ```
     balance = number of vowels - number of consonants
     ```
   - A prefix sum variable `prefix_sum = 0`
   - A counter `count = 0`
   - A hashmap `freq = {0: 1}` to store frequency of prefix sums

2. **Iterate through each string `s` in `arr[]`:**
   - Calculate `balance = get_balance(s)`
   - Update `prefix_sum += balance`
   - If `prefix_sum` has been seen before:
     - Add `freq[prefix_sum]` to `count` (valid subarrays ending here)
   - Update `freq[prefix_sum] += 1`

3. **Return** the final `count`

---

### 🔢 get_balance(s) Logic:

- Loop through characters in `s`
  - If character is a vowel (`a, e, i, o, u`), increment `v`
  - Else, it's a consonant: increment `c`
- Return `v - c` as the balance

---

### 🧮 Why It Works:

If the prefix sum up to index `j` equals prefix sum up to index `i-1`, then the total balance from `i` to `j` is zero — meaning **equal vowels and consonants**.

This is the **same trick** used in subarray sum problems like:
- "Count subarrays with sum = 0"
- "Longest subarray with equal 0s and 1s"

---
## ⏱️ Time & Space Complexity

### 🧮 Time Complexity:

- Let:
  - `N` = number of strings in `arr`
  - `M` = average length of each string
  - Total number of characters across all strings ≤ 10⁵

#### Step Breakdown:
| Step                             | Time Complexity     |
|----------------------------------|----------------------|
| Calculating balance for each string | O(M) per string (total O(N * M)) |
| Prefix sum + hashmap operations | O(N)                |
| **Total Time**                  | **O(N * M)**  
> Since total characters ≤ 10⁵, this is efficient in practice.

---

### 🧠 Space Complexity:

| Component                        | Space Used             |
|----------------------------------|-------------------------|
| HashMap (`freq`)                 | O(N) in worst case      |
| Balance calculation (temp vars)  | O(1)                    |
| **Total Space**                  | **O(N)**

---

### ✅ Summary:

| Complexity Type | Value       |
|-----------------|-------------|
| Time Complexity | O(N * M)    |
| Space Complexity| O(N)        |

---

## 💻 Python Code

```python
class Solution:
    def countBalanced(self, arr):
        def get_balance(s):
            vowels = set("aeiou")
            v = sum(1 for ch in s if ch in vowels)
            c = len(s) - v
            return v - c

        from collections import defaultdict

        prefix_sum = 0
        count = 0
        freq = defaultdict(int)
        freq[0] = 1  # For substrings starting from index 0

        for s in arr:
            balance = get_balance(s)
            prefix_sum += balance
            count += freq[prefix_sum]
            freq[prefix_sum] += 1

        return count

```
## 🚀 Applications

Understanding and solving the **Balanced Vowel-Consonant Subarray** problem strengthens your grasp on:

---

### 1. 🔄 Prefix Sum & Hashmap Technique
- A classic pattern in many array/string problems.
- Core concept in problems like:
  - Subarrays with Sum = K
  - Longest subarray with equal 0s and 1s
  - Number of subarrays with XOR = K
- Essential for coding interviews and CP.

---

### 2. 🧠 Balanced String Detection
- Useful in:
  - Language processing systems (detecting phonetic balance)
  - Linguistics research tools
  - Game mechanics (e.g., letter/word balance in word games)
  - Text compression or summarization (vowel/consonant analysis)

---

### 3. 📚 Subarray and Sliding Window Pattern Mastery
- Helps develop logic for:
  - Kadane’s Algorithm variants
  - Contiguous grouping & segment analysis
  - Efficient windowed processing of large data

---

### 4. 💼 Real-World Analogy
- Analyzing **balanced workloads** (e.g., task vs idle cycles)
- Equal distribution in **biological sequences** (like DNA base pairs)
- Signal processing with equal wave components (e.g., AC signal analysis)

---

### 5. 💬 Competitive Programming & Interviews
- Similar problems are frequent in platforms like:
  - LeetCode
  - Codeforces
  - HackerRank
  - Google/Amazon Interviews

---

### 📌 Summary:
This problem is more than just about vowels — it's about applying **prefix sum frequency counting** to solve **balance-based substring detection**, a powerful and common pattern in software development and AI preprocessing alike.

---
## 🏷️ Tags 
`prefix-sum`, `hashmap`, `subarray`, `balanced-strings`, `string-algorithms`, `frequency-counting`, `interview-prep`, `medium`, `optimization`, `vowel-consonant`, `sliding-window`


