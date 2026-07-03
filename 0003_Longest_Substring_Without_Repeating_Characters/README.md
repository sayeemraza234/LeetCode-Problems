# LeetCode Solutions

This repository contains my solutions to LeetCode problems along with explanations and approaches.


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

