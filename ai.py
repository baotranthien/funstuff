import speech_recognition
import pyttsx3
from datetime import datetime
now = datetime.now()
import pyttsx3
robot_ear = speech_recognition.Recognizer()
with speech_recognition.Microphone() as mic:
	print("Ikaros: I'm Listening")
	audio = robot_ear.listen(mic)
try:
	you = robot_ear.recognize_google(audio)
except:
	you = ""

print("You:" + you)

if "hello" in you:
	robot_brain = "Hi there I'm Ikaros nice to meet you"
elif "today" in you:
	robot_brain = today.strftime("%B %d, %Y")
else:
	robot_brain = "Sorry I can't hear you, could you please repeat that for me"
if "time" in you:
	robot_brain = now.strftime("%H:%M:%S")
if "weather" in you:
	robot_brain = "In Ho Chi Minh City, in daytime it will be scroching hot but in about 3PM it is going to rain quite recently"
if "your name" in you:
	robot_brain = "My name is Ikaros"
if you == "where are you from":
	robot_brain = "I'm from a manga called Sora no Otoshimono"
if you == "how do you look like":
	robot_brain = "I'm a girl with green eyes, pink hair and you coud google me as Ikaros from Sora no Otoshimono"
if "my name" in you:
	robot_brain = "Your name is Bao Tran"	
if "place to play" in you:
	robot_brain = print("I could suggest you a few place to go, if you in district 7 you could go to creasent mall or vincom and you could find more imformation on google")






print(robot_brain)
voice_handler = pyttsx3.init()
voices = voice_handler.getProperty('voices')
voice_handler.setProperty('voice',voices[1].id)
voice_handler.say(robot_brain)
voice_handler.runAndWait()
