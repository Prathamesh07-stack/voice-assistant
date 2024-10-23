import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)  # Use 'voice' instead of 'voices'

# Set speech rate
engine.setProperty('rate', 150)  # Set the rate to a lower value (e.g., 150)

def talk(text):
    engine.say(text)  # Use the parameter text
    engine.runAndWait()

def take_command():
    try:
        with sr.Microphone() as source:
            print('Listening...')
            voice = listener.listen(source)
            command = listener.recognize_google(voice)
            command = command.lower()

            if 'alexa' in command:
                command = command.replace('alexa', '').strip()  # Remove 'alexa' and trim whitespace
                print(command)
                return command  # Return the command after processing it
    except Exception as e:  # Exception handling for better debugging
        print(f"An error occurred: {e}")
        return None  # Return None if an error occurs

def run_alexa():
    command = take_command()  # Get the command
    if command:  # Check if command is not None
        if 'play' in command:
            song = command.replace('play', '')
            talk('Playing ' + song)
            pywhatkit.playonyt(song)
        elif 'time' in command:
            time = datetime.datetime.now().strftime('%I:%M %p')
            print(time)
            talk('Current time is ' + time)
        elif 'who' in command:
            person = command.replace('who', '')
            info = wikipedia.summary(person, 2)
            print(info)
            talk(info)
        elif 'date' in command:
            talk('Rohit, you can go with your heart, surgeon. I\'m not free for you.')

        run_alexa()  # Keep running to listen for further commands

# Start the Alexa function
run_alexa()
