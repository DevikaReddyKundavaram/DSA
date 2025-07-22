
# Smallest Positive Missing Number

## Problem Statement
Given an array `arr[]` of integers, find the **smallest positive number** missing from the array.

**Note:** Positive numbers start from 1. The array can contain negative numbers and zero.

---

## Input
- An array `arr[]` of size `n` where `1 ≤ n ≤ 10^5`
- Array elements range from `-10^6` to `10^6`

### Example Input:
```
arr[] = [2, -3, 4, 1, 1, 7]
```

## Output
- Return the **smallest positive number** missing from the array.

### Example Output:
```
3
```

---

## Algorithm
1. Iterate through the array and for every valid number `x` such that `1 <= x <= n`, place it at index `x-1` using swapping.
2. After arranging, iterate again through the array.
3. The first index `i` where `arr[i] != i + 1` indicates that the missing number is `i + 1`.
4. If all indices satisfy `arr[i] = i + 1`, then the missing number is `n + 1`.

---

## Time and Space Complexities
- **Time Complexity:** `O(N)` (Each element is swapped at most once.)
- **Space Complexity:** `O(1)` (In-place swapping, no extra space.)

---

## Python Code
```python
class Solution:
    def missingNumber(self, arr):
        n = len(arr)
        for i in range(n):
            while 1 <= arr[i] <= n and arr[arr[i] - 1] != arr[i]:
                correct_idx = arr[i] - 1
                arr[i], arr[correct_idx] = arr[correct_idx], arr[i]
        for i in range(n):
            if arr[i] != i + 1:
                return i + 1
        return n + 1
```

### Sample Usage
```python
sol = Solution()
print(sol.missingNumber([2, -3, 4, 1, 1, 7]))  # Output: 3
print(sol.missingNumber([5, 3, 2, 5, 1]))      # Output: 4
print(sol.missingNumber([-8, 0, -1, -4, -3]))  # Output: 1
```

---

## Applications
- Detecting missing numbers in datasets
- Data validation tasks in software engineering
- Finding missing IDs in sequences (e.g., tickets, user IDs)
- Competitive programming

---

## Tags
`Array`, `Index Mapping`, `Sorting`, `Missing Number`, `Placement Sort`, `Cyclic Sort`, `In-place Algorithm`
