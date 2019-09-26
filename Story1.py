#Combined Story
import Getters

def Story1(debug=False):
    if debug: print("Story1 Function")
    print("\n")
    output = ""

    character1 = Getters.getMario_Character("Enter a Mario Character: ")
    color1 = Getters.getColor("Pick a Color: ")
    kartType = Getters.getVehicle("Bike Or Kart? ")
    city = "Greensville"
    town = "TownTown"
    color2 = Getters.getColor("Pick a Color: ")
    firstLetter = charater1[0].upper()
    character2 = Getters.getMario_Character("Eneter a Mario Character: ")
    hours = 2
    socialMedia = Getters.getSocial("Enter a Social Media Platform: ")
    
    output += "Mario Kart Legacy: \n"
    output += "One day "+character1+" was walking down the street,\n"
    output += "and they saw a "+color1+" "+kartType+" and they stole it.\n"
    output += character1+" took the "+kartType+" to the "+town+" "+city+" auto shop.\n"
    output += character1+" added a "+color2+" "+firstLetter+" to their"+kartType+".\n"
    output += "Now with their pimped out "+kartType+" "+character1+" went to the race track.\n"
    return output

print(Story1())
