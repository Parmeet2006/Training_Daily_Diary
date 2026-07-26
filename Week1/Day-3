# 📅 Day 3: Python Memory Architecture & Data Structures

**Date:** June 26, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 3`

---

## 🎯 Overview & Objectives

In today's session, we explored how Python handles memory allocation under the hood and compared **Single Value Containers (SVCs)** with **Multi Value Containers (MVCs)**. Understanding reference copying, hashing mechanisms, and data structure schemas is essential for designing structured context payloads and tool-calling models in Agentic AI.

---

## 🧠 Key Concepts Covered

### 1. Memory Allocation & Reference Mechanics
* **Single Value Containers (SVCs):** Python uses integer interning and caching. Immutable objects with identical values share memory addresses (`id()`).
* **Reference Copying:** Assigning a container variable to another (`b = a` or `numbers = data`) passes the memory reference, not a deep copy. Modifying one reflects in both.
* **Re-allocation:** Creating new bracketed values (`data = [...]`) allocates a distinct block in RAM with a new `id()`.

### 2. Multi Value Containers Comparison
* **List (`[]`):** Ordered, index-based, mutable, and allows duplicate elements.
* **Set (`set()`):** Unordered, uses **Hashing** internally, automatically removes duplicate items, and does not support positional indexing.
* **Dictionary (`{}`):** Holds key-value pairs. Keys are unique (using hashing algorithms), while values can be duplicate or deeply nested.

### 3. Practical Data Modeling
* Built real-world schemas using nested dictionaries to represent e-commerce catalogs, food menus, and chat application message payloads.
