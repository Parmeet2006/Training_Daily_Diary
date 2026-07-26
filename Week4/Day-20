# 📅 Day 20: Capstone Project Architecture — "DelegateAI / Prompt2Phone" (Autonomous Telephony & Voice Task Execution)

**Date:** July 22, 2026  
**Training:** Agentic AI with Python (6-Week Industrial Training)  
**Mentor:** Ishant Sharma (Director, Auribises Technologies, Ludhiana)  
**Repository Source:** `DelegateAI / Prompt2Phone Capstone Project`

---

## 🎯 Overview & Objectives

Session 20 marked the official architectural assembly and execution of our capstone industrial AI project: **"DelegateAI / Prompt2Phone"** (*Tagline: "Type the task. AI makes the call."*). 

Moving beyond isolated scripts, we integrated our complete 6-week tech stack—**Python, OpenAI Function Calling (`gpt-4o-mini`), ElevenLabs Conversational AI, Twilio Outbound Telephony, Streamlit Navigation UI, and MongoDB Atlas Persistence**—into a production-ready, multi-agent task execution system.

Link Of Prompt2Phone: https://github.com/Parmeet2006/DelegateAI
---

## 🏗️ Complete Project Directory Structure

```text
delegateai/
├── .env                       # API Credentials & Mongo Connection URIs (Excluded via .gitignore)
├── .gitignore                 # Prevents pushing virtualenvs (.venv) and .env keys
├── requirements.txt           # Environment dependencies (streamlit, pymongo, openai, elevenlabs, etc.)
├── config.py                  # Centralized client initializations (OpenAI, ElevenLabs, Mongo URIs)
├── database.py                # MongoDB Atlas DBHelper & Collections (`tasks`, `contacts`)
├── aiagent.py                 # OpenAI Function Calling Engine (`save_task` tool schema)
├── calleragent.py             # ElevenLabs + Twilio Telephony Dispatcher & Conversation Tracker
├── app.py                     # Main Streamlit Application Navigation Entry Point
└── pages/
    ├── save_tasks.py          # Conversational Chat Interface for Delegating Tasks
    ├── execute_calls.py       # Control Board for Dispatching Outbound Voice Calls
    └── dashboard.py           # Real-Time Telephony Analytics & Call Status Monitoring
