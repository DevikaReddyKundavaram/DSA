# Cutting Binary String 🔥

---

## Problem Statement 📄
You are given a binary string `s` consisting only of characters `'0'` and `'1'`.  
Split this string into the **minimum number of non-empty substrings** such that:  
✅ Each substring represents a **power of 5** in decimal.  
✅ No substring should have **leading zeros**.

If it's impossible to split, return `-1`.

---

## 🔥 Dry Run Example

### Input: `s = "101101101"`

Binary indexes:

### Step-by-step:

| i  | Substring `s[j:i]` | Decimal | Power of 5? | dp[i] Update |
|----|---------------------|---------|-------------|-------------|
| 1  | `1`                 | 1       | ✅           | `dp[1] = 1` |
| 3  | `101`               | 5       | ✅           | `dp[3] = 1` |
| 6  | `101` (3-6)         | 5       | ✅           | `dp[6] = dp[3] + 1 = 2` |
| 9  | `101` (6-9)         | 5       | ✅           | `dp[9] = dp[6] + 1 = 3` |

Final `dp = [0, 1, inf, 1, inf, inf, 2, inf, inf, 3]`  
Answer: `3`

---

## ⏳ Time & Space Complexities

| Type   | Complexity |
|--------|------------|
| **Time Complexity**   | `O(n^2)`  |
| **Reason:** For each `i`, we check all substrings `s[j:i]`. Each substring takes O(1) for `is_power_of_five`. |
| **Space Complexity**  | `O(n)`    |
| **Reason:** DP array of size `n+1` to store minimum cuts. |

---


## 👨‍💻 Code (Python)

```python
class Solution:
    def cuts(self, s):
        n = len(s)
        dp = [float('inf')] * (n + 1)
        dp[0] = 0

        def is_power_of_five(sub):
            if not sub or sub[0] == '0':
                return False
            num = int(sub, 2)
            if num == 0:
                return False
            while num % 5 == 0:
                num //= 5
            return num == 1

        for i in range(1, n + 1):
            for j in range(i):
                if is_power_of_five(s[j:i]):
                    dp[i] = min(dp[i], dp[j] + 1)

        return dp[n] if dp[n] != float('inf') else -1
```


## 🚀 Real-World Applications

### 🔹 Binary Data Segmentation
In **data transmission** (networking, protocols, compression), binary strings often represent data chunks. Efficiently splitting them into meaningful patterns (e.g., fixed factors like powers of 5) can help in **data parsing, encoding validation, or error detection**.

### 🔹 Compiler Design / Tokenization
Languages that compile down to **binary or bytecode** often need to validate or segment binary sequences based on mathematical properties. This is relevant in **lexical analysis** and **token validation** phases.

### 🔹 Cryptography
Certain cryptographic protocols use **binary sequences tied to mathematical properties** (e.g., primes, powers). Validating substrings through such properties ensures **data integrity and correctness** during encryption/decryption.

### 🔹 Embedded Systems / IoT
Binary strings often represent control signals. In some systems, these signals follow patterns related to **specific powers or multiples** for simplification (power-of-2, power-of-5), used in **protocol parsing, power-efficient encoding**.

### 🔹 Error Detection in File Formats
Binary file formats (audio, video, images) may structure data in chunks that align to **certain power patterns** for compatibility or optimization reasons. Validating these splits ensures file consistency.

### 🔹 Communication Protocols
Protocols sometimes break payloads into specific **binary lengths with mathematical constraints** (e.g., power-of-5 blocks for padding or synchronization).

---

## 🔖 Tags

- Dynamic Programming (DP)
- Binary Strings
- Substring Problems
- Bit Manipulation
- Number Theory (Powers of 5)
- String Processing
- Mathematical Validation
- Competitive Programming
