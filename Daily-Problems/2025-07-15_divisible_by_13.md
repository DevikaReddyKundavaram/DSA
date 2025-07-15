# 🔢 Problem: Divisible by 13

**Difficulty:** Medium  

---

## 📝 Problem Statement

Given a number represented as a **string `s` (which may be very large)**, check whether it is divisible by **13** or not.

### Constraints:
- 1 ≤ `s.length` ≤ 10⁵

---

## 🔍 Examples

### Input:
s = "2911285"
### Output:
True


### Input:
s = "27"
### Output:
False


---

## 💡 Approach

### Why not use direct integer conversion?
- In languages like **C++** or **Java**, numbers with 10⁵ digits would cause overflow.
- In **Python**, we could directly convert and compute, but in coding interviews/competitions, we avoid relying on Python-specific features.
- So, we compute the modulus manually.

### Algorithm:
1. Initialize `res = 0`
2. For each character `c` in string `s`:
    - `res = (res * 10 + int(c)) % 13`
3. If `res == 0`, then `s` is divisible by **13**.



## ⏱️ Time and Space Complexity

### ✅ Time Complexity: **O(N)**  
- We iterate through each digit in the string exactly **once**.
- Each iteration performs **constant time arithmetic operations**.
- Therefore, the overall time complexity is **O(N)**, where **N** is the length of the string.

---

### ✅ Space Complexity: **O(1)**
- We are only using a single variable `res` to store the modulus.
- No extra space is used that grows with input size.
- Hence, the space complexity is **O(1)**.

---
## 🧑‍💻 Python Solution

```python
def isDivisibleBy13(s):
    res = 0
    for c in s:
        res = (res * 10 + int(c)) % 13
    return res == 0
```


## 🌍 Real-World Applications

### 🔹 1. Financial Software (Validation)
- Large account numbers or transaction IDs (sometimes stored as strings) may require divisibility checks as part of **validation algorithms**.
- Example: Verifying if a transaction batch ID is compliant with internal rules (e.g., divisible by 13 for consistency).

---

### 🔹 2. Cryptography
- Cryptographic systems often work with very large numbers represented as strings.
- Modulus operations are common in **public-key encryption algorithms** and **digital signature verification**.

---

### 🔹 3. Data Integrity Checks
- Some data systems use modulus-based checksum techniques for error detection.
- This approach helps in verifying data integrity where IDs or keys are large numeric strings.

---

### 🔹 4. Competitive Programming / Technical Interviews
- Handling **large numbers as strings** and performing modular arithmetic is a common interview and contest problem.
- Helps assess understanding of numeric algorithms without relying on big integers.

---

### 🔹 5. Backend Systems (Unique Key Generation)
- Backend systems sometimes generate large, unique numerical identifiers stored as strings.
- Modulo checks (like % 13) might be used to distribute data across servers or partitions.

---

### ✅ **Why Important?**
These types of modulus operations on large string-represented numbers are foundational in:
- Building robust, language-agnostic software
- Designing efficient algorithms for large datasets
- Preparing for real-world edge cases in software systems


## 🔖 Tags
`#Strings`, `#Mathematics`, `#Modulo`, `#LargeNumbers`, `#NumberTheory`, `#CompetitiveProgramming`
