# Madlibs By Jack and Kyle

import Screens, Getters, Story1, Story2, Lists

def Madlibs(debug=False):
    if debug:
        print("Debug Active")
    
    print(Screens.titleScreen(debug))
    
    input("Press Any Key To Continue")
    
    done = False
    while not done:
        print(Screens.mainMenu(debug))
        choice = Getters.getMenuOption(debug)
        
        if choice == "q":
            exit();
        elif choice == "story1":
            print(Story1.Story1(debug))
            input("Press Any Key To Continue")
            
        elif choice == "story2":
            print(Story2.Story2(debug))
            input("Press Any Key To Continue")
            
        elif choice == "naughty":
            print("Naughty Mode ON")
            Lists.swearlist = []

Madlibs()
