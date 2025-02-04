# Maximum Product Subarray 
LINK TO PROBLEM ( https://leetcode.com/problems/maximum-product-subarray/ )
## Problem Statement
**Given an integer array `nums`, find a subarray that has the largest product, and return the product.**

The test cases are generated so that the answer will fit in a **32-bit integer**.

---

## Examples

### Example 1:
```python
# Input
nums = [2,3,-2,4]
# Output
6
# Explanation: [2,3] has the largest product 6.
```

### Example 2:
```python
# Input
nums = [-2,0,-1]
# Output
0
# Explanation: The result cannot be 2, because [-2,-1] is not a subarray.
```

---

## Constraints
- `1 <= nums.length <= 2 * 10^4`
- `-10 <= nums[i] <= 10`
- The product of any subarray of `nums` is guaranteed to fit in a **32-bit integer**.

---

## Approach
To solve this problem efficiently, we can use **Dynamic Programming with Two Variables (Kadane’s Variation):**

1. **Track Two Variables:** Since the product can become negative, keep track of both **maximum product (`max_product`)** and **minimum product (`min_product`)**.
2. **Swap when encountering a negative number:** If `nums[i]` is negative, swap `max_product` and `min_product`.
3. **Update the products:** Compute the new `max_product` and `min_product` at each index.
4. **Keep track of the global maximum product.**

---

## Optimized Solution (Python)
```python
class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        pre,suf=1,1
        maxi=float(-inf)
        for i in range(len(nums)):
            if pre==0: pre=1
            if suf==0: suf=1
            pre*=nums[i]
            suf*=nums[len(nums)-i-1]
            maxi=max(maxi,max(suf,pre))
        return maxi
```

---

## Time & Space Complexity
- **Time Complexity:** `O(n)`, since we iterate through the array once.
- **Space Complexity:** `O(1)`, as we use only a few extra variables.

---

## Edge Cases Considered
✅ Arrays containing **zero** (e.g., `[0, -1, -2]`)<br>
✅ Arrays with **all negative numbers** (e.g., `[-1, -2, -3]`)<br>
✅ Arrays with **single elements** (e.g., `[5]` or `[-5]`)<br>
✅ Arrays where the maximum product subarray includes **negative numbers** (e.g., `[2, -3, -2, 4]`)

---

## Contributing
If you find a bug or have an improvement suggestion, feel free to **open an issue** or submit a **pull request**!

🚀 **Happy Coding!**

