from ibm_watson import TextToSpeechV1
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
api= IAMAuthenticator("1AawsCWWakZn2kdifzb6DqQ_E59Bkq6HJ37iF4cOr6Qo")
text_2_speech = TextToSpeechV1(authenticator=api)
text_2_speech.set_service_url("https://api.eu-gb.text-to-speech.watson.cloud.ibm.com/instances/8cc629be-45c6-4773-a998-52defdd6cd5d")

import speech_recognition as sr
r=sr.Recognizer()
with sr.Microphone() as source:
    print("Speak Now")
    audio=r.listen(source)
    try:
        text=r.recognize_google(audio)
        print("You said:{}".format(text))
    except:
        print("we couldnot record your voice") 

thefile=open('spechtotext.txt','w')
thefile.write(format(text))
thefile.close()

with open("spechtotext.txt") as text_file:
   d=text_file.read()
   text_file.close()


with open("texttospech.mp3","wb") as audio:
   audio.write(text_2_speech.synthesize(d,accept="audio/mp3").get_result().content)
