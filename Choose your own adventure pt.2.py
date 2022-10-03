





#Sets text to type slowly
import sys,time

def sprint(str):
   for c in str + '\n':
     sys.stdout.write(c)
     sys.stdout.flush()
     time.sleep(3./90)






























def door1():
   sprint("The old oak door cracks as you push against it.")
   sprint("After some force, it heaves open")
   sprint("When your eyes adjust to the darkness of the room, you can see a table up against the wall to your left.")
   sprint("Infront of you underneath a window lies a small bed, and a closet is set into the wall on your right")
   if (assist_mode == help):
       print("Choices are bed/closet/table")
   
if answer.lower().strip == "yes":
   
else:
   print("thats not right!")
  
input("") 
   
def door2():
   sprint("The smell of the fresh paint burns you nostrils, as you get closer.")
   sprint("You begin to push the door open, and your hands become colder")
   sprint("Your hands are coverd in red pait")
   sprint("When you step into the doorway, you are frightend by what you see.")
   sprint("Against the wall there is a skeleton chained to the wall, to the left is a toilet, and at your feet the bucket of red paint")
   sprint("You hear a loud crash as the door shuts behind you and you hear the lock turn, trapping you inside the room"
   if (assist_mode == help):
       print("Choices are paint/toilet/skeleton")
          
if answer.lower().strip == "yes":
   
else:
   print("thats not right!")
   
   input("")
          
def door3():
   sprint("As you try to push the door open, it doesn't move")
   sprint("You look around the room and find a crobar")
   sprint("Use the crobar to open the door")
   sprint("When you step into the room the crobar in you hand turns to dust")
   sprint("In the room you see a large cage filled with shrews, and crickets")
   sprint("On another wall you see a breaker box, and a chalkboard with a large math equation"
   if (assist_mode == help):
       print("Choices are cage/breaker/chalkboard")
   
 if answer.lower().strip == "yes":
   
else:
   print("thats not right!")      
          
   input("") 







def t2():

   print("Dagon: Correct,", user, ",let us continue.")
   sprint("A vortex opens up above you, and after a series of twists and turns...")
   sprint("You find yourself back in your home, the warmth of a past fire still emminating from coals in the fireplace")
   sprint("The room has a simple layout, with a front door behind you, and two doors on either side of the fireplace.")
   sprint("Dagon: Now, not every choice is night and day, some can branch off into different paths.")
   if (assist_mode == "help" or "devskip"):
       sprint("Choices are left/right/behind")
   door_choice=input("Where do you go? ")
  
   if (door_choice == "left"):
       sprint("You step over to the left door")
       sprint("The door infront of you is riddled with scratches up and down it's weathered oak boards.")
       door1()
   elif(door_choice == "right"):
       sprint("You step around a couch, and over to the right door")
       sprint("The door infront of you is covered in a fresh coat of red paint. A smell of fresh steak lingers in the air.")
       door2()
   elif(door_choice == "behind"):
       sprint("You turn around, and step towards the door behind you")
       sprint("The door infront of you is a solid oak door, with bands of iron running up and down its face.")
       sprint("A small window sits in the center, and through the door you can hear the clicking and screaching of crickets")
       door3()









     
def t1():
  
  sprint("Infront of you are two doors, one on the left, the other on the right")
  if (assist_mode == "help"):
     sprint("Choices are: left/right")
  choice=input("Where do you go ")
  
  if (choice == "left"):
    sprint("You go left")
    sprint("...")
    sprint("And fall into a pit of vipers")
    sprint("You are dead")
    sprint("Dagon: It appears you have died. Don't worry, I can restart your progress from the last checkpoint. ")
    sprint("Dagon: When you get back, go Right")
    input("type anything to continue ")
    t1()
  elif (choice == "right"):
    sprint("You go right")
    sprint("...")
    sprint("You find yourself in a room, small, and dark.")
    sprint("A voice booms above you")
    t2()
  else:
    print("Dagon: Sorry, You can't do that.")
    t1()

sprint("Hello Adventurer, I am Dagon, and I am here to guide you on an adventure")
sprint("Dagon: Before we begin, I am going to need your name")

user=input("What is your name? ")

print("Dagon: Ahhhhh,", user, ",that is an interesting name")
sprint("Dagon: Now two rules. First, always anwser in lowercase. Second, Have Fun")
assist_mode=input("Dagon: Finally, if you feel you need help finding things to interact with, Type (help) ")
if (assist_mode == "devskip"):#allows dev to skip ahead
    t2()
sprint("Dagon: Now that we know each other, and the rules, lets get to the adventure")
sprint("Dagon: Here are two doors, one leads to doom, the other will further the journey")
sprint("Dagon: For now, let's go left")
t1()

