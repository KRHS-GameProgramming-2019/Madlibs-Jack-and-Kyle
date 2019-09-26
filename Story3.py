# Kyles Story
import Getters

def Story3(debug):
    if debug: print("Story3 Function")
    print("\n")
    
    friendName1 = Getters.getWord("Enter a name: ",debug)
    sportName1 = Getters.getSport("Enter a sport: ",debug)
    
    output = "\n"
    output += "One day me and my friend " + friendName1
    output += " were playing "+sportName1+"\n"
    output += friendName1 + " scored a point"

    return output 

