```markdown
# 🧠 Problem 143: Reorder List

**Difficulty:** Medium  
**Tags:** Linked List, Two Pointers, Stack, Recursion  
**Companies:** Facebook, Amazon, Apple, Google, Microsoft

---

## 📘 Problem Statement

You are given the head of a singly linked list. The list can be represented as:

```
L0 → L1 → … → Ln - 1 → Ln
```

Reorder the list to be in the following form:

```
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
```

You may **not** modify the values in the list's nodes. Only the **nodes themselves** may be changed.

---

## 🧪 Examples

### Example 1
**Input:**  
`head = [1,2,3,4]`  
**Output:**  
`[1,4,2,3]`  

### Example 2
**Input:**  
`head = [1,2,3,4,5]`  
**Output:**  
`[1,5,2,4,3]`

---

## 📏 Constraints

- The number of nodes in the list is in the range `[1, 5 * 10^4]`.
- `1 <= Node.val <= 1000`

---

## 💡 Explanation

To reorder the list as specified:

1. Find the **middle** of the linked list using the **slow and fast pointer** approach.
2. Reverse the **second half** of the list.
3. Merge the **two halves**, alternating nodes from each part.

We **do not modify values**, only node pointers.

---

## 🧭 Step-by-Step Approach

1. **Find the middle node:**
   - Use slow and fast pointers to reach the middle.
2. **Reverse the second half:**
   - Starting from the node after the middle, reverse pointers till the end.
3. **Merge two halves:**
   - Alternately connect one node from the first half, then one from the reversed second half.

---

## 🧑‍💻 Python Code

```python
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reorderList(self, head: ListNode) -> None:
        """
        Do not return anything, modify head in-place instead.
        """

        # Step 1: Find the middle of the list
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Step 2: Reverse second half
        prev, curr = None, slow.next
        slow.next = None  # Cut the list into two halves
        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt

        # Step 3: Merge two halves
        first, second = head, prev
        while second:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first, second = tmp1, tmp2
```

---

## ✅ Test Code

```python
# Helper functions for testing
def build_linked_list(values):
    head = ListNode(values[0])
    curr = head
    for val in values[1:]:
        curr.next = ListNode(val)
        curr = curr.next
    return head

def linked_list_to_list(head):
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result

# Test
input_list = [1, 2, 3, 4, 5]
head = build_linked_list(input_list)
Solution().reorderList(head)
print(linked_list_to_list(head))  # Output: [1, 5, 2, 4, 3]
```

---

## ⏱️ Time and Space Complexity

- **Time Complexity:** `O(N)`
  - Finding the middle: `O(N)`
  - Reversing second half: `O(N)`
  - Merging: `O(N)`
- **Space Complexity:** `O(1)` (In-place reordering; no extra space used except for pointers)

---

## 🏷️ Tags

`Linked List` `Two Pointers` `Stack` `In-place Algorithm` `Recursion`
```
