## Problem #9: Palindrome Number

### Approach

Solved without converting the integer to a string.

- Negative numbers are never palindromes.
- Numbers ending in 0 (except 0 itself) cannot be palindromes.
- Reverse only half of the number.
- Compare the first half and reversed second half.

### Complexity

- Time Complexity: O(log₁₀ n)
- Space Complexity: O(1)

### Examples

Input: 121

Output: true

Input: -121

Output: false

Input: 10

Output: false

