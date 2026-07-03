## Problem #5: Longest Palindromic Substring

### Approach

Used the Expand Around Center technique.

- Every character can be the center of a palindrome.
- Check both odd-length and even-length palindromes.
- Expand outward while characters match.
- Track the longest palindrome found.

### Complexity

- Time Complexity: O(n²)
- Space Complexity: O(1)

### Examples

Input: "babad"

Output: "bab"

Note: "aba" is also a valid answer.

Input: "cbbd"

Output: "bb"

