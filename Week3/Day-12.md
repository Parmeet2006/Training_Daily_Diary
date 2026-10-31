# 📅 Day 12: NoSQL Database Integration (MongoDB Atlas), Password Hashing (SHA-256), & Persistence Layer Abstraction

**Date:** July 05, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 12`

---

## 🎯 Overview & Objectives

Session 12 focused on persistence layers, security practices, and cloud NoSQL integration[cite: 29, 31, 34]. We configured a cloud-hosted MongoDB Atlas cluster, created client connections using `pymongo`, implemented password hashing using Python's `hashlib` (SHA-256), and applied object-oriented encapsulation to build modular helper utilities (`FileHelper` and `DBHelper`) for saving application state to disk and cloud databases[cite: 29, 31, 33, 34].

---

## 🧠 Key Concepts & Learning Summary

### 1. Cloud NoSQL Setup & Connection Mechanics (MongoDB Atlas)
* **Atlas Cluster Configuration:** Configured cloud cluster access, database user roles, and network security IP whitelisting (`0.0.0.0/0`)[cite: 29].
* **`pymongo` Connection:** Installed `pymongo[srv]` to manage connections via SRV connection strings (`mongodb+srv://...`)[cite: 29].
* **Server Ping Verification:** Issued admin `ping` commands to verify cluster reachability and handle network connection errors gracefully[cite: 29].

### 2. Cryptographic Hashing & Data Transformation
* **SHA-256 Encryption:** Applied `hashlib.sha256()` to encode user passwords into hexadecimal digest strings before storing them in database records[cite: 31].
* **Document Serializers:** Added conversion methods inside entity models (`to_csv()` for file storage and `to_dictionary()` via `vars(self)` for BSON/JSON NoSQL document inserts)[cite: 31].

### 3. Object-Oriented Persistence Abstraction (`FileHelper` & `DBHelper`)
* **`FileHelper` Class:** Encapsulated file handles, stream writes (`.write()`), and buffer closures (`.close()`) into a dedicated helper class[cite: 33].
* **`DBHelper` Class:** Created a database management utility class to handle MongoDB client initialization, collection selection, and document insertion (`insert_one`)[cite: 34].

---
