# 📅 Day 6: Modular Functions, Argument Flexibility (`*args`, `**kwargs`), Memory Passing Mechanics, & Recursion

**Date:** June 29, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 6`

---

## 🎯 Overview & Objectives

Session 6 covered the core foundations of functional programming in Python. We transitioned from writing repetitive code to creating reusable controllers through functions. Key topics included default arguments, reference copies, function overloading dynamics, dynamic variadic arguments (`*args` and `**kwargs`), call-by-value vs. call-by-reference memory behaviors, and recursive execution stacks.

---

## 🧠 Key Concepts & Learning Summary

### 1. Function Fundamentals & Reusability
* Functions encapsulate business logic to eliminate repetitive procedural blocks (e.g., extracting maximum values from lists).
* Functions in Python are **first-class objects**: they have unique memory addresses (`id()`), can be assigned to reference variables (`add = add_numbers`), passed around, or deleted (`del`).

### 2. Argument Flexibility & Overloading Behavior
* **Default Arguments:** Positional arguments without default values cannot follow default arguments (`def func(a, b=10)` is valid; `def func(a=10, b)` raises a SyntaxError).
* **Function Redefinition:** Python does not support traditional method overloading. Redefining a function with a matching name overwrites the previous definition in memory.
* **Variadic Arguments:**
  * `*args`: Collects extra positional arguments into an immutable **Tuple**.
  * `**kwargs`: Collects extra keyword arguments into a **Dictionary**.
  * Combining `(*args, **kwargs)` enables fully dynamic signature wrappers.

### 3. Pass-by-Value vs. Pass-by-Reference & Mutability
* **Immutable Types (Integers, Strings, Tuples):** Reassigning or modifying values inside a function creates a new memory allocation, leaving original caller scope variables intact.
* **Mutable Types (Lists, Dicts):** Modifying elements in place mutates the original reference passed from caller scope. To preserve original data, deep copies or manual duplicate lists (`my_numbers.append()`) must be instantiated.

### 4. Recursion Mechanics & Return Values
* **Recursion:** A function calling itself until reaching a termination base condition (`if number <= 10`).
* **Return Values:** Standardizes returning computation results back to the caller scope via the `return` keyword instead of printing directly inside controller blocks.

---
