import requests
from collections import deque
from termcolor import colored
import textwrap

# Replace YOUR_API_KEY with your actual API key
API_KEY = "YOUR_API_KEY"

def lookup_word(word):
    url = f"https://www.dictionaryapi.com/api/v3/references/collegiate/json/{word}?key={API_KEY}"
    response = requests.get(url)
    if response.status_code == 200:
        # The API returns a list of definitions for the word, so we just take the first one
        definition = response.json()[0]["shortdef"][0]
        return definition
    else:
        return None

def display_recent_searches(recent_searches):
    print(colored("Recent Searches:", "blue"))
    if len(recent_searches) == 0:
        print("No recent searches")
    else:
        for i, word in enumerate(recent_searches, start=1):
            print(f"{i}. {word}")
    print()

def main():
    recent_searches = deque(maxlen=10)
    while True:
        print(colored("Welcome to the Dictionary!!", "red"))
        print(colored("1. Look up a word", "cyan"))
        print(colored("2. Recent searches", "cyan"))
        print(colored("3. Quit", "cyan"))
        choice = input("Enter your choice: ")
        if choice == "1":
            word = input(colored("Enter a word to look up: ", "cyan"))
            definition = lookup_word(word)
            if definition:
                recent_searches.append(word)
                print(textwrap.fill(f"The definition of {colored(word, 'green')} is: {definition}", 100))
            else:
                print(f"Sorry, no definition found for {word}")
        elif choice == "2":
            display_recent_searches(recent_searches)
        elif choice == "3":
            print(colored("Goodbye!", "yellow"))
            break
        else:
            print(colored("Invalid choice. Please try again.", "red"))

if __name__ == "__main__":
    main()
