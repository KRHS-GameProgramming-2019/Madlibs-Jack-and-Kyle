#Jacks Story
import Getters

def Story2(debug):
    if debug: print("Story2 Function")
    print("\n")
    timeOfDay = Getters.getTOD("Enter a time of day: ")
    character1 = Getters.getMario_Character("Enter a Mario Character: ")
    number1 = Getters.getNumber("A number between 1 and 200: ",200)
    number2 = Getters.getNumber("A number between 1 and 12: ",12)
    color1 = Getters.getColor("Enter a color: ")
    noun1 = Getters.getWord("Enter a noun: ")
    verb1 = Getters.getVerb(endsWith="ly")
    color2 = Getters.getColor("Enter a color: ")
    noun2 = Getters.getWord("Enter a noun: ")
    character2 = Getters.getMario_Character("Enter a Second Mario Character: ")
    character3 = Getters.getMario_Character("Enter a Third Mario Character: ")
    color3 = Getters.getColor("Enter a color: ")
    noun3 = Getters.getWord("Etner a noun: ")
    noun4 = Getters.getWord("Enter another noun: ")
    kartType1 = Getters.getVehicle("Bike or Kart? ")
    noun5 = Getters.getWord("Enter the last noun: ")
    
    print("\n")
    output = ""
    output += "The Race At Bowsers Castle. \n"
    output += "\n"
    output += "One "+timeOfDay+" "+character1+" went to a race at Bowsers Castle.\n"
    output += "The race was on "+number1+" CC, and the racers were ready to go!\n"
    output += character1+" was in the "+number2+" place to start, with their "+color1+" "+noun1+" ready to go.\n"
    output += "They went through the course "+verb1+" and got to the first "+color2+" boost pad.\n"
    output += character1+" hit an item box and got a "+noun2+" they immediately used it on "+character2+".\n"
    output += "They then moved into pole position, but "+character1+" was soon contested by "+character3+" and they were fighting for the front.\n"
    output += "The two zoomed through the "+color3+" halls and left the castle.\n"
    output += "They both hit the "+noun3+" at the same time and cross the Finish "+noun4+".\n"
    output += character1+" got out of their "+kartType1+" and started hitting "+character3+" with "+noun5+".\n"
    output += character1+" lived and won the cup trophy!"
    output += "\n"
    

    return output
