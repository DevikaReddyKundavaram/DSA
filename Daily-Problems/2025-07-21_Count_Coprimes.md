
# 💡 Problem: Count the Coprimes  

---

## 🚩 Problem Statement  

You are given an array `arr[]` of positive integers.  
Your task is to count the number of pairs `(i, j)` such that:

- `0 ≤ i < j ≤ n-1`
- `gcd(arr[i], arr[j]) = 1`

In other words, count the number of unordered pairs of indices `(i, j)` where the elements at those positions are **co-prime**.

---

## 🔍 Examples

### Example 1  
**Input:**  
`arr = [1, 2, 3]`  
**Output:**  
`3`  

**Explanation:**  
Pairs: (0,1), (0,2), (1,2)  
All these pairs satisfy `gcd = 1`.

---

### Example 2  
**Input:**  
`arr = [4, 8, 3, 9]`  
**Output:**  
`4`  

**Explanation:**  
Pairs: (0,2), (0,3), (1,2), (1,3)

---

## 🔑 Algorithm / Approach  

### Core Idea:
- **Inclusion-Exclusion Principle:** Count how many previous numbers share prime factors with the current number.
- For every number, calculate all subsets of its prime factors.
- For each subset, use inclusion-exclusion to count how many previous numbers share any factors.
- Update counts of subsets for future elements.

### Steps:
1. For each number, find its unique **prime factors**.
2. Count how many previous numbers share any of its prime factors using subsets.
3. Apply inclusion-exclusion principle:  
   - Odd subset sizes: add count  
   - Even subset sizes: subtract count  
4. Update frequency map for future numbers.
5. If a number is `1`, it is coprime with all previous numbers.
---
## 📊 Time & Space Complexity

### 🕒 Time Complexity

| Step                          | Complexity        |
|--------------------------------|-------------------|
| Prime factorization per element | O(sqrt(num)) per element |
| Subsets of prime factors        | O(2^k) per element (k ≤ 4-5 on average) |
| Processing all `n` elements      | O(n * sqrt(max(arr))) |
| **Expected Overall**            | **O(n * sqrt(max(arr)))** |

---

### 🗃️ Space Complexity

| Usage               | Space    |
|----------------------|----------|
| Frequency Map        | O(max(arr)) |
| Subsets Storage      | O(k)      |
| **Total Space**      | **O(max(arr))** |

---

## ✅ Python Code  

```python
from collections import defaultdict
from math import isqrt
from itertools import combinations
from functools import reduce
from operator import mul

class Solution:
    def cntCoprime(self, arr):
        def prime_factors(x: int) -> list[int]:
            ret = []
            k = 2
            while k*k <= x:
                if x % k == 0:
                    ret.append(k)
                while x % k == 0:
                    x //= k
                k += 1
            if x > 1:
                ret.append(x)
            return ret
            
        cnt = defaultdict(int)
        ans = 0
        
        for i, e in enumerate(arr):
            if e == 1:
                ans += i
                continue
            
            primes = prime_factors(e)
            k = len(primes)
            
            shared = 0
            for r in range(1, k+1):
                for comb in combinations(primes, r):
                    prod = reduce(mul, comb, 1)
                    if r & 1:   
                        shared += cnt[prod]
                    else:     
                        shared -= cnt[prod]
            ans += i - shared
            
            for r in range(1, k+1):
                for comb in combinations(primes, r):
                    prod = reduce(mul, comb, 1)
                    cnt[prod] += 1
        return ans
```
## 🎯 Applications

- 🔐 **Cryptography:**  
  Analyzing coprime pairs is crucial for algorithms like RSA, where the concept of coprimeness is fundamental to key generation.

- 🧮 **Number Theory & Mathematics:**  
  Frequently used in problems involving Euler’s Totient Function, primitive roots, and understanding properties of numbers.

- 🏆 **Competitive Programming:**  
  Classic interview and coding competition problem type involving GCD, coprimes, and inclusion-exclusion logic.

- 📊 **Data Analysis / Algorithms:**  
  Useful for understanding data relationships based on divisibility and co-primality in databases or mathematical datasets.

---

## 🏷️ Tags

`#Mathematics`, `#NumberTheory`, `#GCD`, `#Coprime`, `#InclusionExclusion`, `#Bitmasking`, `#BruteForceOptimization`, `#PrimeFactorization`
