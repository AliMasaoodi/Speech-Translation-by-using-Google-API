# This is Python script.

# Import the necessary modules
import googletrans
import speech_recognition as spr
from googletrans import Translator
from gtts import gTTS
import os

# will print all languages that Google Translator supports
print(googletrans.LANGUAGES)

# Creating Recogniser() class object
recog1 = spr.Recognizer()

# Creating microphone instance
mc = spr.Microphone()

# Capture Voice
with mc as source:
    print("Please Speak 'hello' to initiate Translation !")
    print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
    recog1.adjust_for_ambient_noise(source, duration=0.2)
    audio = recog1.listen(source)
    MyText = recog1.recognize_google(audio)
    MyText = MyText.lower()

# Here initialising the recorder with Hello,
# whatever after that hello it will recognise it.
if 'hello' in MyText:

    # Translator method for translation
    translator = Translator()

    # short form of english which you will speak
    from_lang = 'en'

    # short form of spanish, that we want to convert
    to_lang = 'es'

    with mc as source:

        print("Speak you sentence...")
        recog1.adjust_for_ambient_noise(source, duration=0.2)

        # Storing your speech into an audio variable
        audio = recog1.listen(source)

        # By using recognize.google() method to
        # convert the audio into text
        get_sentence = recog1.recognize_google(audio)

        # B using try & except block to improve its efficiency.
        try:

            # Printing Speech that need to be translated
            print("Phase to be Translated :" + get_sentence)

            # Using translate() method that requires three arguments,
            # 1st the sentence which needs to be translated
            # 2nd source language
            # and 3rd to which we need to translate in
            text_to_translate = translator.translate(get_sentence,
                                                     src=from_lang,
                                                     dest=to_lang)

            # Storing the translated text in text variable
            text = text_to_translate.text

            # Using Google-Text-to-Speech ie, gTTS() method to speak the translated text into the
            # destination language which is stored in to_lang.
            # Also, we have given 3rd argument as False because by default it speaks very slowly
            speak = gTTS(text=text, lang=to_lang, slow=False)

            # By using save() method to save the translated speech
            # in capture_voice.mp3
            speak.save("captured_voice.mp3")

            # using OS module to run translated voice
            os.system("start captured_voice.mp3")

        # Here we are using except block for UnknownValue and Request Error and printing
        # the same to provide better service to the user.
        except spr.UnknownValueError:
            print("Unable to Understand your Input")

        except spr.RequestError as e:
            print("Unable to provide The Required Output".format(e))


