Python Voice Assistant

This is a versatile Python-based voice assistant that uses SpeechRecognition to take voice commands and perform various tasks, including playing music, searching Wikipedia, providing weather updates, controlling apps, taking notes, capturing screenshots, and sending WhatsApp messages. The assistant is integrated with WolframAlpha, OpenWeatherMap, and PyWhatKit to extend its functionality.

Features

	•	Music Playback: Play your favorite songs from local storage or online.
	•	Wikipedia Search: Fetch summarized information directly from Wikipedia.
	•	Weather Updates: Get real-time weather data for any city using OpenWeatherMap.
	•	App Control: Open applications like Notepad, Calculator, and more via voice commands.
	•	Note-Taking: Create and save notes seamlessly.
	•	Screenshot Capture: Take a screenshot and save it instantly.
	•	WhatsApp Messaging: Send WhatsApp messages via voice commands.
	•	General Knowledge: Solve queries and perform calculations using WolframAlpha.

Requirements

Before running the project, ensure you have the following installed:
	•	Python 3.7 or above
	•	The required Python libraries:
 pip install speechrecognition pyttsx3 wikipedia wolframalpha pywhatkit pyaudio pillow requests

 	•	API keys:
	•	WolframAlpha: Sign up at WolframAlpha Developer Portal.
	•	OpenWeatherMap: Sign up at OpenWeatherMap API.

How to Use

	1.	Clone the repository:
 git clone https://github.com/yourusername/python-voice-assistant.git
cd python-voice-assistant

	2.	Place your API keys for WolframAlpha and OpenWeatherMap in the appropriate locations in the code.
	3.	Run the assistant:
 python bot2.py

 	4.	Speak your command after the assistant activates (e.g., “Play music,” “What’s the weather in New York?”).

Commands

Here are some example commands the assistant can understand:
	•	Music: “Play music” or “Play [song name].”
	•	Wikipedia: “Tell me about [topic].”
	•	Weather: “What’s the weather in [city]?”
	•	App Control: “Open Notepad” or “Open Calculator.”
	•	Notes: “Take a note” or “Write this down.”
	•	Screenshot: “Take a screenshot.”
	•	WhatsApp: “Send a WhatsApp message to [contact name].”
	•	General Knowledge: “What is the square root of 64?” or “Who is the president of the USA?”

Dependencies

	•	SpeechRecognition: For voice command recognition.
	•	Pyttsx3: For text-to-speech conversion.
	•	Wikipedia API: For fetching data from Wikipedia.
	•	WolframAlpha API: For general knowledge queries and calculations.
	•	PyWhatKit: For WhatsApp message automation.
	•	Pillow: For screenshot capture.
	•	Requests: For accessing weather APIs.

Future Improvements

	•	Add support for more languages.
	•	Include additional API integrations.
	•	Enhance NLP for better command recognition.

Contributing

Contributions are welcome! Feel free to fork the repository, create a branch, and submit a pull request.

