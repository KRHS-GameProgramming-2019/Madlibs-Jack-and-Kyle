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

        if (option == "2" or 
            option == "two" or 
            option == "story2" or
            option == "story 2"):
                option = "story2"
                goodInput = True
         
        if (option == "3" or 
            option == "three" or 
            option == "story3" or
            option == "story 3"):
                option = "story3"
                goodInput = True
        
        if option == "naughty":
            option = "naughty"
            goodInput = True
        
        if option == "snake":
            option = "snake"
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

#Time Of Day Getter
def getTOD(prompt,debug=False):
    if debug: print("getTOD Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.times:
            goodInput = False
            print("Please enter a time of day!")
    
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
        
        if word.lower() in Lists.blocks:
            goodInput = False
            print("Choose a different character!")
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
            
        elif word.lower() not in Lists.mario_characters:
            goodInput = False
            print("Please enter a Mario Character!")
    
    Lists.blocks.append(word.lower())
    return word

# Vehicle Getter
def getMarioVehicle(prompt,debug=False):
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
def getNumber(mini = 0, maxi = 1,debug=False):
    if debug: print("getNumber Function")
    
    goodInput = False
    while not goodInput:
        number = input("Enter a number between "+str(mini)+" and "+str(maxi)+": ")
        goodInput = True
        
        try:
            number = int(number)
            if number < maxi+1 and number > mini-1:
                goodInput = True
            else:
                goodInput = False
                print("Please enter a number in the range!")
        except:
            goodInput = False
            print("Please enter a number!")
    
    number = str(number)
    return number
    
# Get Action
def getAction(prompt,debug=False):
    if debug: print("getAction Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.action:
            goodInput = False
            print("Please enter a synonym for jumped")
    return word
    
# Get Mario Villains
def getMario_Villains(prompt,debug=False):
    if debug: print("getMarioVillain Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.mario_villains:
            goodInput = False
            print("Please enter a Mario Villain")
    return word
    
# Get SFL
def getSFL(prompt,debug=False):
    if debug: print("getSFL Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.SFL:
            goodInput = False
            print("Please enter a synonym for large!")
    return word
    
# Get Vehicle
def getVehicle(prompt,debug=False):
    if debug: print("getVehicle Function")
    
    goodInput = False
    while not goodInput:
        word = input(prompt)
        goodInput = True
        
        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        elif word.lower() not in Lists.vehicle:
            goodInput = False
            print("Please enter a vehicle type!")
    return word

#Get Verb
def getVerb(debug=False,endsWith=""):
    if debug: print("getVehicle Function")
    
    goodInput = False
    while not goodInput:
        word = input("Enter a verb that ends with "+endsWith+": ")
        goodInput = True

        if isSwear(word,debug):
            goodInput = False
            print("Please dont swear!")
        if not word.endswith(endsWith):
            goodInput = False
            print("The verb needs to end with "+endsWith+"!")

    return word
    
# Swear Checker
def isSwear(word, debug=False):
    if debug: print("SwearWord Function")
    
    if word.lower() in Lists.swearlist:
        return True
    else:
        return False
