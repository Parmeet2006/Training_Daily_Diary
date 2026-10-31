# 📅 Day 19: Web Search APIs (Serper.dev) & Web Scraping with BeautifulSoup

**Date:** July 12, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `Session 19`

---

## 🎯 Overview & Objectives

Session 19 focused on web data retrieval and extraction mechanics[cite: 60, 61]. We explored executing structured web searches via the **Serper.dev API** to retrieve real-time search engine results (titles and snippets) and built web scrapers using **BeautifulSoup4** to parse HTML document trees, filter CSS tags/classes, and extract raw text from target web pages[cite: 60, 61].

---

## 🧠 Key Concepts & Learning Summary

### 1. Web Search Integration (Serper.dev API)
* **REST Payload Configuration:** Constructed HTTP POST requests to `https://google.serper.dev/search` carrying JSON payload queries (`{"q": query}`) and custom header authorization keys (`X-API-KEY`)[cite: 60].
* **Organic Result Parsing:** Parsed JSON response bodies to extract organic search result titles, snippets, and URLs dynamically[cite: 60].

### 2. Web Scraping & HTML Document Parsing (`BeautifulSoup4`)
* **HTML Parsing Engine:** Leveraged `BeautifulSoup(html_text, 'html.parser')` to parse raw HTML strings fetched via the `requests` library[cite: 61].
* **Tag Selection Methods:**
  * `.find_all('tag')`: Retrieves all occurrences of specific HTML tags (e.g., `<a>`, `<p>`)[cite: 61].
  * **Class Filtering:** Selected HTML elements based on explicit CSS class signatures (e.g., `<p class="star-rating Three">`)[cite: 61].
* **Text Extraction:** Processed tag objects to extract raw human-readable text contents using `.text` attributes[cite: 61].

---
