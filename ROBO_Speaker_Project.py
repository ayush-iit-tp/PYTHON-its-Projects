import os

if __name__ == '__main__':
    print("Welcome to RoboSpeaker 1.1. "
          "Created by Ayush")

    while True:
          x = input("Enter what you want me to speak: ")
          if x == "q":
              break
          command = f'powershell -Command "Add-Type -AssemblyName System.Speech; 'f'$speak = New-Object System.Speech.Synthesis.SpeechSynthesizer; 'f'$speak.Speak(\'{x}\');"'
          os.system(command)
