# LeetCode Solutions

This repository contains my solutions to LeetCode problems along with explanations and approaches.

## Progress

| Problem No. | Problem Name | Difficulty | Language | Status |
|------------|--------------|------------|----------|--------|
| 3 | Longest Substring Without Repeating Characters | Medium | Python | ✅ Solved |

---

## Problem #3: Longest Substring Without Repeating Characters

### Approach
Used the Sliding Window technique with a HashMap (dictionary).

- Maintain a window of unique characters.
- Expand the right pointer.
- If a duplicate character is found, move the left pointer.
- Track the maximum window size.

### Complexity

- Time Complexity: O(n)
- Space Complexity: O(n)

### Performance

- Runtime: 15 ms
- Beats: 91.1%
- Memory: 12.5 MB
- Beats: 81.0%

### Solution

```python
class Solution:
    def lengthOfLongestSubstring(self, s):
        last_seen = {}
        left = 0
        max_len = 0

        for right, ch in enumerate(s):
            if ch in last_seen and last_seen[ch] >= left:
                left = last_seen[ch] + 1

            last_seen[ch] = right
            max_len = max(max_len, right - left + 1)

        return max_len