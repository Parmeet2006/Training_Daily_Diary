# 📅 Day 9: Methods in Classes, Linked Data Structures, & Circular Doubly Linked List Mechanics

**Date:** July 02, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 9`

---

## 🎯 Overview & Objectives

Session 9 focused on expanding class capabilities by encapsulating behaviors inside instance methods and building low-level linked data structures from scratch[cite: 13, 14, 16]. We transitioned from simple property storage to building a **Circular Doubly Linked List (CDLL)** data structure to power music playlist navigation (forward and reverse looping)[cite: 14, 16, 17, 18].

---

## 🧠 Key Concepts & Learning Summary

### 1. Encapsulating Behavior in Classes
* Added member functions to models (e.g., `input_user_details()`, `show_user_details()`) to isolate data input/output logic inside the class definition[cite: 13].
* Explored invoking instance methods via instance variables (`user.show_user_details()`) versus explicit class references (`User.show_user_details(user)`)[cite: 13, 14].

### 2. Manual Pointers & Node Referencing
* Designed a `Song` node containing data attributes (`title`, `artist`, `duration`) and pointer references (`next_song`, `previous_song`) initialized to `None`[cite: 14, 15].
* Linked nodes manually by setting bidirectional pointers to form a closed circular loop[cite: 14].

### 3. Circular Doubly Linked List (CDLL) Architecture
* Built a custom `CircularDoublyLinkedList` container class managing `head`, `tail`, and `size` references[cite: 16].
* **Dynamic Node Insertion (`add` method):**
  * When empty (`head == None`): Both `head` and `tail` point to the new element[cite: 16].
  * When populated: Updates four crucial memory links to stitch the new node between `tail` and `head` dynamically[cite: 16].
* **Bidirectional Traversal:** Loop through nodes seamlessly in both forward (`head` $\rightarrow$ `tail`) and reverse (`tail` $\rightarrow$ `head`) directions until returning to the start node[cite: 14, 16].

---
