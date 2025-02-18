import random

def brand_name_generator():
    print("Welcome to the Brand Name Generator!")
    adjective = input("Enter an adjective that describes your brand: ")
    noun = input("Enter a noun related to your brand: ")
    
    suffixes = ["ify", "ology", "scape", "sy", "ster", "genix", "omatic", "verse", "flow"]
    prefix = ["Neo", "Ultra", "Hyper", "Eco", "Pro", "Quantum", "Cyber", "Omni", "Super"]
    
    brand_name1 = adjective.capitalize() + noun.capitalize()
    brand_name2 = noun.capitalize() + random.choice(suffixes)
    brand_name3 = random.choice(prefix) + noun.capitalize()
    
    print("Here are some brand name ideas for you:")
    print(f"1. {brand_name1}")
    print(f"2. {brand_name2}")
    print(f"3. {brand_name3}")

if __name__ == "__main__":
    brand_name_generator()
