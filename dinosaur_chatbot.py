import re, random
from colorama import Fore, init

# Initialize colorama (autoreset ensures each print resets after use)
init(autoreset=True)

# Destination & joke data
dinosaur = {
    "herbivores": ["Triceratops", "Staegosaurus", "Pachycepholosaurus"],
    "carnivores": ["T-rex", "Spinosaurus", "Gigantosaurus", "Allosaurus", "Velociraptor"],
    "hybrids": ["Indominus rex", "Ultima imperatrix", "Scorpios Rex", "Distortus Rex", "Mutadons", "Stegoceratops", ]
}

# Helper function to normalize user input (remove extra spaces, make lowercase)
def normalize_input(text):
    return re.sub(r"\s+", " ", text.strip().lower())

# Provide travel recommendations (recursive if user rejects suggestions)
def recommend():
    print(Fore.CYAN + "Dino Expert: Herbivores, Carnovores, or Hybrids?")
    preference = input(Fore.YELLOW + "You: ")
    preference = normalize_input(preference)
    
    if preference in dinosaur:
        suggestion = random.choice(dinosaur[preference])
        print(Fore.GREEN + f"Dino Expert: How about {suggestion}?")
        print(Fore.CYAN + "Dino Expert: Do you like it? (yes/no)")
        answer = input(Fore.YELLOW + "You: ").lower()
        
        if answer == "yes":
            print(Fore.GREEN + f"Dino Expert: Nice! {suggestion} is a really cool dino!")
        elif answer == "no":
            print(Fore.RED + "Dino Expert: Let's try another then.")
            recommend()
        else:
            print(Fore.RED + "Dino Expert: I'll suggest again.")
            recommend()
    else:
        print(Fore.RED + "Dino Expert: Sorry, I don't have that Dino.")
    
    show_help()

# Offer packing tips based on user’s destination and duration
def Taming_tips():
    print(Fore.CYAN + "Dino Expert: WHich Dino?")
    location = normalize_input(input(Fore.YELLOW + "You: "))
    print(Fore.CYAN + "Dino Expert: How Old?")
    days = input(Fore.YELLOW + "You: ")
    
    print(Fore.GREEN + f"Dino Expert: Taming tips for {days} days in {location}:")
    print(Fore.GREEN + "- Be gentle and careful.")
    print(Fore.GREEN + "- Dont make sudden movements.")
    print(Fore.GREEN + "- Don't tame the wrong dino.")

# Display help menu
def show_help():
    print(Fore.MAGENTA + "\nI can:")
    print(Fore.GREEN + "- Say the names of different dinosaurs(say 'name')")
    print(Fore.GREEN + "- Offer taming tips (say 'taming')")
    print(Fore.CYAN + "Type 'exit' or 'bye' to end.\n")

# Main chat loop
def chat():
    print(Fore.CYAN + "Hello! I'm a Dino Expert.")
    name = input(Fore.YELLOW + "Your name? ")
    print(Fore.GREEN + f"Nice to meet you, {name}! Hope you like dinosaurs!!!")
    show_help()
    
    while True:
        user_input = input(Fore.YELLOW + f"{name}: ")
        user_input = normalize_input(user_input)
        
        if "name" in user_input or "dino" in user_input:
            recommend()
        elif "tame" in user_input or "taming" in user_input:
            Taming_tips()
        elif "help" in user_input:
            show_help()
        elif "exit" in user_input or "bye" in user_input:
            print(Fore.CYAN + "Dino Expert:  Goodbye!  Hope you enjoy the world of dinosaurs!")
            break
        else:
            print(Fore.RED + "Dino Expert: Idon't understand.\n                    Could you rephrase?")

# Run the chatbot
if __name__ == "__main__":
    chat()
