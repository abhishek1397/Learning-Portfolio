# Hashing

**Hashing** is a technique used to **store and retrieve data efficiently**.

It maps a **key** (like a name or number) to an **index** in a hash table using a **hash function**.

> ⚙️ **Hashing = Hash Function + Collision Handling**

---

## 🔹 **1. Hash Function**

A **hash function** converts a key into an integer index (the location in the hash table).

A good hash function should:

* Distribute keys **uniformly** across the table
* Be **fast** to compute
* Minimize **collisions**

### Common Hashing Methods

| **Method**                | **Description**                                                            | **Example**                                       |
| ------------------------- | -------------------------------------------------------------------------- | ------------------------------------------------- |
| **Division Method**       | Uses remainder of division by table size.                                  | `h(k) = k % m`                                    |
| **Mid-Square Method**     | Square the key and extract middle digits.                                  | `k = 123 → k² = 15129 → middle = 12 → index = 12` |
| **Folding Method**        | Divide the key into parts, add them together, then mod by table size.      | `key = 123456 → (12+34+56) % m`                   |
| **Multiplication Method** | Multiply key by a constant (0 < A < 1), take fractional part × table size. | `h(k) = floor(m × (k × A mod 1))`                 |

---

## ⚠️ **2. Collision**

A **collision** happens when **two keys hash to the same index**.

Example:

```
Table size = 10
h(12) = 2
h(22) = 2
```

Both keys 12 and 22 want to go to index 2 → **collision!**

---

## 🔧 **3. Collision Resolution Techniques**

When collisions occur, we must decide **where to place the new key**.

### 🔸 A. **Open Addressing**

All elements are stored **in the hash table itself**.
If a collision occurs, find another **open (empty)** slot.

| **Method**            | **Description**                                             | **Probe Sequence**               |
| --------------------- | ----------------------------------------------------------- | -------------------------------- |
| **Linear Probing**    | Move linearly to the next slot until an empty one is found. | `h(k), h(k)+1, h(k)+2, ...`      |
| **Quadratic Probing** | Check slots in quadratic order.                             | `h(k)+1², h(k)+2², h(k)+3², ...` |
| **Double Hashing**    | Use a second hash function to determine step size.          | `h1(k) + i * h2(k)`              |

---

### 🔸 B. **Separate Chaining**

Each slot in the hash table contains a **linked list (or chain)**.
All elements that hash to the same index are stored in that list.

✅ Easy to implement
✅ No need to mark deleted slots
❌ Requires extra memory for linked lists

---

## 🧩 **Visual Summary**

```
           ┌────────────────────────────┐
           │          Hashing           │
           └────────────────────────────┘
                        │
           ┌────────────┴────────────┐
           │                         │
   ┌─────────────┐           ┌────────────────┐
   │ Hash Function│           │  Collision     │
   └─────────────┘           └────────────────┘
   │                                  │
   ▼                                  ▼
┌────────────────┐        ┌──────────────────────────┐
│ Division Method │        │   Open Addressing        │
│ Mid-Square      │        │     • Linear Probing     │
│ Folding         │        │     • Quadratic Probing  │
│ Multiplication  │        │     • Double Hashing     │
└────────────────┘        └──────────────────────────┘
                                │
                                ▼
                         Separate Chaining
```

---

## 📘 **Quick Recap**

| Concept               | Description                                        |
| --------------------- | -------------------------------------------------- |
| **Hash Function**     | Converts key → index                               |
| **Collision**         | Two keys map to same index                         |
| **Open Addressing**   | Store all keys in same array; probe for empty slot |
| **Separate Chaining** | Use linked lists at each index                     |
| **Probing Methods**   | Linear, Quadratic, Double Hashing                  |

---

Would you like me to show **code examples** for all three probing techniques — *linear*, *quadratic*, and *double hashing* — side by side for comparison?
