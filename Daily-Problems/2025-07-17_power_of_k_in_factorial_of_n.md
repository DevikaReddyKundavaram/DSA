# 🧑‍💻 DSA Daily Problem - Power of K in Factorial of N

## 🗓️ Date: 2025-07-17  
## 🚦 Difficulty: Medium  
## 🏆 Points: 4  

---

## 📄 Problem Statement:
Given two positive integers **n** and **k**, determine the highest value of **x** such that **k^x** divides **n!** (n factorial) completely.

---

### 🔢 Examples:

#### Example 1:
**Input:**  
n = 7, k = 2  
**Output:**  
4  
**Explanation:**  
7! = 5040, and 2^4 = 16 is the highest power of 2 that divides 5040.

#### Example 2:
**Input:**  
n = 10, k = 9  
**Output:**  
2  
**Explanation:**  
10! = 3628800, and 9² = 81 is the highest power of 9 that divides 3628800.

---

## 📌 Constraints:
# 🧑‍💻 DSA Daily Problem - Power of K in Factorial of N

## 🗓️ Date: 2025-07-17  
## 🚦 Difficulty: Medium  
## 🏆 Points: 4  

---

## 📄 Problem Statement:
Given two positive integers **n** and **k**, determine the highest value of **x** such that **k^x** divides **n!** (n factorial) completely.

---

### 🔢 Examples:

#### Example 1:
**Input:**  
n = 7, k = 2  
**Output:**  
4  
**Explanation:**  
7! = 5040, and 2^4 = 16 is the highest power of 2 that divides 5040.

#### Example 2:
**Input:**  
n = 10, k = 9  
**Output:**  
2  
**Explanation:**  
10! = 3628800, and 9² = 81 is the highest power of 9 that divides 3628800.

---

## 📌 Constraints:
# 🧑‍💻 DSA Daily Problem - Power of K in Factorial of N

## 🗓️ Date: 2025-07-17  
## 🚦 Difficulty: Medium  
## 🏆 Points: 4  

---

## 📄 Problem Statement:
Given two positive integers **n** and **k**, determine the highest value of **x** such that **k^x** divides **n!** (n factorial) completely.

---

### 🔢 Examples:

#### Example 1:
**Input:**  
n = 7, k = 2  
**Output:**  
4  
**Explanation:**  
7! = 5040, and 2^4 = 16 is the highest power of 2 that divides 5040.

#### Example 2:
**Input:**  
n = 10, k = 9  
**Output:**  
2  
**Explanation:**  
10! = 3628800, and 9² = 81 is the highest power of 9 that divides 3628800.

---

## 📌 Constraints:
1 ≤ n ≤ 10^5
2 ≤ k ≤ 10^5


---

## ✅ Approach:
- Factorize **k** into its prime factors.
- Count the total number of occurrences of each prime factor in **n!**.
- The answer is the **minimum of (count of p in n! / exponent in k)** for each prime factor **p**.

---

## 🔥 Solution (Python):

```python
class Solution:
    def maxKPower(self, n, k):
        def prime_factors(k):
            factors = {}
            d = 2
            while d * d <= k:
                count = 0
                while k % d == 0:
                    count += 1
                    k //= d
                if count:
                    factors[d] = count
                d += 1
            if k > 1:
                factors[k] = 1
            return factors
        
        def count_p_in_factorial(n, p):
            count = 0
            power = p
            while power <= n:
                count += n // power
                power *= p
            return count
        
        factors = prime_factors(k)
        res = float('inf')
        for p in factors:
            count_in_fact = count_p_in_factorial(n, p)
            max_power = count_in_fact // factors[p]
            res = min(res, max_power)
        return res
```
## 🚀 Applications:
- **Competitive Programming:**  
  Problems involving factorials and divisibility frequently appear in contests like Codeforces, CodeChef, and LeetCode.

- **Mathematical Problem Solving:**  
  Strengthens understanding of number theory, especially related to prime factors, combinatorics, and factorial properties.

- **Algorithm Design:**  
  Demonstrates efficient handling of repeated operations (counting factors, etc.), which is crucial for building optimized algorithms.

- **Software Development / AI / Data Science:**  
  Useful in building modules for combinatorics, permutations, statistical models, and probabilistic systems.

- **Interview Preparation:**  
  Helps develop a deeper understanding of prime numbers, factorial behavior, and related optimizations, which are common in technical interviews.

## 🏷️ Tags:
- `#Mathematics`
- `#NumberTheory`
- `#PrimeFactorization`
- `#Factorials`
- `#CompetitiveProgramming`
- `#Combinatorics`
- `#Optimization`
- `#AlgorithmicThinking`
- `#CodingInterviews`
