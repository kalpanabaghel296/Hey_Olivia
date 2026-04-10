# Hey_Olivia


Hey_Olivia is a Windows-based AI Voice Assistant built using Python, Natural Language Processing, and Machine Learning. It listens to the user's voice, understands the intent, and responds back using speech.



------------------------------------------------------------------------

## Project Description

Olivia works as a voice-controlled assistant that:

-   Takes voice input from the user(hindi, english, hinglish)
-   Converts speech into text
-   Processes the text using NLP
-   Predicts user intent using a Machine Learning model
-   Executes actions
-   Responds back using text-to-speech

------------------------------------------------------------------------

## Flow of Olivia

User Voice\
↓\
Microphone\
↓\
Speech-to-Text (SpeechRecognition)\
↓\
Text Preprocessing (NLTK)\
↓\
ML Intent Classifier (Scikit-learn)\
↓\
Action Executor (Web / System Tasks)\
↓\
Text Response\
↓\
Text-to-Speech (pyttsx3)\
↓\
User hears response

------------------------------------------------------------------------

## Tech Stack

-   Language: Python 3.11
-   Backend: Flask
-   Speech-to-Text: SpeechRecognition (Google API)
-   NLP: NLTK
-   Machine Learning: Scikit-learn
-   Frontend: HTML, CSS, JavaScript
-   Text-to-Speech: pyttsx3
-   Version Control: Git & GitHub
<<<<<<< HEAD

------------------------------------------------------------------------

## Python Version Requirement

This project requires Python 3.11.

Scikit-learn 1.3.0 works properly with Python 3.11.X Using Python 3.12 or higher may cause installation errors.

Check your Python version:

    python --version

If Python 3.10 is not installed, download it from:
https://www.python.org/downloads/release/python-31011/

While installing: - Select "Add Python to PATH" - Choose "Install for all users"

------------------------------------------------------------------------

## Guide to run this project

### 1. Clone the Repository

    https://github.com/kalpanabaghel296/Hey_Olivia
    cd Hey_Olivia

### 2. Create Virtual Environment

    py -3.11 -m venv venv

Activate (Windows PowerShell):

    venv\Scripts\activate

### 3. Upgrade pip

    python -m pip install --upgrade pip

### 4. Install Dependencies

    pip install -r requirements.txt  
       or
    pip install numpy sounddevice SpeechRecognition googletrans==4.0.0-rc1 requests pyttsx3  

### 5. To run the backend from root folder
    python -m backend.app

### 6. To run the assistant from root folder
    python -m backend.core.assistant

# To run the assistant responsibly, run thr backend first    
------------------------------------------------------------------------

## requirements.txt

Make sure your requirements.txt contains:

    Flask==3.0.0
    SpeechRecognition==3.10.0
    pyttsx3==2.90
    nltk==3.8.1
    scikit-learn==1.3.0
    
------------------------------------------------------------------------

## Common Error

If you get Microsoft C++ Build Tools error:

Reason: - Python version is not 3.11 - Or pip is outdated

Solution: - Install Python 3.11 - Upgrade pip - Recreate virtual
environment - Install requirements again

## To prevent from pushing the venv and cached files if .gitignore does not work:

    git rm -r --cached .

------------------------------------------------------------------------
## Conclusion

Hey_Olivia demonstrates how Speech Recognition, NLP, Machine Learning,
and Web technologies can be combined to build a functional AI Voice
Assistant for Windows.
