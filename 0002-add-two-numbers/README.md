# 2. Add Two Numbers

## Problem Statement

You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit.

Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

---

### Example 1

Input:
```text
l1 = [2,4,3]
l2 = [5,6,4]
```

Output:
```text
[7,0,8]
```

Explanation:
```text
342 + 465 = 807
```

### Example 2

Input:
```text
l1 = [0]
l2 = [0]
```

Output:
```text
[0]
```

### Example 3

Input:
```text
l1 = [9,9,9,9,9,9,9]
l2 = [9,9,9,9]
```

Output:
```text
[8,9,9,9,0,0,0,1]
```

---

### Constraints

```text
The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
```

---

## Complexity Analysis

```text
Time Complexity: O(max(m, n))
Space Complexity: O(max(m, n))
```