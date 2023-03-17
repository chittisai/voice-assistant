import speech_recognition as sr
import pyttsx3
import pywhatkit
import datetime
import wikipedia as wiki

listener = sr.Recognizer()
engine = pyttsx3.init()
voices = engine.getProperty('voices')
engine.setProperty('voice', voices[1].id)


def talk(text):
    engine.say(text)
    engine.runAndWait()

#listening
with sr.Microphone() as source:
    talk('i am listening')
    print('listening....')
    voice = listener.listen(source)
    command = listener.recognize_google(voice)
    print('\t you: ' + command)

# running assistant
if 'song' in command:
    song = command.replace('song', '')

if 'play' in command:
    song = command.replace('play', '')
    print('🎶' + song)
    talk('playing' + song)
    pywhatkit.playonyt(song)

elif 'time' in command:
    time = datetime.datetime.now().strftime('%I:%M %p')
    print('current time is ' + time)
    talk('current time is ' + time)

elif 'who is' or 'who are' or 'what is' or 'what are' in command:
    incmnd = command.replace('who is' or 'what are' or 'who are' or 'what is', '')
    info = wiki.summary(incmnd, 1)
    print(info)
    talk(info)

elif 'hello' in command:
    print('hello! how can I help you? \n\t\t you should run the code again to give command')
    talk('hello! how can I help you?')
