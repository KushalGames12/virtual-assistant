import pyttsx3 # pip install pyttsx3
import speech_recognition as sr # pip install speechRecognition
import webbrowser as wb # pip install webbrowser

engine = pyttsx3.init()
voices = engine.getProperty('voice')
engine.setProperty('voice', voices[1])

def speak(audio):
       engine.say(audio) 
       engine.runAndWait()

def takeCommand():
	rec = sr.Recognizer()
	with sr.Microphone() as source:
		print('Listening')
		# rec.energy_threshold = 300
		# rec.pause_threshold = 0.5
		audio = rec.listen(source)

	try:
		print('Recognizing....')
		query = rec.recognize_google(audio)
		print(f'User Said: {query}')
	except Exception as e:
		print(e)
		print("I couldn't understand what you said! Would you like to repeat?")
		return 'None'
	return query

def openWebsite(link):
	try:
		wb.open(link)
	except Exception as e:
		speak("Failed to open the webpage")
		print("Failed to open the webpage")

if __name__ == '__main__':
	while True:
		command = takeCommand().lower()
		if command == "hello":
			print("Hello, Sir")
			speak("Hello, Sir")

		elif command == "open github":
			speak("Opening Github....")
			openWebsite("https://github.com/")

		elif command == "quit":
			quit()
