---
title: Python - QUIZZ 
layout: default
---

basic array manipulation techniques that are commonly required in technical interviews.

### Quiz 1: Two Sum

Problem:
Given an array of integers nums and an integer target, return the indices of the two numbers such that they add up to target.

Example:

    Input: nums = [2, 7, 11, 15], target = 9
    Output: [0, 1]

Solution:
```python
def two_sum(nums, target):
    num_dict = {}
    for i, num in enumerate(nums):
        complement = target - num
        if complement in num_dict:
            return [num_dict[complement], i]
        num_dict[num] = i

# Test the function
print(two_sum([2, 7, 11, 15], 9))  # Output: [0, 1]
```

Quiz 2: Reverse a String

Problem:
Write a function that reverses a string. The input string is given as an array of characters s.

Example:

    Input: s = ["h", "e", "l", "l", "o"]
    Output: ["o", "l", "l", "e", "h"]

Solution:

```python
def reverse_string(s):
    left, right = 0, len(s) - 1
    while left < right:
        s[left], s[right] = s[right], s[left]
        left += 1
        right -= 1

# Test the function
s = ["h", "e", "l", "l", "o"]
reverse_string(s)
print(s)  # Output: ["o", "l", "l", "e", "h"]
```

### Quiz 3: Move Zeroes

Problem:
Given an array nums, write a function to move all 0s to the end of it while maintaining the relative order of the non-zero elements.

Example:

    Input: nums = [0, 1, 0, 3, 12]
    Output: [1, 3, 12, 0, 0]

Solution:

```python
def move_zeroes(nums):
    last_non_zero_found_at = 0
    for i in range(len(nums)):
        if nums[i] != 0:
            nums[last_non_zero_found_at], nums[i] = nums[i], nums[last_non_zero_found_at]
            last_non_zero_found_at += 1

# Test the function
nums = [0, 1, 0, 3, 12]
move_zeroes(nums)
print(nums)  # Output: [1, 3, 12, 0, 0]
```

commonly tested in technical interviews:
* sliding window, 
* prefix products, and 
* interval merging

### Quiz 1: Longest Substring Without Repeating Characters

Problem:
Given a string s, find the length of the longest substring without repeating characters.

Example:

    Input: s = "abcabcbb"
    Output: 3 (The answer is "abc", with the length of 3)

```python
def length_of_longest_substring(s: str) -> int:
    char_set = set()
    left = 0
    result = 0

    for right in range(len(s)):
        while s[right] in char_set:
            char_set.remove(s[left])
            left += 1
        char_set.add(s[right])
        result = max(result, right - left + 1)

    return result

# Test the function
print(length_of_longest_substring("abcabcbb"))  # Output: 3
```

### Quiz 2: Product of Array Except Self

Problem:
Given an array nums of n integers where n > 1, return an array output such that output[i] is equal to the product of all the elements of nums except nums[i].

Example:

    Input: nums = [1,2,3,4]
    Output: [24,12,8,6]

Solution:

```python
def product_except_self(nums):
    length = len(nums)
    left_products = [1] * length
    right_products = [1] * length
    output = [1] * length

    for i in range(1, length):
        left_products[i] = left_products[i - 1] * nums[i - 1]

    for i in range(length - 2, -1, -1):
        right_products[i] = right_products[i + 1] * nums[i + 1]

    for i in range(length):
        output[i] = left_products[i] * right_products[i]

    return output

# Test the function
print(product_except_self([1, 2, 3, 4]))  # Output: [24, 12, 8, 6]
```

### Quiz 3: Merge Intervals

Problem:
Given a collection of intervals, merge all overlapping intervals.

Example:

    Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
    Output: [[1,6],[8,10],[15,18]]

Solution:

```python
def merge_intervals(intervals):
    intervals.sort(key=lambda x: x[0])
    merged = []

    for interval in intervals:
        if not merged or merged[-1][1] < interval[0]:
            merged.append(interval)
        else:
            merged[-1][1] = max(merged[-1][1], interval[1])

    return merged

# Test the function
print(merge_intervals([[1, 3], [2, 6], [8, 10], [15, 18]]))  # Output: [[1, 6], [8, 10], [15, 18]]
```


