# Speech to HandWriting.
import speech_recognition as sr
import pywhatkit


def ListenWhatUserSaid():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Capturing Your voice...")
        r.pause_threshold = 1
        audio = r.listen(source)

    try:
        print("Initializing your voice.....")
        query = r.recognize_google(audio, language='en-in')
        print(f"user said:  {query}\n")
        pywhatkit.text_to_handwriting(query)


    except Exception as e:
        # print(e)
        return "nothing"
    return query


if __name__ == "__main__":
    ListenWhatUserSaid()
