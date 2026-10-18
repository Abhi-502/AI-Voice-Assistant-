AI Voice Assistant & Playfair Cipher Scripts
This repository contains two distinct projects: an AI-powered Voice Assistant built with Python and the Gemini API, and a cryptographic implementation of the Playfair Cipher in both Python and Java.

1. AI Voice Assistant
A Python-based voice assistant that listens to audio input via your microphone, processes the text using Google's Gemini Large Language Model, and responds using text-to-speech.

Prerequisites
Python 3.8+

A working microphone.

Google Gemini API Key: You must obtain a free API key from Google AI Studio.

Installation
Clone or download the project files to your local machine.

It is recommended to use a virtual environment:

Bash
python -m venv venv
source venv/bin/activate  # On Windows use: venv\Scripts\activate
Install the required dependencies:

Bash
pip install SpeechRecognition pyttsx3 google-generativeai pyaudio
Note: If pyaudio fails to install on macOS, you may need to run brew install portaudio first.

Configuration
Open voice_assistant.py and replace the placeholder API key with your actual Gemini API key:

Python
API_KEY = "YOUR_GEMINI_API_KEY" 
Usage
Run the assistant from your terminal:

Bash
python voice_assistant.py
The assistant will greet you and start listening.

Speak your query clearly into the microphone.

Say "exit", "stop", or "quit" to terminate the program.
