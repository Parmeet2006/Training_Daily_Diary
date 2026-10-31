# 📅 Day 10: Real-World Queue Mechanics, FastTag Toll System, String Immutability, & Text Slicing

**Date:** July 03, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 10`

---

## 🎯 Overview & Objectives

Session 10 applied object-oriented design and linked structures to solve real-world system challenges[cite: 19, 20, 21]. We built a simulated **Toll Plaza Queue System** leveraging FastTag account integration and circular linked references[cite: 19, 20, 21]. Additionally, we conducted an in-depth exploration of **Python String Architecture**, focusing on memory immutability, negative indexing, advanced string slicing mechanics, and template formatting[cite: 22, 23].

---

## 🧠 Key Concepts & Learning Summary

### 1. Real-World Domain Composition (1-to-1 Mapping)
* **Entity Relations:** Embedded a `FastTag` object directly inside a `Vehicle` instance (`self.fasttag`), showcasing object composition[cite: 19, 21].
* **State Mutation:** Processed dynamic toll deductions against `FastTag` balances based on vehicle classification types (e.g., `4W` vs `2W`)[cite: 20].

### 2. Queue System Mechanics (`TollPlazaQueue`)
* Modeled queue operations (First-In, First-Out behavior) by modifying circular doubly linked pointers (`head`, `tail`) upon vehicle entry and toll clearance[cite: 20].
* Handled transaction processing by evaluating balances before completing deletion routines[cite: 20, 21].

### 3. String Immutability & Manipulation Mechanics
* **Immutability:** String methods like `.upper()`, `.strip()`, and `.split()` do not modify original strings in place; they return newly allocated string objects in memory[cite: 22].
* **Indexing & Slicing:**
  * Positive indexing (`[0]`) and Negative indexing (`[-1]`) for reverse access[cite: 22].
  * Substring Slicing syntax: `[start:stop:step]`[cite: 22].
  * Reverse String Trick: `str[::-1]` reverses string order using a negative step size[cite: 22].
* **Advanced Formatting:** Compared `f-strings`, `.format()`, positional indexing `{0}`, and map-based dictionary formatting `.format_map(vars(self))`[cite: 19, 23].

---
