#Combined Story
import Getters

def Story1(debug=False):
    if debug: print("Story1 Function")
    print("\n")
    output = ""

    character1 = Getters.getMario_Character("Enter a Mario Character: ")
    color1 = Getters.getColor("Pick a Color: ")
    kartType = Getters.getVehicle("Bike Or Kart? ")
    word = Getters.getWord("A Noun: ")
    city = "Crapstown"
    town = "TownTown"
    color2 = Getters.getColor("Pick a Color: ")
    firstLetter = character1[0].upper()
    character2 = Getters.getMario_Character("Enter a Mario Character: ")
    number1 = Getters.getNumber("Enter a number between 1 and 1000: ",1000)
    number2 = Getters.getNumber("Enter a number between 1 and 200: ",200)
    print("\n")
    
    output += "Mario Kart Race Story: \n"
    output += "One day "+character1+" was walking down the street,\n"
    output += "and they saw a "+color1+" "+kartType+" and they stole it.\n"
    output += character1+" took the "+kartType+" to the "+town+" "+city+" auto shop.\n"
    output += character1+" added a "+color2+" "+firstLetter+" to their "+kartType+" for "+number1+" dollars.\n"
    output += "Now with their pimped out "+kartType+" "+character1+" went to the race track.\n"
    output += "At the race track "+character1+" saw "+character2+" and challenged them to a race.\n"
    output += "The race was on the "+word1+" Cup at "+number2+" CC."
    output += character2+" was faster, but "+character1+" was better and won the race!\n"
    output += "\n"
    
    return output
