import speech_recognition as sr
import pyttsx3
import google.generativeai as genai
import os

# Configure your Google GenAI API key here
# Get one from Google AI Studio if you haven't already
API_KEY = "YOUR_GEMINI_API_KEY" 
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-1.5-flash')

# Initialize Text-to-Speech engine
engine = pyttsx3.init()

def speak(text):
    """Converts text to speech."""
    engine.say(text)
    engine.runAndWait()

def listen():
    """Listens to the microphone and converts speech to text."""
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("\nListening... (Say 'exit' or 'stop' to quit)")
        recognizer.adjust_for_ambient_noise(source)
        audio = recognizer.listen(source)
        try:
            command = recognizer.recognize_google(audio)
            print(f"You said: {command}")
            return command
        except sr.UnknownValueError:
            print("Sorry, I didn't catch that.")
            return None
        except sr.RequestError:
            print("Could not request results from Google Speech Recognition service.")
            return None

def process_with_ai(text):
    """Sends the text to Gemini and returns the response."""
    try:
        response = model.generate_content(text)
        return response.text.replace("*", "") # Removing markdown asterisks for better speech
    except Exception as e:
        print(f"Error: {e}")
        return "I encountered an error connecting to the AI."

if __name__ == "__main__":
    speak("Voice assistant activated. How can I help you today?")
    while True:
        user_input = listen()
        if user_input:
            if user_input.lower() in ['exit', 'quit', 'stop']:
                speak("Goodbye!")
                break
            
            ai_response = process_with_ai(user_input)
            print(f"Assistant: {ai_response}")
            speak(ai_response)
