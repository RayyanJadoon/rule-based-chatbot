import re , random
from colorama import Fore, init

init(autoreset=True)

destinations = {

"beaches": ["Bali", "Maldives", "Phuket"],

"mountains": ["Swiss Alps", "Rocky Mountains", "Himalayas"],

"cities": ["Tokyo", "Paris", "New York"]

}

jokes = [

"Why don't programmers like nature? Too many bugs!",

"Why did the computer go to the doctor? Because it had a virus!",

"Why do travelers always feel warm? Because of all their hot spots!"

]


def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())


def show_help():
    print(Fore.CYAN + "Here are some things you can ask me:")
    print(Fore.YELLOW + "- Suggest a travel destination = type: 'suggest destination'")
    print(Fore.YELLOW + "- Tell me a joke = type: 'tell me a joke'")
    print(Fore.YELLOW + "- Exit = type: 'exit'")

def recommend():
    print(Fore.CYAN + "What type of destination are you interested in? (beaches, mountains, cities)")
    choice = normalize_input(input(Fore.YELLOW + "Your choice: "))

    if choice in destinations:
        destination = random.choice(destinations[choice])
        print(Fore.GREEN + f"I recommend you visit {destination}!")
    else:
        print(Fore.RED + "Sorry, I don't have recommendations for that type of destination.")

    print("Would you like another recommendation? (yes/no)")
    yes_no = normalize_input(input(Fore.YELLOW + "Your choice:  "))

    if yes_no == "yes":
        recommend()
    elif yes_no == "no":
        print(Fore.CYAN + "Alright! Hope you have a great trip!")
    else:
        print(Fore.RED + "I didn't understand that. Please type 'yes' or 'no'.")
        recommend()


def packing():
    print(Fore.CYAN + "What type of trip are you going on? (beach, mountain, city)")
    trip_type = normalize_input(input(Fore.YELLOW + "Your choice: "))

    if trip_type == "beach":
        print(Fore.GREEN + "For a beach trip, you should pack: swimsuit, sunscreen, sunglasses, flip-flops.")
    elif trip_type == "mountain":
        print(Fore.GREEN + "For a mountain trip, you should pack: hiking boots, warm clothes, backpack, water bottle.")
    elif trip_type == "city":
        print(Fore.GREEN + "For a city trip, you should pack: comfortable shoes, casual clothes, camera, travel guide.")
    else:
        print(Fore.RED + "Sorry, I don't have packing suggestions for that type of trip.")

def joke():
    joke = random.choice(jokes)
    print(Fore.GREEN + f"Here's a joke for you: {joke}")



def chat():
    print(Fore.CYAN + "Hello! I'm your travel assistant. How can I help you today?")
    name = input(Fore.YELLOW + "What's your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}!")

    while True:
        user_input = normalize_input(input(Fore.YELLOW + "You: "))

        if "recommend" in user_input or "suggest" in user_input:
            recommend()
        elif "joke" in user_input:
            joke()
        elif "pack" in user_input:
            packing()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input:
            print(Fore.CYAN + "Goodbye! Safe travels!")
            break
        else:
            print(Fore.RED + "I'm sorry, I didn't understand that. Type 'help' for options.")


if __name__ == "__main__":
    chat()

chat()