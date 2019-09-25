#Combined Story
import Getters

def Story1(debug):
    if debug: print("Story1 Function")
    print("\n")
    output = ""

    course1 = Getters.getCourse("")
    
    output += "Mario Kart Legacy: \n"
    output += "The race was on"

    return output
