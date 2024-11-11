[**View Problem on LeetCode**](https://leetcode.com/problems/two-sum/description/)

```markdown
# Two Sum Solution

### Problem Description
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers such that they add up to `target`.

- Each input is guaranteed to have exactly one solution.
- You may not use the same element twice.
- The answer can be returned in any order.

### Examples

#### Example 1
- **Input:** `nums = [2,7,11,15]`, `target = 9`
- **Output:** `[0,1]`
- **Explanation:** `nums[0] + nums[1] == 9`, so we return `[0, 1]`.

#### Example 2
- **Input:** `nums = [3,2,4]`, `target = 6`
- **Output:** `[1,2]`

#### Example 3
- **Input:** `nums = [3,3]`, `target = 6`
- **Output:** `[0,1]`

---

### Solution Code

Here's the Python solution for the Two Sum problem:

```python
def twoSum(nums, target):
    num_map = {}  # Dictionary to store value and its index
    
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_map:
            return [num_map[complement], i]
        num_map[num] = i
```

### Solution Explanation

1. **Initialize a Dictionary:** A dictionary (`num_map`) is used to store each number and its index as we iterate through the list.
2. **Iterate through `nums`:** For each number in `nums`, calculate its `complement` as `target - num`.
3. **Check for the Complement:** If `complement` is already in `num_map`, it means the current number and the number stored in `num_map` add up to `target`. In that case, return their indices.
4. **Update Dictionary:** If the complement isn’t found, store the current number with its index in `num_map` and continue.

This solution has a **time complexity of O(n)**, making it efficient for large lists.

---

### Usage

To run this code, copy the function into a Python file, and call `twoSum(nums, target)` with your desired inputs.
