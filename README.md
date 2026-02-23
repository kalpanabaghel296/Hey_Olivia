# Hey_Olivia

<<<<<<< HEAD
Hey_Olivia is a Windows-based AI Voice Assistant built using Python, Natural Language Processing, and Machine Learning. It listens to the user's voice, understands the intent, and responds back using speech.
=======
Hey_Olivia is a Windows-based AI Voice Assistant built using Python,
Natural Language Processing, and Machine Learning. It listens to the
user's voice, understands the intent, and responds back using speech.
>>>>>>> d93671f7e4716a48bde98418a10db2e15403fd8b

------------------------------------------------------------------------

## Project Description

Olivia works as a voice-controlled assistant that:

<<<<<<< HEAD
-   Takes voice input from the user(hindi, english, hinglish)
=======
-   Takes voice input from the user
>>>>>>> d93671f7e4716a48bde98418a10db2e15403fd8b
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

-   Language: Python 3.10
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

This project requires Python 3.10.

Scikit-learn 1.3.0 works properly with Python 3.10. Using Python 3.12 or higher may cause installation errors.

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

    py -3.10 -m venv venv

Activate (Windows PowerShell):

    venv\Scripts\activate

### 3. Upgrade pip

    python -m pip install --upgrade pip

### 4. Install Dependencies

    pip install -r requirements.txt  
       or
    pip install numpy sounddevice SpeechRecognition googletrans==4.0.0-rc1 requests pyttsx3  

------------------------------------------------------------------------

## requirements.txt

Make sure your requirements.txt contains:

    Flask==3.0.0
    SpeechRecognition==3.10.0
    pyttsx3==2.90
    nltk==3.8.1
    scikit-learn==1.3.0

------------------------------------------------------------------------

## Running the Project

    python app.py

------------------------------------------------------------------------

## Common Error

If you get Microsoft C++ Build Tools error:

Reason: - Python version is not 3.10 - Or pip is outdated

Solution: - Install Python 3.10 - Upgrade pip - Recreate virtual
environment - Install requirements again

## To prevent from pushing the venv and cached files if .gitignore does not work:

    git rm -r --cached .
=======
>>>>>>> d93671f7e4716a48bde98418a10db2e15403fd8b

------------------------------------------------------------------------

<<<<<<< HEAD
------------------------------------------------------------------------

=======
## Python Version Requirement

This project requires Python 3.10.

Scikit-learn 1.3.0 works properly with Python 3.10. Using Python 3.12 or
higher may cause installation errors.

Check your Python version:

    python --version

If Python 3.10 is not installed, download it from:
https://www.python.org/downloads/release/python-31011/

While installing: - Select "Add Python to PATH" - Choose "Install for
all users"

------------------------------------------------------------------------

## Installation Guide

### 1. Clone the Repository

    git clone <your-repository-link>
    cd Hey_Olivia

### 2. Create Virtual Environment

    py -3.10 -m venv venv

Activate (Windows PowerShell):

    venv\Scripts\activate

### 3. Upgrade pip

    python -m pip install --upgrade pip

### 4. Install Dependencies

    pip install -r requirements.txt

------------------------------------------------------------------------

## requirements.txt

Make sure your requirements.txt contains:

    Flask==3.0.0
    SpeechRecognition==3.10.0
    pyttsx3==2.90
    nltk==3.8.1
    scikit-learn==1.3.0

------------------------------------------------------------------------

## Running the Project

    python app.py

or

    python server.py

------------------------------------------------------------------------

## Common Error

If you get Microsoft C++ Build Tools error:

Reason: - Python version is not 3.10 - Or pip is outdated

Solution: - Install Python 3.10 - Upgrade pip - Recreate virtual
environment - Install requirements again

To delete old venv (PowerShell):

    deactivate
    Remove-Item -Recurse -Force venv

------------------------------------------------------------------------

>>>>>>> d93671f7e4716a48bde98418a10db2e15403fd8b
## Conclusion

Hey_Olivia demonstrates how Speech Recognition, NLP, Machine Learning,
and Web technologies can be combined to build a functional AI Voice
Assistant for Windows.
