#Combined Story
import Getters

def Story1(debug=False):
    if debug: print("Story1 Function")
    print("\n")
    output = ""

    character1 = "Mario"
    color1 = Getters.getColor("Pick a Color: ")
    kartType = "Kart"
    city = "Greensville"
    town = "TownTown"
    color2 = "Red"
    firstLetter = "M"
    character2 = "Wario"
    hours = 2
    socialMedia = "Snapchat"
    
    output += "Mario Kart Legacy: \n"
    output += "One day "+character1+" was walking down the street, \n"
    output += "and they saw a "+color1+" "+kartType+" and they stole it. \n"
    output += character1+" took the "+kartType+" to the "+town+" "+city+" auto shop. \n"
    output += character1+" added a "+color2+" "+firstLetter+" to their"+kartType+".\n"
    output += "Now with their pimped out "+kartType+" "+character1+" went to "
    return output

print(Story1())
