from player import Player
import random

#constants
w, l = 8, 8

#lists
firearms = ["a M1911", "a Glock 17", "a rusty revolver"]
melee = ["a sword", "a hunting knife", "a butter knife"]
items = [
    "a compass",
    "a hundred dollar bill",
    "a full garbage bag",
    "a bag",
    "a baby"
]

#player inventory
inventory = ["a M1911", "a butter knife"]

#creating map
gameMap = [["⬛️" for i in range(w)] for j in range(l)]

#creating player
player = Player(0, 0, "⚪️", gameMap, firearms, melee, items, inventory)

#locations on the map
locations = ["🌳", "💥", "🏠"]

#chance of each location spawning on the map
chance = [35, 15, 50]

#no. of locations
spawnNumber = 62

#spawn finalBoss
gameMap[7][7] = "😈"

#instructions
print("\nHello adventurer, welcome to Cursed Neighborhood!")

print("\nBackstory: you wake up one day and realize that your neighborhood has been cursed by the Riddler\nyou are unable to leave because of a force field around the town\nyou must kill him to rid your town of the curse")

print(
"""
Your goal is to reach the 😈 and fight it with a secret weapon.
Your current location is ⚪️ starting at the top left corner of the map
Items can be purchased or sold at any 💥 trading shops
Loot 🏠 houses to gain items
The 🌳 park is a dangerous place and make wise choices if you wish to continue

Commands: 
inventory: this will show you a list of everything in your inventory
cash: this will show your bank balance
instructions: this will repeat the instructions

Movement:
up: move up
right: move right
down: move down
left: move left
""")
print("\nHave fun and good luck!\n")

#show map
def showMap():
    for i in range(w):
        for j in range(l):
            print(gameMap[i][j], end="  ")
        print("\n")
    
#generate random coordinates and check if the coordinates are unoccupied
def locationPosition():
    x = random.randint(0, w - 1)
    y = random.randint(0, l - 1)
    pos = [x, y]

    if gameMap[pos[0]][pos[1]] == "⬛️":
        return pos
    else:
        return locationPosition()


#find number of locations based on chance list, n = number of locations to spawn
def spawnRate(n):
    #location spawn is a list of the number of times each location will spawn based on the chance list
    locationSpawn = [] 
    for i in range(len(chance)):
        #spawn number is a way to find the number of locations based on the chance list
        spawnNumber = (chance[i] / 100) * n
        locationSpawn.append(round(spawnNumber))
    
    return locationSpawn

#spawn locations based on spawnRate function, n = number of locations to spawn
def spawn(n):
    #runs a loop for the number of times a 
    for i in range(len(spawnRate(len(locations)))):
        for j in range(spawnRate(n)[i]):
            pos = locationPosition()
            gameMap[pos[0]][pos[1]] = locations[i]


#initial function calls
spawn(spawnNumber)
showMap()


def main():
    #game loop
    while player.game:
        direction = input("what would you like to do: ")
        player.move(direction, w, locations)
        print() 
        showMap()


if __name__ == "__main__":
    main()