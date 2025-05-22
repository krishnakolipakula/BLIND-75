# 📘 Explanation.md – Leetcode 19: Remove Nth Node From End of List

## 🧩 Problem Summary

> Given the head of a linked list, remove the nth node from the **end** of the list and return its head.

---

## 💡 Approach Used

This solution uses **two traversals** of the linked list:

### ✅ Step-by-step Explanation:

1. **Count the length** of the linked list:
   - Start with a `temp` pointer at the head and loop through until the end, incrementing a counter `i`.
   - This gives the total length of the list.

2. **Calculate the position to delete from the start:**
   - The position from the start = `i - n + 1` (where `i` is the total number of nodes).

3. **Edge cases:**
   - If the list has only one node, return `None`.
   - If the head itself needs to be removed (i.e., `k == 1`), return `head.next`.

4. **Traverse again to remove the node:**
   - Use two pointers: `temp1` to reach the node to be deleted, and `temp2` to keep track of the previous node.
   - Skip the `k-th` node by changing the `next` pointer of `temp2`.

---

## 🧠 Intuition

To remove the nth node from the end, we need to know how far that is from the beginning. Counting the nodes gives us that offset. Then we delete the node at that position.

---

## 🧪 Code

```python
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        temp = head
        i = 1

        # Step 1: Count the length of the list
        while temp.next != None:
            temp = temp.next
            i += 1

        # Step 2: Calculate position from the beginning
        k = i - n + 1

        temp1 = head

        # Step 3: Edge case - only one node
        if i == 1:
            head = None
            return head

        # Step 4: Edge case - delete head
        elif k == 1:
            head = head.next
            return head

        # Step 5: Traverse again and delete k-th node
        else:
            j = 1
            temp2 = head
            while j != k:
                temp2 = temp1
                temp1 = temp1.next
                j += 1
            temp2.next = temp1.next
            return head
```

---

## ⏱️ Time & Space Complexity

| Type               | Complexity |
|--------------------|------------|
| 🕒 Time             | O(L) + O(L) = O(L)       |
| 💾 Space            | O(1)       |

Where `L` is the number of nodes in the list.

---

## ⚠️ Notes

- This is a **two-pass approach**: one to count, another to delete.
- A more optimal approach exists using **fast and slow pointers** in a single pass.
- This code avoids using a dummy node but handles edge cases manually.

---

## 🏷️ Tags

- `Linked List`
- `Two Pass`
- `Basic Pointer Manipulation`
- `Medium`

---
✅ Handles edge cases like removing the first or only node  
✅ Clean separation of steps for understanding  
🚫 Not optimal (can be improved using one-pass dummy node approach)
```
