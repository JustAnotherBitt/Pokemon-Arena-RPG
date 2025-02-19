import subprocess
from ascii_art import game_name

game_name()

def choose_language():
    print("Choose the language:")
    print("1 - English ")
    print("2 - Portuguese (Brazil)")

    choice = input("Option: ")

    if choice == "1":
        subprocess.run(["python", "game_en/main_en.py"])
    elif choice == "2":
        subprocess.run(["python", "game_pt/main_pt.py"]) 
    else:
        print("Invalid option!")


if __name__ == "__main__":
    choose_language()
