import Lists

# Menu Options
def getMenuOption(debug=False):
    if debug: print("getMenuOption Function")
    
    goodInput = False
    while not goodInput:
        option = input("Please Select An Option: ")
        option = option.lower()
        # ~ print(option)
        if (option == "q" or 
            option == "quit" or 
            option == "x" or
            option == "exit"):
                option = "q"
                goodInput = True
                
        if (option == "1" or 
            option == "one" or 
            option == "story1" or
            option == "story 1"):
                option = "story1"
                goodInput = True
        else:
            print("Select A Menu Option")
    
    return option

# Word Getter
def getWord(prompt,debug=False):
    if debug: print("getWord Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
                
    
    return word

#Sport Getter
def getSport(prompt,debug=False):
    if debug: print("getSport Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.sports:
            goodInput = False
            print("Please enter a sport!")
    
    return word

#Color Getter
def getColor(prompt,debug=False):
    if debug: print("getColor Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.colors:
            goodInput = False
            print("Please enter a color!")
    
    return word

# Mario Character Getter
def getMario_Character(prompt,debug=False):
    if debug: print("getMario_Character Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.mario_characters:
            goodInput = False
            print("Please enter a Mario Character!")
        
    return word

# Vehicle Getter
def getVehicle(prompt,debug=False):
    if debug: print("getMario_Vehicle Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.mario_vehicle:
            goodInput = False
            print("Please enter a Mario Vehicle!")
            
    return word
            
# Get Social Media
def getSocial(prompt,debug=False):
    if debug: print("getSocialMediaPlatform Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.social_media_platform:
            goodInput = False
            print("Please enter a Social Media Platform!")
    return word
    
#Get Number
def getNumber(prompt,debug=False):
    if debug: print("getNumber Function")
    
    goodInput = False
    while not goodInput:
        number = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        try:
            number = int(number)
            goodInput = True
        except:
            goodInput = False
            print("Please enter a number!")

    return number

# Swear Checker
def isSwear(word, debug=False):
    if debug: print("SwearWord Function")
    
    if word.lower() in Lists.swearlist:
        return True
    else:
        return False
