#import pyttsx3
#gap = pyttsx3.init()
#gap.say("Pydev kanaliga obuna bo'ling")
#gap.runAndWait()

#import speech_recognition as sr
#for index, name in enumerate(sr.Microphone.list_microphone_names()):
#    print("Microphone with name \"{1}\" found for `Microphone(device_index={0})`".format(index, name))
import speech_recognition as sr
r = sr.Recognizer()
with sr.Microphone(device_index=1) as source:
    print("Nimadir ayting")
    audio = r.listen(source)

query = r.recognize_google(audio, language="uz-UZ")
print(f"Siz {query.lower()} Dedingiz")