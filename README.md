## Overview
This project is a Python-based virtual assistant capable of performing a variety of tasks using voice commands. The assistant can perform actions like opening applications, playing music, searching the web, managing notes, checking the weather, sending WhatsApp messages, and more.

---

## Features
- **Text-to-Speech (TTS)**: Converts the assistant's responses into spoken words.
- **Speech-to-Text (STT)**: Uses voice input to recognize commands.
- **Application Control**: Open/close applications like Notepad, Command Prompt, and Adobe Reader.
- **Music Playback**: Play specific songs or choose a random one.
- **Weather Information**: Fetch current weather details for a given city.
- **Web Search**: Perform searches on Google or YouTube.
- **Wikipedia Summaries**: Get concise information from Wikipedia.
- **System Control**: Control system functions like volume, shutdown, restart, or sleep mode.
- **WhatsApp Messaging**: Send scheduled messages to predefined contacts.
- **Screenshot Capture**: Take and save screenshots with custom filenames.
- **WolframAlpha Queries**: Get answers to computational or factual questions.

---

## Requirements
- Python 3.7+
- Libraries: Install the required Python modules using `pip install`:
  - `pyttsx3`
  - `speechrecognition`
  - `requests`
  - `wikipedia`
  - `pywhatkit`
  - `pyautogui`
  - `wolframalpha`

---

## Installation
1. Clone or download the repository.
2. Install the necessary Python libraries using:
   ```bash
   pip install pyttsx3 speechrecognition requests wikipedia pywhatkit pyautogui wolframalpha
   ```
3. Ensure that you have the required applications installed (e.g., Adobe Reader, Notepad).

---

## Configuration
- **Music Paths**: Update the `music_paths` dictionary with the correct paths to your local music files.
- **Weather API**: Replace the `api_key` in the weather function with your OpenWeatherMap API key.
- **WolframAlpha API**: Replace the `app_id` in the WolframAlpha query section with your WolframAlpha App ID.
- **WhatsApp Contacts**: Add/update the `contacts` dictionary with the names and numbers of your contacts.

---

## Usage
1. Run the script:
   ```bash
   python assistant.py
   ```
2. Greet the assistant to start:
   - E.g., "Good morning, Alex!"
3. Use voice commands to interact. Example commands:
   - "Open Notepad."
   - "What's the weather in New York?"
   - "Play the song 'Closer'."
   - "Take a screenshot."

---
