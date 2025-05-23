import json
import speech_recognition as sr
from dotenv import load_dotenv
import os
import pyautogui
import keyboard

load_dotenv()


def prompt_user_for_character():
    """Prompt the user for a character and return the corresponding voice line."""
    with open('characters.json', 'r') as f:
        char_vl = json.load(f)

    user_input = input("Enter a character: ")
    if user_input == "exit":
        print("Exiting...")
        exit()
    elif user_input == "help":
        print("Available characters: ", ', '.join(list(char_vl.keys())))
        return prompt_user_for_character()
    
    if user_input.title() in char_vl.keys():
        print("Selected character:", user_input)
        print("Voice line:", char_vl[user_input.title()])
        return char_vl[user_input.title()]
    else:
        print("Character not found. Please check the name and try again.")
        return prompt_user_for_character()


def recoginize_vl(voice_line):
    """Recognize the voice line using Google Speech Recognition."""
    r = sr.Recognizer()
    said_something = False
    while True:
        with sr.Microphone() as source:
            if not said_something:
                print("Say something!")
            try:
                audio = r.listen(source)
                voice_to_text = r.recognize_google(audio)
                print("You said:", voice_to_text)
                if voice_to_text.lower() == voice_line.lower():
                    said_something = True
                    return True
            except Exception as e:
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