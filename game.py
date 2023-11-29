import time

def intro():
    print("Welcome to the Text Adventure Game!")
    time.sleep(1)
    print("You find yourself in a mysterious room.")

def make_choice():
    print("\nWhat will you do?")
    print("1. Open the door")
    print("2. Look around")

def open_door():
    print("\nThe door creaks open...")
    time.sleep(1)
    print("You see a dark hallway ahead.")

def look_around():
    print("\nYou look around and find a key on the table.")

def main():
    intro()
    choice = input("Enter 1 or 2: ")

    if choice == "1":
        open_door()
    elif choice == "2":
        look_around()
    else:
        print("Invalid choice. Game over.")

if __name__ == "__main__":
    main()
                                                                                          
