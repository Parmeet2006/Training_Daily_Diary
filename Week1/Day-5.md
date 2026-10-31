# 📅 Day 5: Operators, Bitwise Mechanics, PEP 8 Standards, & Conditional Systems

**Date:** June 28, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 5`

---

## 🎯 Overview & Objectives

Session 5 focused on building decision-making logic and low-level data manipulation techniques in Python. We explored arithmetic and assignment operators, logical and membership mechanics, low-level bitwise bit-shifting, PEP 8 design standards, and nested conditional constructs applied to real-world promotional discount algorithms and algorithmic problem-solving.

---

## 🧠 Key Concepts & Learning Summary

### 1. Arithmetic & Assignment Operations
* Covered core arithmetic operations (`+`, `-`, `*`, `/`, `//`, `%`, `**`).
* Evaluated floor division (`//`) versus floating-point division (`/`), and exponentiation (`**`).
* Worked with compound assignment operators (`+=`, `-=`, `*=`, `/=`). Note: Inplace increment/decrement operators (`++`, `--`) are not supported in Python.

### 2. Logical, Conditional, & Membership Operators
* **Comparison Operators:** (`>`, `<`, `>=`, `<=`, `==`, `!=`) return Boolean flags.
* **Identity vs. Equality:** Explored the distinction between `==` (value comparison) and `is` (memory reference comparison).
* **Membership Operators:** Used `in` and `not in` to verify element presence inside sequences and dictionary keys.
* **Logical Operators:** Used `and`, `or`, and `not` for multi-condition authentication flows.

### 3. Bitwise Mechanics & Bit-Shifting Operations
* **Bitwise Logical Ops:** Explored `&` (AND), `|` (OR), and `^` (XOR) operations directly on binary registers.
* **Bit Shifting:**
  * **Left Shift (`<<`):** Multiplies numbers by powers of 2 ($N \times 2^k$).
  * **Right Shift (`>>`):** Performs floor division by powers of 2 ($\lfloor N / 2^k \rfloor$).
* **Signed Integer Bit Shifts:** Analyzed 2's complement arithmetic for negative numbers under right-shifts (e.g., `-11 >> 3` yields `-2`).

### 4. PEP 8 & Conditional Control Flow Architecture
* Applied [PEP 8 guidelines](https://peps.python.org/pep-0008/) for readable, standardized Python code formatting.
* Designed multi-layered validation logic using simple `if/else`, laddered `if/elif/else`, and nested conditions to evaluate business constraints (e.g., coupon code eligibility, cart threshold checks, and max discount capping).

---
