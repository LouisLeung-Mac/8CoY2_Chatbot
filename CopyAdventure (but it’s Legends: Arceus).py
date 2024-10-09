# Adventure Game

welcome = "Welcome adventurer!"
print(Welcome)

forest = print("you find yoursef in a deep dark forest in the Coronet Highlands, a foggy, misty place never explored in the slopes west of Moonview Arena below the territory of an Alpha Sneasler")
print(Forest in the Coronet Highlands)
summit = "You are in Cloudcap Pass near the summit, you see the Stone Portal near you and the snowy slopes"
plains = "you find yourself in a grassy plain of the plateau, there's spruce trees and ruins nearby"
Stone Portal = "you entered the portal and it seems to be very dark, and it's hard to see"
torchCave = "you see your path even clearer and you saw a mark of the different noble and ride pokemon blessed engraved on the walls as you walk up the Stone Portal"
Fly = "it doesn't seem you can use Braviary to fly here... the woods are too dense and dark to coordinate."
cliffs = "you see rows of small cliffs and slopes with graveyard, and a creepy, hazardous Alpha Mismagius seems to be wandering around"
inventory = []

# Logic
print(it seems dark here at sunset... you seem unfamiliar with this place as if you've never been here in your expedition in the highlands)
print(a deep dark forest admist somewhere...)

# move northeast up, east up, southeast, summit camp or fly
move = input("which direction do you want to go?")
if move == "northeast up":
  Higher Up = "you are in the Coronet Highlands near the snowy mountains, you see stone portal"
  print(Cloudcap Pass)
  goPortal == input("would you like to enter the cave?")
  if goCave == "yes"
     if "torch" in inventory:
       print(torchCave)
     print(Stone Portal)
elif move == "East up":
  plains = "you find yourself in a grassy plain of the plateau, there's spruce trees and ruins nearby"
  print(Sacred Plaza, Celestial Ruins)
  if not "torch" in inventory:
    print("There's a torch on the floor")
    pickup = input("do you want to pick up the torch?")
    if pickup == "yes"
      inventory.append("torch")
elif move == "Southeast"
   cliffs = "you are now in stonetooth rows after walking out the forested slope, and you see an Alpha Mismagius focused on you suspiciousy near the graves"
   print(Stonetooth Rows)
   approach with caution == input("are you sure you want to approach and sneak to the tall grass of one of the cliff rows?")
   if approach with caution == "yes"
     print("You decided to approach with caution. Mismagius seems to be confused and gets curious, and you are in great danger.")
   elif approach with caution == "no"
     print("You decided to approach it another time. Better head somewhere else back in the woods...")
elif move == Summit Camp
    summit camp = "You walk through Moonview Arena out of the misty forest to the camp, as Professor Laventon looks at you curiously. He asks you whether you have anything to report about the forest seeing you clearly creeped out by the woods."
 
