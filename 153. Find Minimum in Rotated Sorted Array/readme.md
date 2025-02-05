# Find Minimum in Rotated Sorted Array (https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/description/)


## Problem Statement
**Given a sorted and rotated array `nums` of unique elements, return the minimum element of this array.**

You must write an algorithm that runs in **O(log n)** time.

---

## Examples

### Example 1:
```python
# Input
nums = [3,4,5,1,2]
# Output
1
# Explanation: The original array was [1,2,3,4,5] rotated 3 times.
```

### Example 2:
```python
# Input
nums = [4,5,6,7,0,1,2]
# Output
0
# Explanation: The original array was [0,1,2,4,5,6,7] and it was rotated 4 times.
```

### Example 3:
```python
# Input
nums = [11,13,15,17]
# Output
11
# Explanation: The original array was [11,13,15,17] and it was rotated 4 times.
```

---

## Constraints
- `n == nums.length`
- `1 <= n <= 5000`
- `-5000 <= nums[i] <= 5000`
- All the integers of `nums` are **unique**.
- `nums` is sorted and rotated between `1` and `n` times.

---

## Approach
To solve this problem efficiently in **O(log n) time**, we use **Binary Search**:

1. **Initialize Two Pointers:** `left = 0`, `right = len(nums) - 1`.
2. **Binary Search Condition:** While `left < right`:
   - Find the middle element: `mid = (left + right) // 2`
   - If `nums[mid] > nums[right]`, the minimum must be in the right half.
   - Otherwise, the minimum is in the left half.
3. **Return `nums[left]`** as the minimum element.

---

## Optimized Solution (Python)
```python
from typing import List

def findMin(nums: List[int]) -> int:
    left, right = 0, len(nums) - 1
    
    while left < right:
        mid = (left + right) // 2
        
        if nums[mid] > nums[right]:
            left = mid + 1
        else:
            right = mid
    
    return nums[left]
```

---

## Time & Space Complexity
- **Time Complexity:** `O(log n)`, as we apply binary search.
- **Space Complexity:** `O(1)`, as we use only a few extra variables.

---

## Edge Cases Considered
✅ Arrays with **no rotation** (e.g., `[1,2,3,4,5]`)<br>
✅ Arrays with **minimum at the end** (e.g., `[2,3,4,5,1]`)<br>
✅ Arrays with **only one element** (e.g., `[5]`)<br>
✅ Arrays where **minimum is the first element** (e.g., `[0,1,2,3]`)

---

## Contributing
If you find a bug or have an improvement suggestion, feel free to **open an issue** or submit a **pull request**!

🚀 **Happy Coding!**
