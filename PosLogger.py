import subprocess
import sys
import os
import platform
import msvcrt as m
print("Checking dependencies...")
try:
    import pyautogui
    print("pyautogui found.")
except ModuleNotFoundError:
    while True:
        print("You have missing 'pyautogui dependency. Do you want to install now?'")
        choice = input("""
            [y/Y] Yes
            [n/N] No
            input:  >""")
        if choice == "y" or choice == "Y":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pyautogui"])
            input("pyautogui installed. Please restart the app.")
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif choice == "n" or choice == "N":
            quit()
        else:
            input("You entered incorrect input.")
            continue

try:
    import pynput
    print("pynput found.")
except ModuleNotFoundError:
    while True:
        print("You have missing 'pynput' dependency. Do you want to install now?'")
        choice = input("""
            [y/Y] Yes
            [n/N] No
            input:  >""")
        if choice == "y" or choice == "Y":
            subprocess.check_call([sys.executable, "-m", "pip", "install", "pynput"])
            input("pynput installed. Please restart the app.")
            os.execl(sys.executable, sys.executable, *sys.argv)
        elif choice == "n" or choice == "N":
            quit()
        else:
            input("You entered incorrect input.")
            continue

def clear():
    return os.system("cls" if platform.system() == "Windows" else "clear")

logfile = open("Logs.txt", "a+")


def wait():
    m.getch()

def mouselog():
    current = pyautogui.position()
    clear()
    print(current)
    description = input("Type your description (type c/C to cancel): ")
    if not description == "c" or description == "C":
        with open("Logs.txt", "a+") as logfile:
            logfile.write(f"{current} :"+f"{description}\n")
            input("Mouse position is logged.")
    else:
        input("Operation is cancelled.")
        return False

while True:
    clear()
    print("""
    Mouse Position Logger
    --------------------
    Logs the mouse positions with descriptions and saves it to a 'Logs' file.

    Your saved positions:
    """)
    logfile = open("Logs.txt", "r")
    for line in logfile.readlines():
        print(" "*4+line)
    logfile.close()

    menu_operation_input = input("""
    [1] Start Logging
    [2] Remove a Log
    [3] Quit
    input:  >""")

    if str(menu_operation_input) == "1":
        print("Press any key to record the mouse position...")
        wait()
        if mouselog() == False:
            continue
    elif str(menu_operation_input) == "2":
        while True:
            clear()
            print("Type the index number of the line to delete:")
            with open("Logs.txt") as file:
                lines = file.readlines()

            for index, line in enumerate(lines, 1):
                if line.strip():
                    print(f"[{index}] "+line)
            delete_index = int(
                input("Enter the line number you want to delete: "))

            with open("Logs.txt", 'w') as file:
                for index, line in enumerate(lines, 1):
                    if index != delete_index and line.strip():
                        file.write(line)
            input(f"Index of {delete_index}th line is deleted.")
            break
    elif str(menu_operation_input) == "3":
        quit()
