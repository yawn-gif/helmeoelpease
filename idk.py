import time
import random
import sys

def glitch_effect(text, glitch_char="#", delay=0.05):
    """Creates a glitchy text effect."""
    for char in text:
        if random.random() < 0.1:  # 10% chance to glitch
            sys.stdout.write(glitch_char)
            sys.stdout.flush()
            time.sleep(delay / 2)
            sys.stdout.write("\b" + char)
        else:
            sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def slow_print(text, delay=0.05):
    """Prints text slowly to create suspense."""
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

def main_menu():
    """Displays the main menu."""
    glitch_effect("Welcome to the Abyss", delay=0.1)
    print("1. Start Game")
    print("2. Exit")
    choice = input("Enter your choice: ")
    if choice == "1":
        start_game()
    elif choice == "2":
        glitch_effect("Goodbye...", delay=0.1)
    else:
        print("Invalid choice.")
        main_menu()

def start_game():
    """Begins the main game logic."""
    slow_print("You find yourself in a dark room. The air is cold.")
    time.sleep(1)
    first_decision()

def first_decision():
    """The player's first decision point."""
    slow_print("A faint light flickers to your left. To your right, you hear whispers.")
    print("1. Go left")
    print("2. Go right")
    print("3. Stay still")
    choice = input("What do you do? ")

    if choice == "1":
        go_left()
    elif choice == "2":
        go_right()
    elif choice == "3":
        stay_still()
    else:
        print("The whispers grow louder as you hesitate...")
        first_decision()

def go_left():
    """Handles the left path."""
    slow_print("You walk towards the light. It flickers, revealing a cracked mirror.")
    glitch_effect("Your reflection doesn't match your movements...", delay=0.08)
    time.sleep(1)
    print("1. Touch the mirror")
    print("2. Turn back")
    choice = input("What do you do? ")

    if choice == "1":
        mirror_event()
    elif choice == "2":
        slow_print("You turn back, but the light disappears. You are lost.")
        end_game("Lost")
    else:
        print("The mirror starts to crack as you hesitate...")
        go_left()

def go_right():
    """Handles the right path."""
    slow_print("The whispers grow louder. You feel something brushing against your arm.")
    glitch_effect("RUN", delay=0.2)
    time.sleep(1)
    print("1. Run forward")
    print("2. Stay still")
    choice = input("What do you do? ")

    if choice == "1":
        slow_print("You run into the darkness, but the whispers follow you.")
        end_game("Whispered to Death")
    elif choice == "2":
        slow_print("The whispers surround you. You feel a cold breath on your neck.")
        end_game("Taken by the Whispers")
    else:
        print("Your indecision costs you dearly...")
        go_right()

def stay_still():
    """Handles staying still."""
    slow_print("You stay still, hoping the darkness will pass.")
    glitch_effect("...but it doesn't.", delay=0.1)
    end_game("Consumed by the Void")

def mirror_event():
    """Event when the player touches the mirror."""
    glitch_effect("Your hand sinks into the mirror.", delay=0.08)
    slow_print("You are pulled into another dimension...")
    time.sleep(1)
    print("1. Explore")
    print("2. Call for help")
    choice = input("What do you do? ")

    if choice == "1":
        slow_print("You wander through the strange world, finding fragments of your past.")
        end_game("Trapped in Reflection")
    elif choice == "2":
        slow_print("Your cries echo, but no one answers.")
        end_game("Echoes Forever")
    else:
        print("Time distorts around you as you hesitate...")
        mirror_event()

def end_game(outcome):
    """Handles the end of the game."""
    glitch_effect(f"Ending: {outcome}", delay=0.1)
    play_again = input("Would you like to play again? (y/n): ")
    if play_again.lower() == "y":
        main_menu()
    else:
        glitch_effect("Farewell...", delay=0.1)

# Start the game
if __name__ == "__main__":
    main_menu()


