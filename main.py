import json
import speech_recognition as sr
from dotenv import load_dotenv
import os
import pyautogui
import keyboard

load_dotenv()


def prompt_user_for_character():
    """Prompt the user for a character and return the corresponding voice line."""
    character = input("Enter a character: ")
    char_vl = {
        "Iron Fist": "cheaper town hall",
        "Luna Snow": "I am ready to put on a show"
    }
    #json.loads("characters.json")

    if character in char_vl.keys():
        print("Selected character:", character)
        print("Voice line:", char_vl[character])
        return char_vl[character]
    else:
        print("Character not found. Please check the name and try again.")
        prompt_user_for_character()


def recoginize_vl(voice_line):
    """Recognize the voice line using Google Speech Recognition."""
    r = sr.Recognizer()
    while True:
        with sr.Microphone() as source:
            print("Say something!")
            try:
                audio = r.listen(source)
                google_api_key = os.getenv("GOOGLE_SPEECH_RECOGNITION_API_KEY")
                voice_to_text = r.recognize_google(audio)
                print("You said:", voice_to_text)
                if voice_to_text.lower() == voice_line.lower():
                    return True
            except Exception as e:
                #print("Error:", e)
                #print("Could not understand the audio. Please try again.")
                continue

def ult_check(voice_line):
    """Check if the recognized voice line matches the ult line. If it does, press 'q'."""
    while True:
        if recoginize_vl(voice_line):
            keyboard.unblock_key('q')
            pyautogui.press('q')
            keyboard.block_key('q')
            print("Ulting!")


def main():
    keyboard.block_key('q')
    voice_line = prompt_user_for_character()
    ult_check(voice_line)


if __name__ == "__main__":
    main()