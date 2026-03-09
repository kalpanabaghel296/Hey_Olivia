
# Olivia AI Assistant – Desktop Control & Automation Module

## Overview

The **Desktop Control & Automation Module** extends the functionality of the Olivia AI Assistant, enabling it to interact with the Windows operating system and perform real-world tasks through voice commands.

With this module, Olivia can:

- Launch desktop applications
- Perform system operations
- Control browser activities
- Automate keyboard and mouse interactions

This enhancement transforms Olivia from a simple conversational assistant into a **desktop automation assistant capable of executing system-level tasks**.

---
# System Architecture

The Olivia assistant follows a modular architecture that separates voice processing, intent detection, and task execution.

Voice Input  
→ Wake Word Detection  
→ Speech Recognition  
→ Language Translation (Hindi / Hinglish → English)  
→ Intent Detection (processor.py)  
→ Command Routing  
→ Controllers (System / Browser / Automation)  
→ System Execution  
→ Voice / Text Response

---

# Project Structure

Hey_Olivia
│
├── backend
│   ├── app.py
│   ├── core
│   │   └── assistant.py
│   ├── brain
│   │   └── processor.py
│   ├── voice
│   │   ├── wake_word.py
│   │   └── tts.py
|   |   |_ listener.py 
│   ├── commands
│   │   └── command_listener.py
│   ├── utils
│   │   └── translator.py
│   ├── system
│   │   └── system_controller.py
│   ├── browser
│   │   └── browser_controller.py
│   └── automation
│       └── automation_controller.py
│
├── docs
├── requirements.txt
├── README.md
└── Dockerfile

---

# Controller Modules

## System Controller

Location:

backend/system/system_controller.py

Responsibilities:

- Opening desktop applications
- Shutdown / Restart
- Lock system
- Opening Windows utilities

Example commands:

open calculator  
open notepad   
restart system

### Application Launch Strategy

Olivia uses a **three stage launch strategy**.

1. Known Windows system commands

Examples:

calc  
explorer  
notepad  

2. Start Menu search

Directories scanned: this helps in newly installed apps 

C:\\ProgramData\\Microsoft\\Windows\\Start Menu\\Programs  
%APPDATA%\\Microsoft\\Windows\\Start Menu\\Programs  

This helps launch apps like:

VS Code  
Spotify  
Zoom  
Chrome  
Teams  

3. Generic fallback launcher

start "" "app_name"

Used when the application exists in the system PATH.

---

# Browser Controller

Location:

backend/browser/browser_controller.py

Responsibilities:

- Opening websites
- Google search
- YouTube search

Example commands:

open youtube  
search python tutorial  
play lofi music

---

# Automation Controller

Location:

backend/automation/automation_controller.py

Responsibilities:

- Keyboard automation
- Mouse automation
- Controlling active windows

Library used:

pyautogui

Example commands:

scroll down  
scroll up  
type hello world  
press enter  
switch tab  
close tab

---

# Intent Detection

Implemented in:

backend/brain/processor.py

The processor analyzes text commands and routes them to the correct controller.

Example routing:

open chrome → SystemController  
search python → BrowserController  
scroll down → AutomationController  

Example flow:

User: Olivia open calculator  

Speech Recognition → "open calculator"  

Intent → OPEN_APP  

Controller → SystemController  

Calculator opens.

---

# Example Voice Commands

System:

Olivia open calculator  
Olivia open notepad  
Olivia open file explorer  

Browser:

Olivia open youtube  
Olivia search machine learning tutorial  

Automation:

Olivia scroll down  
Olivia type hello everyone  
Olivia press enter  

---

# Future Improvements

## Smart Application Indexing

Olivia will scan installed applications once and build an index file.

Example:

apps_index.json

Then launching apps will become faster.

Example:

open vscode  
open spotify  
open zoom  

---

## Advanced Browser Intelligence

Future features:

pause youtube video  
skip video  
open new tab  
close browser  

---

## LLM Integration

LLM will handle general questions.

Examples:

Olivia who is Kalpana Chawla  
Olivia explain machine learning  
Olivia what is sin 30  

Unknown commands will be routed to the LLM.

---

# Dependencies

Key libraries:

pyautogui  
subprocess  
os  
glob  
webbrowser  

---

# Summary

The Desktop Control & Automation Module enables Olivia to:

- Launch applications
- Perform system operations
- Control browser tasks
- Automate desktop interactions
