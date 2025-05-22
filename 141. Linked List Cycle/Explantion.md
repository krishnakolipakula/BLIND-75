# 🚴‍♂️ Leetcode 141 - Linked List Cycle

## 🧩 Problem Statement
Given the `head` of a singly linked list, determine if the linked list has a **cycle** in it.

A cycle exists if following the `next` pointers leads you back to a previously visited node instead of `None`.

---

## ✅ Explanation

We use **Floyd’s Cycle Detection Algorithm** (also known as the **Tortoise and Hare Algorithm**) to solve this problem **without any extra memory**.

### 💡 Key Idea:
- Use two pointers:
  - `slow` moves **1 step** at a time.
  - `fast` moves **2 steps** at a time.
- If there is a cycle, the two pointers will eventually **meet**.
- If there's **no cycle**, the fast pointer will reach the end (`None`).

---

## 🧱 Step-by-Step Approach

### 🔹 Step 1: Edge Case Handling
```python
if head == None or head.next == None:
    return False
```
- If the list is empty or has only one node, it **can't** have a cycle.

---

### 🔹 Step 2: Initialize Pointers
```python
fast = head
slow = head
```
- Both `fast` and `slow` start at the head.

---

### 🔹 Step 3: Traverse the List
```python
while fast.next != None and fast.next.next != None:
```
- Keep looping **as long as** the fast pointer has two more steps to take.
- This ensures we don't get a `NoneType` error.

---

### 🔹 Step 4: Move Pointers
```python
fast = fast.next.next
slow = slow.next
```
- `fast` moves two steps.
- `slow` moves one step.

---

### 🔹 Step 5: Check for Meeting Point
```python
if fast == slow:
    return True
```
- If both pointers meet, a **cycle is detected**.

---

### 🔹 Step 6: If Loop Ends
```python
return False
```
- If the loop exits naturally, it means `fast` hit the end of the list — no cycle found.

---

## ⏱️ Time and Space Complexity

| Type               | Complexity |
|--------------------|------------|
| 🕒 Time Complexity  | O(n)       |
| 💾 Space Complexity | O(1)       |

- Only two pointers are used — no additional memory.
- In the worst case, every node is visited once.

---

## 🏷️ Tags

- `Linked List`
- `Two Pointer`
- `Floyd’s Cycle Detection`
- `Tortoise and Hare`
- `Cycle Detection`

---

## 📌 Summary

- ✅ Elegant solution using two pointers
- ✅ O(1) space — no extra data structures
- ✅ Efficient and handles all edge cases

Floyd’s algorithm is a classic and optimal method to detect cycles in linked structures — and your implementation nails it! 🔥
```
