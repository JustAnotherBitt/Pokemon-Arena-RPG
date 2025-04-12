import subprocess
from ascii_art import game_name

game_name()

def choose_language():
    while True:
        print("Choose the language:")
        print("1 - English")
        print("2 - Portuguese (Brazil)")

        choice = input("\nOption: ")

        if choice == "1":
            # subprocess.run(["python", "game_en/main_en.py"])
            print('\nOh, sorry... Language update is still in progress! Only Portuguese (2) is available for now ;)')
            print('Try again!\n')
        elif choice == "2":
            subprocess.run(["python", "game_pt/main_pt.py"])
            break
        else:
            print("Invalid option!\n")

if __name__ == "__main__":
    choose_language()

