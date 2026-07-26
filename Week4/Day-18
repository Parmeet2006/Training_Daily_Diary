# 📅 Day 18: Pattern Extraction via Regular Expressions (Regex) & Multi-Page Streamlit Dashboards

**Date:** July 11, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 18`

---

## 🎯 Overview & Objectives

Session 18 focused on advanced text extraction mechanics using Regular Expressions (`re` module) and building multi-page enterprise web dashboards using Streamlit (`st.navigation`, `st.Page`)[cite: 55, 56]. We implemented pattern matching rules to extract entity attributes (emails, phone numbers, vehicle registrations, PAN numbers, hashtags, URLs), and structured a complete healthcare dashboard with metrics, line charts, and dataframes[cite: 55, 57, 59].

---

## 🧠 Key Concepts & Learning Summary

### 1. Pattern Matching & Text Extraction (`re` Module)
* **Search & Match Operations:**
  * `re.search()`: Locates substring occurrences within raw text[cite: 55].
  * `re.findall()`: Extracts all non-overlapping matches fitting pattern rules (e.g., regex quantifiers `\d+`, `\S+@\S+`, `#\w+`, `https?://\S+`)[cite: 55].
  * `re.fullmatch()`: Validates exact string structure constraints against entire inputs[cite: 55].
* **Entity Validation Rules:**
  * **Phone Number:** `\d{10}` (Exact 10-digit sequence)[cite: 55].
  * **PAN Card:** `[A-Z]{5}[0-9]{4}[A-Z]` (5 uppercase letters, 4 digits, 1 uppercase letter)[cite: 55].
  * **Vehicle Registration:** `[A-Z]{2}[0-9]{2}[A-Z]{2}[0-9]{4}` (State code, district code, series, and number)[cite: 55].
  * **URLs & Social Hashtags:** `https?://\S+` and `#\w+`[cite: 55].

### 2. Streamlit Multi-Page Navigation Architecture
* **`st.Page` & `st.navigation`:** Configured multi-page web applications by bundling distinct script files into an integrated navigation menu bar with custom titles and icons[cite: 56].
* **Layout Grid Mechanics:** Utilized `st.columns()` to divide UI views into responsive columns for display cards (`st.metric`) and split-screen charts/tables[cite: 57].
* **Analytics Visualization:** Integrated Pandas DataFrames (`pd.DataFrame`) directly with Streamlit's native charting components (`st.line_chart`, `st.dataframe`)[cite: 57, 59].

---
