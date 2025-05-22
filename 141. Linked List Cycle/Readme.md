# 🔁 141. Linked List Cycle

**Difficulty:** Easy  
**Topics:** Linked List, Two Pointers, Hashing  
**Companies:** Amazon, Google, Microsoft, Facebook, Adobe

---

## 🧩 Problem Statement

Given the `head` of a singly linked list, determine if the list contains a **cycle**.

A cycle exists **if any node in the list is reachable again by continuously following the `next` pointer**. Internally, `pos` is used to denote the index of the node that the tail connects to. This is only for visualization — not part of the input.

🔁 **Return `true` if there is a cycle; otherwise, return `false`.**

---

## 📥 Examples

### Example 1:
```
Input: head = [3,2,0,-4], pos = 1  
Output: true  
Explanation: The tail connects to the 1st node (0-indexed), creating a cycle.
```

### Example 2:
```
Input: head = [1,2], pos = 0  
Output: true  
Explanation: The tail connects to the 0th node.
```

### Example 3:
```
Input: head = [1], pos = -1  
Output: false  
Explanation: There is no cycle.
```

---

## 📌 Constraints

- `0 <= number of nodes <= 10^4`
- `-10^5 <= Node.val <= 10^5`
- `pos` is `-1` or a valid index in the linked list (used for testing/visualization)

---






