# 🌀 Max Circular Subarray Sum

## 🧩 Problem Statement

Given a **circular array** `arr[]` of integers, find the **maximum possible sum** of a non-empty subarray.  
In a circular array, a subarray can **wrap around** from the end to the beginning.

---

## 📝 Input

- A list `arr[]` of integers, where `1 ≤ arr.length ≤ 10⁵`  
- Each element `arr[i]` lies in the range `-10⁴ ≤ arr[i] ≤ 10⁴`

---

## 🎯 Output

- Return a single integer: the **maximum sum of a non-empty subarray**, considering both circular and non-circular possibilities.

---

## 🔍 Examples

### Example 1

**Input:**
```python
arr = [8, -8, 9, -9, 10, -11, 12]```

**Output:**
22
---

## ⚙️ Algorithm

We consider two types of subarrays:
1. **Normal (Non-Wrapping)**: Apply **Kadane’s Algorithm** to find the max subarray sum.
2. **Wrapping**:  
   - Total sum of array: `total_sum`  
   - Min subarray sum: Use Kadane’s algorithm on inverted array to find min subarray  
   - Max circular sum = `total_sum - min_subarray_sum`  
   - This gives max subarray **that wraps** around.

Finally, compare both:
```python
result = max(max_kadane, total_sum - min_subarray)

## 🧠 Python Code

```python
class Solution:
    def maxCircularSum(self, arr):
        def kadane(nums):
            max_ending = max_so_far = nums[0]
            for x in nums[1:]:
                max_ending = max(x, max_ending + x)
                max_so_far = max(max_so_far, max_ending)
            return max_so_far

        total_sum = sum(arr)
        max_kadane = kadane(arr)

        # Invert elements to find the minimum subarray sum
        inverted_arr = [-x for x in arr]
        max_inverted = kadane(inverted_arr)
        max_wrap = total_sum + max_inverted  # Equivalent to total_sum - (-min_sum)

        if max_wrap == 0:
            return max_kadane  # All numbers are negative

        return max(max_kadane, max_wrap)
```
## 💡 Applications

The **Max Circular Subarray Sum** problem has several practical applications, especially where data is **cyclical or wraps around**. Some real-world use cases include:

- 🎧 **Audio Signal Processing**: Identifying peaks and patterns in cyclic waveforms.
- 🔁 **Circular Buffers / Ring Buffers**: Useful in real-time systems like audio/video streams, task queues, and OS kernels.
- 📶 **Network Traffic Analysis**: Monitoring periodic bursts of traffic and calculating peak loads.
- 🧠 **Pattern Recognition**: In time-series data (e.g., stock prices or sensor data) that behaves cyclically.
- 🕹️ **Gaming/Simulation**: Optimizing game loops, energy levels, or health bars that reset cyclically.
- ⌛ **Scheduling Algorithms**: Finding optimal windows in circular schedules like rotating shifts or calendars.
- 🚀 **Embedded Systems**: Where memory is constrained, circular data structures are often used.


## 🔖 Tags

- `#KadaneAlgorithm`
- `#CircularArray`
- `#DynamicProgramming`
- `#SubarraySum`
- `#ArrayAlgorithms`
- `#SlidingWindow`
- `#MaxSubarray`
- `#CompetitiveProgramming`
- `#InterviewPrep`



