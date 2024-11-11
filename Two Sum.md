# 🧮 Two Sum Solution

**[View Problem on LeetCode](https://leetcode.com/problems/two-sum/description/)**

## 📝 Problem Description
Given an array of integers `nums` and an integer `target`, find the indices of two numbers that add up to `target`.

### Constraints
- Only one solution exists for each input.
- Do not use the same element twice.

## 📊 Examples

| Example | Input                  | Output | Explanation                                |
|---------|-------------------------|--------|--------------------------------------------|
| 1       | `nums = [2,7,11,15]`<br>`target = 9`  | `[0,1]` | `nums[0] + nums[1] == 9`                  |
| 2       | `nums = [3,2,4]`<br>`target = 6`      | `[1,2]` | `nums[1] + nums[2] == 6`                  |
| 3       | `nums = [3,3]`<br>`target = 6`        | `[0,1]` | `nums[0] + nums[1] == 6`                  |

---

## 🚀 Solution Code

Here’s the Python solution for the Two Sum problem:

```python
class Solution(object):
    def twoSum(self, nums, target):
        indices = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in indices:
                return [indices[complement], i]
            indices[num] = i

## 🔍 Explanation

1. **Initialize a Dictionary**: A dictionary (`num_map`) keeps track of each number and its index as we loop through the list.
2. **Loop through the Array**: For each number in `nums`, compute its `complement` as `target - num`.
3. **Check if Complement Exists**: If `complement` is in `num_map`, the two numbers add up to `target`, so return their indices.
4. **Update the Dictionary**: If the complement isn’t found, store the current number and its index in `num_map`.

### Complexity Analysis
- **Time Complexity**: O(n), where n is the length of `nums`, as each element is only looked up or added to the dictionary once.
- **Space Complexity**: O(n), for storing elements in the dictionary.

---
