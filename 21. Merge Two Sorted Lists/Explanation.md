# 🔗 Leetcode 21 - Merge Two Sorted Lists

## 🧩 Problem Statement
You are given the heads of two sorted linked lists `list1` and `list2`.  
Merge the two lists into a single sorted linked list by **splicing** their nodes (not creating new ones).  
Return the **head** of the merged linked list.

---

## ✅ Explanation

This is a classic **Linked List merging** problem, similar to the merge step in merge sort.

We’ll use a **dummy node** to simplify edge cases and maintain a `current` pointer to track the last node added.

---

## 🧱 Step-by-Step Approach

### 🔹 Step 1: Create a Dummy Node
```python
dummy = ListNode()
cur = dummy
```
- `dummy` acts as a placeholder for the head of the merged list.
- `cur` is used to build the merged list by appending smaller nodes.

---

### 🔹 Step 2: Traverse Both Lists
```python
while list1 and list2:
    ...
```
- Continue while both lists have nodes left.

---

### 🔹 Step 3: Compare and Append
```python
if list1.val > list2.val:
    cur.next = list2
    list2 = list2.next
else:
    cur.next = list1
    list1 = list1.next
cur = cur.next
```
- Choose the smaller node and append it to `cur.next`.
- Move the chosen list's pointer forward.
- Advance `cur` to keep building.

---

### 🔹 Step 4: Append Remaining Nodes
```python
if list1:
    cur.next = list1
else:
    cur.next = list2
```
- One of the lists might still have nodes left — append it directly.

---

### 🔹 Step 5: Return the Result
```python
return dummy.next
```
- `dummy.next` points to the head of the merged list.

---

## 🧪 Example Walkthrough

### Input:
```
list1 = [1, 2, 4]
list2 = [1, 3, 4]
```

### Output:
```
[1, 1, 2, 3, 4, 4]
```

### How?
- Compare 1 and 1 → add 1
- Compare 2 and 1 → add 1
- Compare 2 and 3 → add 2
- Compare 4 and 3 → add 3
- Compare 4 and 4 → add 4
- list2 ends → append remaining 4 from list1

---

## ⏱️ Time and Space Complexity

| Type               | Complexity |
|--------------------|------------|
| 🕒 Time Complexity  | O(n + m)   | where n and m are lengths of list1 and list2 |
| 💾 Space Complexity | O(1)       | Only pointers used — no extra data structures |

---

## 🏷️ Tags

- `Linked List`
- `Merge Sort`
- `Two Pointer`
- `Dummy Node`
- `Sorting Logic`

---

## 📌 Summary

- ✅ Simple and elegant use of a dummy node
- ✅ Efficient and memory-friendly
- ✅ Preserves input list nodes — no unnecessary memory allocation

A must-know technique for many linked list and sorting problems! 🧠
```
