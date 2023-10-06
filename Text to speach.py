import pyttsx3

engine = pyttsx3.init()

voices = engine.getProperty('voices')
engine.setProperty('voice', voices[0].id) # David voice in microsoft win 10

engine.setProperty('rate', 200)
engine.setProperty('volume', 1.0)

engine.say('Hello, world!')
engine.save_to_file('output.wav') # FOr Saving audio file in wav format
engine.runAndWait()
