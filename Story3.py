#Kyles Story
import Getters

def Story3(debug=False):
	if debug: print("Story3 Function")
	print("\n")
	output = ""
    
    
	character1 = Getters.getMario_Character("Enter a Mario Character: ")
	action1 = Getters.getAction("Enter a synonym for jummped: ")
	number1 = Getters.getNumber(1,11)
	vehicle1 = Getters.getVehicle("Enter a vehicle type: ")
	color1 = Getters.getColor("Enter a color: ")
	character2 = Getters.getMario_Character("Enter a Second Mario Character: ")
	vehicle2 = Getters.getVehicle("Enter a vehicle type: ")
	number2 = Getters.getNumber(1,11)
	SFL1 = Getters.getSFL("Enter a synonym for large: ")
	villain1 = Getters.getMario_Villains("Enter a Mario Villain: ")
	number3 = Getters.getNumber(1,25)
	noun1 = Getters.getWord("Enter a restauraunt name: ")
	
	print("\n")
	output = ""
	output += "Peach's rescue:\n"
 
	output += "When "+character1+" woke up one day, they realized Peach was gone.\n"

	output += "Obviously, "+character1+" had to go and try to find her.\n"
 
	output += "They "+action1+" out of bed and ran out the door at "+str(number1)+" miles per hour.\n"
   
	output += "So, they hopped in their "+vehicle1+" which was "+color1+", and started towards Bowser's castle, where they knew Peach was\n"
 
	output += ""+character1+" decided to meet up with "+character2+" who was in their "+vehicle2+" and kept on going.\n"
   
	output += "When they arrived at Bowser's castle, they realized that the bridge across the firey pit of lava was "+str(number2)+" miles long.\n"
   
	output += "They crossed the bridge with no problems, but when they stood in front of the castle itself, they were unsure they would be able to save peach.\n"
  
	output += "The Castle was "+SFL1+" ! they thought as they stared down the hallway towards Bowser's throne.\n"

	output += "They walked down the hallway of the castle when they were encountered by "+villain1+" \n"

	output += ""+character1+" and "+character2+" fought off "+villain1+" pretty easily, and kept moving.\n"
   
	output += "Finally, after "+str(number3)+" hours of walking, they came to the throne, where Bowser sat.\n"
    
	output += "Fortunately, "+character2+" brought a weapon for themselves and for "+character1+".\n"
    
	output += "The battle began, Bowser using his magic to try and fend off "+character1+" and "+character2+".\n"
  
	output += ""+character1+" and "+character2+" defeated Bowser using their magic powers and found peach in the basement below Bowser's castle.\n"
 
	output += "Peach was so thankful to see "+character1+" and "+character2+" and be successfully freed from her cage!\n"
    
	output += "All three of the friends left the castle with no more encounters and decided to celebrate by going to "+noun1+"\n"
		
    
    
    
   
	return output

