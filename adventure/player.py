from random import randint
from time import sleep

def chance(n):
    m = randint(1, 100)
    if m < n:
        return True
    else:
        return False

def rockPaperScissors():
    print("rock, paper or scissor?")
    choice = int(input("1. rock\n2. paper\n3. scissor\n"))
    chance = randint(0, 2)
    if choice == 1 and chance == 0:
        print("you both picked rock")
        rockPaperScissors()
    elif choice == 1 and chance == 1:
        print("your opponent picked paper\nyou lose")
        return False
    elif choice == 1 and chance == 2:
        print("your opponent picked scissor\nyou win")
        return True
    elif choice == 2 and chance == 0:
        print("your opponent picked rock\nyou win")
        return True
    elif choice == 2 and chance == 1:
        print("you both picked paper")
        rockPaperScissors()
    elif choice == 2 and chance == 2:
        print("your opponent picked scissor\nyou lose")
        return False
    elif choice == 3 and chance == 0:
        print("your opponent picked rock\nyou lose")
        return False
    elif choice == 3 and chance == 1:
        print("your opponent picked paper\nyou win")
        return True
    elif choice == 3 and chance == 2:
        print("you both picked scissor")
        rockPaperScissors()


class Player:
    def __init__(self, x, y, image, minimap, firearms, melee, items, inventory):
        self.x = x
        self.y = y
        self.image = image
        self.map = minimap
        self.firearms = firearms
        self.melee = melee
        self.items = items
        self.inventory = inventory
        self.cash = 50

        self.game = True
        
        self.map[self.x][self.y] = self.image

    def inventoryAccess(self):
        print("\nyour inventory currently consists of: \n")
        for i in range(len(self.inventory)):
            print(f"{i + 1}. {self.inventory[i]}")
        print()
    
    def cashBalance(self):
        print(f"\nyour bank balance is currently {self.cash}\n")

    def instructions(self):
        print(
        """
  
        Your current location is ⚪️ starting at the top left corner of the map
        Items can be purchased or sold at any 💥 trading shops
        Loot 🏠 houses to gain items
        The 🌳 park is a dangerous place and make wise choices if you wish to continue
        Your goal is to reach the 😈 and beat it with a secret weapon bought from a 💥 trading shop

        Commands: 
        inventory: this will show you a list of everything in your inventory
        cash: this will show your bank balance
        instructions: this will repeat the instructions
        """)

    def bossFight(self, dialogueBoss, secretWeapon):
        print(dialogueBoss)

        t = 1.5

        if secretWeapon == 0:
            print("as you walk up to the Riddler, he notices that you haven't brought a rare weapon to fight him")
            sleep(t)
            print("Riddler: 'so you've come here just to die huh? Well, your decision I suppose'")
            sleep(t)

        elif secretWeapon == 3:
            secretWeaponStr = "Ancient Sword of Lies and Secret Trident of Truth"
            print("as you walk up to the Riddler, he notices your Secret Trident of Truth and your Ancient Sword of Lies")
            sleep(0.5)
            print("he becomes visibly nervous and takes a step back")
            sleep(0.5)
        else:
            if secretWeapon == 1:
                secretWeaponStr = "Ancient Sword of Lies"
            elif secretWeapon == 2:
                secretWeaponStr = "Secret Trident of Truth"
            print(f"as you walk up to the Riddler, he notices your {secretWeaponStr}")
            sleep(t)
            print("Riddler: 'you came well prepared I see'")
            sleep(t)

        print("'the Riddler opens up his jacket and pulls out a card'")
        sleep(t)
        print("he throws it at you")
        sleep(t)

        a = int(input("do you:\n1. dodge\n2. deflect with secret weapon\n"))
        if a == 1:
            print("you dodge the flying card and it impacts a wall behind you, shattering it")
            sleep(t)
            print("Riddler: 'so you can dodge it seems, but can you also fight?'")
            sleep(t)

        elif a == 2:
            if secretWeapon == 0:
                print("as you have no secret weapon, the card is not stopped by you and impacts against your chest, fatally wounding you")
                sleep(t)
                print("the Riddler comes closer to you")
                sleep(t)
                print("Riddler: 'I shouldn't have expected anything from you'")
                sleep(t)
                print("he then walks away, leaving you to your fate")
                sleep(t)
                print("nice try, better luck next time")
                self.game = False
            elif secretWeapon == 1 or 2:
                print(f"you pull out your {secretWeaponStr}")
                sleep(t)
                print(f"the card impacts your {secretWeaponStr} and crumbles into a million pieces")
                sleep(t)
                print("the Riddler is impressed by your capabilities")
                sleep(t)
            else:
                print(f"you pull out both your {secretWeaponStr}")
                sleep(t)
                print("the power of both weapons combined force the card to stop midair")
                sleep(t)
                print("the Riddler is shocked at your ability")
                sleep(t)
        
        print("as you calm down from the adrenaline rush, you realize the Riddler turned his back towards you")
        b = int(input("do you:\n1. rush him\n2. taunt him\n"))
        if b == 1:
            if secretWeapon == 0:
                print("you fumble around in your bag to find a weapon to rush him with")
                weaponChoice = self.fight("the weapon you chose is useless", "as you have nothing to fight him with, he turns around and kills you")
                sleep(t)
                if  weaponChoice == "firearm":
                    print("you pull out a gun and shoot him in the back, killing him")
                    sleep(t)
                    print("well done, you have killed the Riddler and freed your town from his curse")
                    self.game = False
                    quit()
                elif weaponChoice == "melee":
                    print("you pull out a melee weapon and charge him")
                    sleep(t)
                    print("the Riddler turns around and you stab him, killing him")
                    sleep(t)
                    print("well done, you have killed the Riddler and freed your town from his curse")
                    self.game = False
                    quit()
            elif secretWeapon == 3:
                print(f"you charge towards him with your {secretWeaponStr} and stab him in the back")
                sleep(t)
                print("he dies without making a single noise")
                sleep(t)
                print("well done, you have killed the Riddler and freed your town from his curse")
                self.game = False
                quit()
            elif secretWeapon == 1 or 2:
                print(f"you charge towards him with your {secretWeaponStr} and stab him in the back")
                sleep(t)
                print("he dies without making a single noise")
                sleep(t)
                print("well done, you have killed the Riddler and freed your town from his curse")
                self.game = False
                quit()
        elif b == 2:
            print("you make fun of his card throwing trick and this angers him")
            sleep(t)
            print("Riddler: 'that was my best trick, how dare you insult me'")
            sleep(t)
            print("Riddler: 'now you're going to pay'")
            sleep(t)
            print("the Riddler suddenly charges you")
            sleep(t)
            
            if secretWeapon == 0:
                print("since you have nothing to defend yourself, he grabs you and throws you against the ground, fatally wounding you")
                sleep(t)
                print("he laughs as you slowly die")
                sleep(t)
                print("nice try, better luck next time")
                self.game = False
            else:
                print(f"you use your {secretWeaponStr}")
                print("you slash the Riddler and he crumbles to the ground, revealing to be the local homeless man from the park")
                sleep(t)
                print("Riddler: 'you... you... you slashed me... aughh'")
                sleep(t)
                print("the Riddler dies")
                sleep(t)
                print("well done, you have killed the Riddler and freed your town from his curse")
                self.game = False
                quit()


    def boss(self):
        t = 1.5

        # Ancient Sword of Lies - Secret Trident of Truth
        riddles = [
            '\n"The more you take, the more you leave behind. What am I?"\n', 
            '\n"I am always hungry, I must always be fed. The finger I touch, will soon turn red. What am I?"\n',
            '\n"I speak without a mouth and hear without ears. I have no body, but I come to life with a hollow wind. What am I?"\n',
        ]   
        truthAnswers = [
            "footsteps",
            "fire",
            "echo"
        ]
        lieAnswers = [
            "money",
            "greed",
            "scream"
        ]

        asl = "Ancient Sword of Lies"
        stt = "Secret Trident of Truth"
        
        # variable to check which weapon the player has when fighting the boss
        w = 0


        if asl in self.inventory and stt in self.inventory:
            dialogue = "the " + asl + " and the " + stt
            w = 3
        elif asl in self.inventory:
            dialogue = "the " + asl
            w = 1
        elif stt in self.inventory:
            dialogue = "the " + stt
            w = 2
        else:
            dialogue = "nothing"
        
        
        print(f"you confidently walk into the lair with the {dialogue}")
        sleep(t)
        print("you see the Holy Riddler sitting in his chair, motionlessly")
        sleep(t)
        print("Riddler: 'I've been expecting you'")
        sleep(t)
        print("you approach him, cautiously")
        sleep(t)
        print("Riddler: 'I know why you're here and I will not try to stop you'")
        sleep(t)
        print("Riddler: 'You are here to kill me, but let me ask you some questions'")
        sleep(t)
        print("Riddler: 'as the Riddler, here are some riddles'")
        sleep(t)
        riddleNum = randint(0, len(riddles)-1)
        riddle = riddles[riddleNum]
        print(riddle)
        print("you repeat the riddle to yourself")
        if w == 3:
            print("suddenly, the Secret Trident of Truth shakes vigorously and falls to the ground transforming into a scroll.")
            sleep(t)
            print("you open the ancient scroll and read: \n")
            sleep(t)
            print()
            for i in range(len(truthAnswers)):
                print(" - ", truthAnswers[i])
            print()
            sleep(t)
            print("the Ancient Sword of Lies proceeds to also begins to shake vigorously and slams onto the ground and expands into a scroll")
            sleep(t)
            print("you open this scroll and read: ")
            sleep(t)
            print()
            for i in range(len(lieAnswers)):
                print(" - ", lieAnswers[i])
            print()
        elif w == 1:
            print("the Ancient Sword of Lies proceeds to also begins to shake vigorously and slams onto the ground and expands into a scroll")
            sleep(t)
            print("you open this scroll and read: ")
            sleep(t)
            print()
            for i in range(len(lieAnswers)):
                print(" - ", lieAnswers[i])
            print()
        elif w == 2:
            print("suddenly, the Secret Trident of Truth shakes vigorously and falls to the ground transforming into a scroll.")
            sleep(t)
            print("you open the ancient scroll and read: ")
            sleep(t)
            print()
            for i in range(len(truthAnswers)):
                print(" - ", truthAnswers[i])
            print()
        else:
            print("since you have no secret weapon, you must answer the riddle without any help")
            sleep(t)
        
        a = input("what is your answer?: ") # can change into int
        if a == truthAnswers[riddleNum]:
            print("the Riddler looks suprised as you say your response")
            sleep(t)
            print("Riddler: 'impressive, for someone like you'")
            sleep(t)
            b = int(input("do you:\n1. ask for another riddle\n2. fight him\n"))
            if b == 1:
                riddles.remove(riddles[riddleNum])
                truthAnswers.remove(truthAnswers[riddleNum])
                lieAnswers.remove(lieAnswers[riddleNum])
                
                print("Riddler: 'ah, you are a curious one I see'")
                sleep(t)
                print("Riddler: 'well then, here you go:'")
                riddleNum = randint(0, len(riddles)-1)
                riddle = riddles[riddleNum]
                print(riddle)
                if w == 3:
                    print("the Secret Trident's scroll changes and reads: ")
                    sleep(t)
                    print()
                    for i in range(len(truthAnswers)):
                        print(" - ", truthAnswers[i])
                    print()
                    print("the Ancient Sword's scroll changes as well and reads: ")
                    sleep(t)
                    print()
                    for i in range(len(lieAnswers)):
                        print(" - ", lieAnswers[i])
                    print()
                elif w == 1:
                    print("the Ancient Sword's scroll changes and reads: ")
                    sleep(t)
                    print()
                    for i in range(len(lieAnswers)):
                        print(" - ", lieAnswers[i])
                    print()
                elif w == 2:
                    print("the Secret Trident's scroll changes and reads: ")
                    sleep(t)
                    print()
                    for i in range(len(truthAnswers)):
                        print(" - ", truthAnswers[i])
                    print()
                else:
                    print("since you still have no secret weapon, you must answer the riddle without any help")

                c = input("what is your answer?: ")
                if c == truthAnswers[riddleNum]:
                    print("Riddler: 'wow, you really are intelligent'")
                    print("Riddler: 'how would you like to join me and rule over these other peasants?'")
                    d = int(input("1. join him\n2. leave him\n"))
                    if d == 1:
                        print("Riddler: 'you made the right choice my friend'")
                        sleep(t)
                        print("you walk up the steps towards the top of his lair, looking down at the town below you")
                        sleep(t)
                        print("you and the Riddler, sitting next to each other, commence the brutal dictatorship that will plague this town for the next fifty years")
                        sleep(1)
                        print("well done! you've beat the game by screwing over every other resident of this city!")
                        self.game = False
                        quit()
                    elif d == 2:
                        print("you say you would rather leave this forsaken place")
                        sleep(t)
                        print("Riddler: 'I respect your decision, here, follow me, the way out is around the corner'")
                        sleep(t)
                        print("you leave the stricken town, into the vast green pastures of the Midwest")
                        sleep(t)
                        print("you look back, seeing the Riddler standing by the entrance")
                        sleep(t)
                        print("you realize that the nightmare has ended and you are finally free")
                        sleep(t)
                        print("well done! You've beat the game!")
                        self.game = False
                        quit()
                else:
                    print("Riddler: 'ah tough luck, wrong my friend, but I appreciate your try'")
                    sleep(t)
                    print("Riddler: 'I guess you aren't the man I was looking for'")
                    if self.bossFight("Riddler: 'I guess it is time to fight so bring it on!'", w):
                        print("well done!, You've beat the game and liberated your neighborhood from the Riddler's curse")
                        self.game = False
                    else:
                        print("nice try, better luck next time")
                        self.game = False
            elif b == 2:
                if self.bossFight("Riddler: 'hmm, so you want to fight me? Well then, lets bring it on!'", w):
                    print("well done!, You've beat the game and liberated your neighborhood from the Riddler's curse")
                    self.game = False
                else:
                    print("nice try, better luck next time")
                    self.game = False
        else: # not done
            print("Riddler: 'that wasn't what I was looking for'")
            sleep(t)
            print("Riddler: 'we both know why you're here'")
            sleep(t)
            if self.bossFight("Riddler: 'so lets fight then!'", w):
                print("well done!, You've beat the game and liberated your neighborhood from the Riddler's curse")
                self.game = False
            else:
                print("nice try, better luck next time")
                self.game = False
    


# y = text printed when you select a useless weapon in a fight, z = text printed when you have nothing in your inventory, e = if the game ends during an if condition
    def fight(self, y, z, e):
        if self.inventory:
            self.inventoryAccess()
            weapon = int(input("\nwhat would you like to use: "))

            if self.inventory[weapon - 1] in self.firearms:
                return "firearm"
            elif self.inventory[weapon - 1] in self.melee:
                return "melee"
            else:
                print("the item you selected is useless in a fight")
                print(y)
                if e:
                    self.game = False
    
        else:
            print(z)
            self.game = False



    def insult(self, dialogue):
        gender = ["man", "woman"]
        
        person = gender[randint(0, 1)]
        
        if person == "man":
            #p = object pronoun, q = subject pronoun, r = possessive pronoun 
            p = "him"
            q = "he"
            r = "his"
        elif person == "woman":
            p = "her"
            q = "she"
            r = "her"
        if dialogue:           
            insultNoun = ["fool", "idiot", "dork", "jerk", "simpleton"]
            insultAdjective = [
                            "stupid", 
                            "repulsive",
                            "depressed",
                            "disgusting",
                            "boring",
                            "drunken",
                            "thoughtless",
                            "reckless",
                            "hideous"
                            ]
            print(f"you call the {person} a {insultAdjective[randint(0,len(insultAdjective)-1)]} {insultNoun[randint(0,len(insultNoun)-1)]}")
        else:
            complimentAdjective = [
                            "nice",
                            "friendly",
                            "praiseworthy",
                            "happy",
                            "beautiful",
                            "smart",
                            "charming"
                        ]
            print(f"you call the {person} a {complimentAdjective[randint(0, len(complimentAdjective)-1)]} {person}")

    def encounters(self, n):
        if n == 0:
            print("\nyou entered a 🌳 park")

            #make four scenarios that are chosen at random when you enter a park
            possibilities = randint(1, 4)  
            
            if possibilities == 1:
                scenario = "\na rabid dog is approaching you quickly."
                print(scenario)

                a = int(input("1. fight the dog\n2. run away from the dog\n3. pet the dog\n"))
                
                if chance(30):
                    y = "you managed to scare the dog away with your item"
                    e = False
                else:
                    y = "the dog was not scared of your item and attacked you"
                    e = True

                if a == 1:
                    b = self.fight(y, "you have nothing to fight the dog with so he attacked you", e)

                    if b == "firearm":
                        c = int(input("\nwhere would you like to shoot:\n1. body\n2. legs\n3. head\n"))
                        
                        if c == 1:
                            if chance(80):
                                print("you hit the dog in the body and it fell to the ground")
                            else:
                                print("the dog was too fast and you missed your shot")
                                if chance(30):
                                    print("you ran away as soon as you missed your shot and lost the dog in the forest")
                                else:
                                    print("the dog jumped on you and bit you in the neck")
                                    self.game = False
                        elif c == 2:
                            if chance(20):
                                print("you have a PHD in physics and shot him perfectly in the leg")
                            else:
                                print("the legs are a very small target and you miss your shot")
                                if chance(30):
                                    print("you ran away as soon as you missed your shot and lost the dog in the forest")
                                else:
                                    print("the dog jumped on you and bit you in the neck")
                                    self.game = False
                        elif c == 3:
                            if chance(50):
                                print("the only thing you see is the dog's head as he is running towards you and you do not miss")
                            else:
                                print("the dog moves left and right and you miss your shot")
                                if chance(30):
                                    print("you ran away as soon as you missed your shot and lost the dog in the forest")
                                else:
                                    print("the dog jumped on you and bit you in the neck")
                                    self.game = False

                    
                    if b == "melee":
                        c = int(input("1. attack the dog\n2. defend yourself\n"))

                        if c == 1:
                            if chance(80):
                                print("you come up close to the dog and use your melee weapon to injure it and you walk away")
                            else:
                                print("the dog bit your hand and you had no choice but to fight him with your wrists")
                                if chance(30):
                                    print("you go crazy punching the dog and he runs away injured and scared")
                                else:
                                    print("you stand no chance against a rabid dog and he attacks you and kills you")
                                    self.game = False
                        elif c == 2:
                            if chance(80):
                                print("the dog is scared of your weapon and he backs off")
                            else:
                                print("the dog is not scared of your weapon and he jumps on you before you can react")
                                if chance(30):
                                    print("you push the dog into a bush and run away")
                                else:
                                    print("the dog attacks you and you die")
                                    self.game = False

                elif a == 2:
                    b = int(input("1. climb a tree\n2. run to the forest\n"))
                    
                    if b == 1:
                        if chance(90):
                            print("the dog is too heavy to climb the tree and you rest as you watch the dog walk away")
                        else:
                            print("the dog is able to climb the tree")
                            c = self.fight(y, "you have nothing to fight the dog with so he attacked you", e)

                            if c == "firearm":
                                if chance(50):
                                    print("you shoot the dog before he climbs all the way up")
                                else:
                                    print("you didn't have enough time to pull the trigger and the rabid dog kills you")
                                    self.game = False

                            if c == "melee":
                                if chance(50):
                                    print("the dog is scared to climb any further and falls to the ground")
                                else:
                                    print("the dog grabbed the melee weapon with his teeth and threw it down to the ground and killed you")
                                    self.game = False

                    elif b == 2:
                        if chance(90):
                            if "a compass" in self.inventory:
                                print("you use the compass to find your way back to where you were and continue your journey")
                                for i in self.inventory:
                                    if i == "a compass":
                                        del i
                            else:
                                print("you manage to lose the dog in the forest but now you are lost and can no longer access a trading shop")
                                count = 0
                                for i in range(8):
                                    for j in range(8):
                                        if self.map[i][j] == "💥":
                                            self.map[i][j] = "🏠"
                                            count += 1
                                        if count > 0:
                                            break
                                
                        else:
                            print("you are too slow to run away from the dog and he catches up to you and kills you")
                            self.game = False
                
                elif a == 3:
                    if chance(70):
                        print("the dog turns out to be friendly and you enjoy your walk in the park")
                    else:
                        b = int(input("as you try to pet the dog another dog comes and attacks it, what would you like to do: \n1. run away\n2. help the rabid dog\n"))
                        
                        if b == 1:
                            if chance(90):
                                print("you walk away from the conflict unharmed")

                            else:
                                print("the two dogs chase you down and kill you")
                                self.game = False

                        elif b == 2:
                            print("you try to go help the rabid dog but they coordinate an attack on you and kill you")
                            self.game = False


            elif possibilities == 2:
                scenario = "\nwhile you are walking in the park you see a suspicious man."
                print(scenario)
 
                a = int(input("1. approach him\n2. avoid eye-contact\n3. fight him\n"))

                if a == 1:
                    if chance(60):
                        print("he greets you kindly and offers you a folded newspaper with an odorous content")
                        b = int(input("would you like to: \n1. accept\n2. reject\n"))
                        
                        if b == 1:
                            if chance(60):
                                print("you recieve the newspaper")
                                self.inventory.append("a newspaper wrap")
                            else:
                                print("it turns out to be a sting operation and you are arrested for buying drugs")
                                self.game = False
                                
                        elif b == 2:
                            print("you reject the offer and walk away")
                    else:
                        item = self.items[randint(0, len(self.items)-1)]
                        print("he greets you and you two have a lovely conversation")
                        print(f"as a parting gift, he gives you {item}")
                        self.inventory.append(item)

                elif a == 2:
                    if chance(60):
                        print("as you are walking past him you avoid eye-contact")
                    else:
                        print("he thinks you are a cop and pulls out his rusty revolver")
                        b = int(input("1. fight\n2. run away\n"))
                        if b == 1:
                            c = self.fight("he shoots you without hesitation", "he shoots you without hesitation", True)
                            
                            if c == "firearm":
                                if chance(85):
                                    print("your gun did more damage than his rusty revolver and you kill him and pick up his gun")
                                    self.inventory.append("a rusty revolver")
                                else:
                                    print("your aim is terrible and you miss the man right in front of you; he kills you")
                                    self.game = False

                            if c == "melee":
                                if chance(75):
                                    print("he pulls out his knife and you have a knife fight")
                                    if chance(70):
                                        print("he sucks at knife handling and you manage to wound him and steal his weapon")
                                        self.inventory.append("a hunting knife")
                                    else:
                                        print("he starts laughing with his rusty revolver in his hands")
                                        if chance(40):
                                            print("you quickly stab him as he is distracted and grab his gun")
                                            self.inventory.append("a rusty revolver")
                                        else:
                                            print("he quickly pulls the trigger before you can react")
                                            self.game = False
                        elif b == 2:
                            if chance(80):
                                print("you run away quickly before he can shoot")
                            else:
                                print("he is a menace and lets you run for 10 metres before he shoots you")
                                self.game = False

                elif a == 3:
                    print("he turns out to be a gang leader and calls his gang members to come and kill you")
                    b = int(input("1. run\n2. fight\n"))
                    
                    if b == 1:
                        if chance(75):
                            print("you manage to run away before the gang member come")
                        else:
                            print("the gang leader grabs you and kills you")
                            self.game = False
                        
                    elif b == 2:
                        c = self.fight("he pulls out his revolver and shoots you", "he pulls out his revolver and shoots you", True)

                        if c == "firearm":
                            if chance(70):
                                print("you fight off 10 men with your gun and you pick up a couple guns before the police came")
                                for i in range(randint(0, 4)):
                                    self.inventory.append(self.firearms[randint(0, len(self.firearms))])
                            else:
                                print("you had no chance against gang members and they come and kill you")
                                self.game = False

                        if c == "melee":
                            if chance(40):
                                print("you are nice with your melee weapon and you wound a couple and run away before the rest of them came")
                            else:
                                print("they all pulled out their guns and at that moment you knew it was over")
                                self.game = False

            elif possibilities == 3:
                scenario = "\nas you enter the park you see a homeless man sleeping on the ground."
                print(scenario)

                a = int(input("1. fight\n2. give him money\n3. avoid eye-contact\n"))

                if a == 1:
                    b = self.fight("you both realize you have nothing useful to fight with and part your ways", "he attacks you with his garbage bag and steals your gun which he uses to shoot you", False)

                    if b == "firearm":
                        c = int(input("\nwhere would you like to shoot:\n1. body\n2. legs\n3. head\n"))
                        if c == 1:
                            if chance(85):
                                print("you shoot and kill him and rummage through his garbage bag hoping to find something valuable")
                                if chance(30):
                                    i = self.items[randint(0, len(self.items) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                elif chance(20):
                                    i = self.melee[randint(0, len(self.melee) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                elif chance(10):
                                    i = self.melee[randint(0, len(self.melee) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                else:
                                    print("you found nothing valuable in his garbage bag")    
                            else:
                                print("he blocks your shot with his garbage bag and quickly runs away")
                        
                        elif c == 2:
                            if chance(85):
                                print("his legs are unprotected so it is a clear shot and you take it")
                                print("he starts begging for his life and the police come by trying to arrest you, however you manage to quickly run away")
                            else:
                                print("he moves his leg and gets scared from the shot")
                                print("the police hear the gun shot and quickly rush over to see what happened")
                                print("they find you holding the gun and quickly arrest you")
                                self.game = False

                        elif c == 3:
                            if chance(90):
                                print("you shoot him and rummage through his garbage bag hoping to find something valuable")
                                if chance(30):
                                    i = self.items[randint(0, len(self.items) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                elif chance(20):
                                    i = self.melee[randint(0, len(self.melee) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                elif chance(10):
                                    i = self.melee[randint(0, len(self.melee) - 1)]
                                    print(f"you found a {i} in his garbage bag")
                                    self.inventory.append(i)
                                else:
                                    print("you found nothing valuable in his garbage bag")   
                            else:
                                print("you miss your shot and run away before the police come and arrest you") 
                                self.game = False
                        
                    if b == "melee":
                        if chance(50):
                            print("you wound the homeless man while he is sleeping and search through his bag")
                            if chance(30):
                                print("you find a rusty revolver and run away")
                                self.inventory.append("a rusty revolver")
                            else:
                                print("you find nothing but smelly garbage")
                        else:
                            print("the homeless man also pulls out a knife and you have a knife fight")
                            if chance(30):
                                print("he is very good at knife handling and manages to wound you, take your gun and shoot you")
                            else:
                                print("he doesn't know any fighting techniques and you wound him and grab his hunting knife")
                                self.inventory.append("a hunting knife")

                elif a == 2:
                    self.cashBalance()
                    b = int(input("how much would you like to donate to the homeless man: "))
                    if b > self.cash:
                        print("you do not have enough money to donate that much")
                    else:
                        print(f"you donated ${b} to the homeless man")
                        if chance(70):
                            print("he thanks you for your kind gesture")
                        else:
                            print("he hands you an item from his garbage bag in return")
                            if chance(30):
                                self.inventory.append(self.firearms[randint(0, len(self.firearms) - 1)])
                            else:
                                self.inventory.append(self.items[randint(0, len(self.items) - 1)])

                elif a == 3:
                    print("you walk by him without making eye-contact")

            elif possibilities == 4:
                scenario = "\nyou see a friend you haven't talked to in many years."
                print(scenario)

                a = int(input("would you like to:\n1. approach him\n2. walk away\n"))
                
                if a == 1:
                    if chance(80):
                        b = int(input("would you like to:\n1. play rock paper scissors\n2. have a conversation\n"))
                        if b == 1:
                            c = rockPaperScissors()
                            if c == True:
                                print("you say you had a fun time and walk away")
                            else:
                                print("you tell your friend you will beat him next time and walk away")
                        elif b == 2:
                            print("you have a lovely conversation catching up with him")
                            if chance(70):
                                item = self.items[randint(0, len(self.items)-1)]
                                print("your friend decides to give you a parting gift, he gave you ", item)
                                self.inventory.append(item)
                            else:
                                print("you say your farewells and leave")
                    else:
                        print("it turns out the man wasn't your friend, but a rival co-worker who stole your job")
                        b = int(input("would you like to:\n1. fight him\n2. insult him\n"))
                        if b == 1: 
                            c = self.fight("he pulls out a Glock 17 and kills you", "he pulls out a Glock 17 and kills you", True)   

                            if c == "firearm":
                                if chance(70):
                                    print("you pull out your gun and shot him for everything he did to you")
                                else:
                                    print("he pulls out a rusty revolver and shoots you")
                                    self.game = False

                            elif c == "melee":
                                if chance(70):
                                    print("you both pull out of ")
                            
                        elif b == 2:
                            pass
                elif a == 2:
                    print("you walk away without your friend noticing")
        
        if n == 1:
            print("\nyou entered a 💥 trading shop")
            self.cashBalance()

            a = int(input("would you like to: \n1. sell\n2. buy\n"))

            if a == 1:
                if self.inventory:
                    self.inventoryAccess()
                    b = int(input("what would you like to sell: "))

                    if self.inventory[b - 1] == self.firearms[1] or self.inventory[b - 1] == self.firearms[0]:
                        print("you sell your pistol for $100")
                        self.cash += 100
                    elif self.inventory[b - 1] == "a rusty revolver":
                        if chance(60):
                            print("you sell your rusty revolver for $50")
                            self.cash += 50
                        else:
                            print("your rusty revolver turns out to be an antique civil war revolver and you sell it for $200")
                            self.cash += 200

                    elif self.inventory[b - 1] in self.melee:
                        print("you sell your melee weapon for $75")
                        self.cash += 75

                    elif self.inventory[b - 1] == "a hundred dollar bill":
                        print("you cash in your hundred dollar bill")
                        self.cash += 100

                    elif self.inventory[b - 1] == "a baby":
                        print("you can not sell a baby, you are promptly arrested")

                    elif self.inventory[b - 1] == "a compass":
                        if chance(70):
                            print("you sell your compass for $60")
                            self.cash += 60
                        else:
                            print("your compass turns out to be an antique pirate compass and you sell it for $120")
                            self.cash += 120

                    elif self.inventory[b - 1] == "a full garbage bag" or self.inventory[b - 1] == "a bag":
                        if chance(30):
                            luckyItems = [
                                "wedding ring",
                                "gold watch",
                                "lottery ticket",
                                "laptop",
                                "small gem"
                            ]
                            c = luckyItems[randint(0, len(luckyItems)-1)]
                            print(f"in the bag you found a {c}, worth $150")
                            self.cash += 150

                        else:
                            if self.inventory[b - 1] == "a bag":
                                print("you sell the bag for $40")
                                self.cash += 40

                            elif self.inventory[b - 1] == "a full garbage bag":
                                print("you hand over your garbage bag\nthe store owner gives you a weird look\nhe takes the bag and refuses to pay you")
                    elif self.inventory[0 - 1] == "a newspaper wrap":
                        print("the storeowner questions how you got it sell the newspaper wrap for $200")
                        self.cash += 200
                    else:
                        pass
                    del self.inventory[b - 1]

            elif a == 2:
                b = int(input("what would you like to buy:\n1. firearm\n2. melee\n3. secret item\n"))
                if b == 1:
                    print("the cost of a firearm is $130")
                    self.cashBalance()
                    c = int(input("would you still like to buy it:\n1. yes\n2. no\n"))
                    if c == 1 and self.cash >= 130:
                        product = self.firearms[randint(0, 2)]
                        print(f"you purchased a {product}")
                        self.cash -= 130
                        self.inventory.append(product)
                    elif self.cash < 130:
                        print("you don't have enough money")
                if b == 2:
                    print("the cost of a melee is $80")
                    self.cashBalance()
                    c = int(input("would you still like to buy it:\n1. yes\n2. no\n"))
                    if c == 1 and self.cash >= 80:
                        product = self.melee[randint(0, 2)]
                        print(f"you purchased a {product}")
                        self.cash -= 80
                        self.inventory.append(product)
                    elif self.cash < 80:
                        print("you don't have enough money")

                if b == 3:
                    c = int(input("would you like to purchase:\n1. Secret Trident of Truth - $280\n2. Ancient Sword of Lies - $250\n"))
                    if c == 1:
                        print("the cost of the legendary Secret Trident of Truth is $280")
                        self.cashBalance()
                        if self.cash >= 280:
                            print(f"you purchased the Secret Trident of Truth")
                            self.cash -= 280
                            self.inventory.append("Secret Trident of Truth")
                        elif self.cash < 280:
                            print("you don't have enough money")
                    elif c == 2:
                        print("the cost of the legendary Ancient Sword of Lies $250")
                        self.cashBalance()
                        if self.cash >= 250:
                            print(f"you purchased the Ancient Sword of Lies")
                            self.cash -= 250
                            self.inventory.append("Ancient Sword of Lies")
                        elif self.cash < 250:
                            print("you don't have enough money")

        if n == 2:
            print("\nyou entered a 🏠 house")

            if chance(90):
                a = int(input("what would you like to do:\n1. rob the home\n2. walk away from the home\n3. greet the homeowner\n"))

                if a == 1:
                    b = int(input("would you like to:\n1. rob it during the day\n2. rob it at night\n"))
                    if b == 1:
                        if chance(75):
                            item = ""
                            if chance(40):
                                item = self.items[randint(0, len(self.items)) - 1]
                            else:
                                if chance(50):
                                    item = self.firearms[randint(0, len(self.firearms)) - 1]
                                else:
                                    item = self.melee[randint(0, len(self.melee)) - 1]
                            
                            self.inventory.append(item)
                            print(f"you are not caught breaking in and you steal {item}")
                        else:
                            print("the homeowner catches you in the act and you are swiftly reported to the police")
                            self.game = False
                    elif b == 2:
                        if chance(95):
                            item = ""
                            if chance(40):
                                item = self.items[randint(0, len(self.items)) - 1]
                            else:
                                if chance(50):
                                    item = self.firearms[randint(0, len(self.firearms)) - 1]
                                else:
                                    item = self.melee[randint(0, len(self.melee)) - 1]
                            
                            self.inventory.append(item)
                            print(f"you are not caught breaking in and you steal {item}")
                        else:
                            if chance(50):
                                print("you enter the home, it is very dark, you trip on the basement stairs and fall to your death")
                                self.game = False
                            else:
                                print("the homeowner catches you in the act and you are swiftly reported to the police")
                                self.game = False

                elif a == 2:
                    if chance(70):
                        searchable = ["trashcan", "basket", "recycling bin", "crate"]
                        print(f"as you are walking away from the home, there is a nearby {searchable[randint(0, len(searchable) - 1)]}")
                        b = int(input("would you like to:\n1. search it\n2. continue walking\n"))
                        if b == 1:
                            if chance(70):
                                item = self.items[randint(0, len(self.items) - 1)]
                                print(f"you find {item}")
                                self.inventory.append(item)
                            elif chance(60):
                                item = self.melee[randint(0, len(self.melee) - 1)]
                                print(f"you find {item}")
                                self.inventory.append(item)
                            else:
                                item = self.firearms[randint(0, len(self.firearms) - 1)]
                                print(f"you find {item}")
                                self.inventory.append(item)
                        elif b == 2:
                            print("you walk away")
                    else:
                        print("as you walk away, the homeowner sees you acting suspicously and questions why you are there")
                        c = int(input("do you:\n1. pretend to be a garbage man\n2. fight the homeowner\n"))
                        if c == 1:
                            print("you say you are a garbage man")
                            if chance(70):
                                print("the homeowner demands to see your ID")
                                d = int(input("do you:\n1. give him a false ID\n2. say you left it at home\n3. drop the act\n"))
                                if d == 1:
                                    if chance(70):
                                        print("the homeowner believes your ID")
                                        print("he gives you a full garbage bag from his home")
                                        print("you reluctantly take it and quickly walk away, under the watchful gaze of the man")
                                        if chance(60):
                                            print("you open the bag and find a $100 bill inside")
                                            self.cash += 100
                                        else:
                                            self.inventory.append("a full garbage bag")
                                    else:
                                        print("he takes a look at your crudely made false ID and instantly calls you out on it")
                                        print("he turns out to be a cop and arrests you for forging a false ID")
                                        self.game = False
                                elif d == 2:
                                    if chance(90):
                                        print("the man tells you to be more attentive next time and leaves you be")
                                    else:
                                        print("the man doesn't believe you and shoots you dead")
                                        self.game = False
                                else:
                                    print("you drop the act and challenge him to a duel of the century Dual-a-thon")
                                    d = self.fight("you get killed immediately","you get shot like a dog", True)
                                    if d == "firearm":
                                        if chance(80):
                                            item = self.firearms[randint(0, len(self.firearms) - 1)]
                                            money = randint(5, 15)
                                            print(f"you kill the homeowner and you find {item} and {money}")
                                            self.inventory.append(item)
                                            self.cash += money
                                        else:
                                            print("you miss")
                                            if chance(60):
                                                print("the homeowner misses too and you quickly run away")
                                            else:
                                                print("you get shot by the homeowner and die")
                                                self.game = False
                                    elif d == "melee":
                                        if chance(70):
                                            print("you pull out your melee weapon and charge the man")
                                            item = self.firearms[randint(0, len(self.firearms) - 1)]
                                            money = randint(5, 15)
                                            print(f"you kill the homeowner and you find {item} and {money}")
                                            self.inventory.append(item)
                                            self.cash += money
                                        else:
                                            print("the homeowner kills you before you even take a step forward")
                                            self.game = False                       
                            else:
                                print("the homeowner doesn't believe you and demand that you leave")
                                d = int(input("do you:\n1. comply\n2. fight\n"))
                                if d == 1:
                                    print("you apologize to him and leave")
                                elif d == 2:
                                    print("you challenge the homeowner to a duel")
                                    d = self.fight("you get killed immediately","you get shot like a dog", True)
                                    if d == "firearm":
                                        if chance(80):
                                            item = self.firearms[randint(0, len(self.firearms) - 1)]
                                            money = randint(5, 15)
                                            print(f"you kill the homeowner and you find {item} and {money}")
                                            self.inventory.append(item)
                                            self.cash += money
                                        else:
                                            print("you miss")
                                            if chance(60):
                                                print("the homeowner misses too and you quickly run away")
                                            else:
                                                print("you get shot by the homeowner and die")
                                                self.game = False
                                    elif d == "melee":
                                        if chance(70):
                                            print("you pull out your melee weapon and charge the man")
                                            item = self.firearms[randint(0, len(self.firearms) - 1)]
                                            money = randint(5, 15)
                                            print(f"you kill the homeowner and you find {item} and {money}")
                                            self.inventory.append(item)
                                            self.cash += money
                                        else:
                                            print("the homeowner kills you before you even take a step forward")
                                            self.game = False           
                                else:
                                    print("you suffer a heart attack and die")            
                                    self.game = False

                        elif c == 2:
                            print("you challenge the homeowner to a duel")
                            d = self.fight("you get killed immediately","you get shot like a dog", True)
                            if d == "firearm":
                                if chance(80):
                                    item = self.firearms[randint(0, len(self.firearms) - 1)]
                                    money = randint(5, 15)
                                    print(f"you kill the homeowner and you find {item} and {money}")
                                    self.inventory.append(item)
                                    self.cash += money
                                else:
                                    print("you miss")
                                    if chance(60):
                                        print("the homeowner misses too and you quickly run away")
                                    else:
                                        print("you get shot by the homeowner and die")
                                        self.game = False
                            elif d == "melee":
                                if chance(70):
                                    print("you pull out your melee weapon and charge the man")
                                    item = self.firearms[randint(0, len(self.firearms) - 1)]
                                    money = randint(5, 15)
                                    print(f"you kill the homeowner and you find {item} and {money}")
                                    self.inventory.append(item)
                                    self.cash += money
                                else:
                                    print("the homeowner kills you before you even take a step forward")
                                    self.game = False                            
                elif a == 3:
                    b = int(input("would you like to:\n1. insult\n2. compliment\n3. play rock paper scissors\n"))
                    if b == 1:
                        self.insult(True)
                        if chance(80):
                            print("the homeowner is deeply offended and shuts the door in your face")
                        else:
                            print("the homeowner is outraged by your comments and challenges you to a duel of honour")
                            c = self.fight("the homeowner shoots and kills you", "the homeowner kills you without hesitation", True)
                            if c == "firearm":
                                if chance(80):
                                    item = self.firearms[randint(0, len(self.firearms) - 1)]
                                    print(f"you kill the homeowner and you find {item}")
                                    self.inventory.append(item)
                                else:
                                    if chance(40):
                                        print("you miss, but the homeowner also misses and you quickly run away")
                                    else:
                                        print("you miss and the homeowner kills you")
                                        self.game = False
                            elif c == "melee":
                                if chance(67):
                                    print("you lunge forward with your melee weapon with your melee weapon and kill the homeowner")
                                    item = self.firearms[randint(0, len(self.firearms) - 1)]
                                    print(f"you find {item} on the body")
                                    self.inventory.append(item)
                                else:
                                    if chance(40):
                                        print("you miss, but the homeowner also misses and you quickly run away")
                                    else:
                                        print("you miss and the homeowner kills you")
                                        self.game = False
                                        
                    elif b == 2:
                        self.insult(False)
                        print("the homeowner thanks you for your kind words")
                        if chance(60):
                            print("they invite you to join them for a cup of tea")
                            c = int(input("would you like to:\n1. go in the home\n2. politely decline\n3. rudely decline\n"))
                            if c == 1:
                                print("you walk in the home")
                                if chance(30):
                                    print("it was an ambush and the homeowner pulls out a gun, intending to rob you")
                                    d = int(input("do you:\n1. surrender (get robbed)\n2. fight back\n"))
                                    if d == 1:
                                        if self.cash == 0:
                                            if self.inventory:
                                                item = self.inventory[randint(0, len(self.inventory) - 1)]
                                                print(f"the homeowner takes {item}")
                                                #self.inventory remove item
                                            else:
                                                print("since you have no money nor any items, the homeowner decides to let you go") 
                                        else:
                                            money = round(self.cash*0.2)
                                            print(f"you give the homeowner {money} dollars")
                                            self.cash -= money
                                    elif d == 2:
                                        e = self.fight("you get shot","you get shot like a dog", True)
                                        if e == "firearm":
                                            if chance(80):
                                                item = self.firearms[randint(0, len(self.firearms) - 1)]
                                                print(f"you kill the homeowner and you find {item}")
                                                self.inventory.append(item)
                                            else:
                                                if chance(40):
                                                    print("you miss, but the homeowner also misses and you quickly run away")
                                                else:
                                                    print("you miss and the homeowner kills you")
                                                    self.game = False
                                        elif e == "melee":
                                            if chance(70):
                                                print("you lunge forward with your melee weapon with your melee weapon and kill the homeowner")
                                                item = self.firearms[randint(0, len(self.firearms) - 1)]
                                                print(f"you find {item} on the body")
                                                self.inventory.append(item)
                                            else:
                                                if chance(40):
                                                    print("you miss, but the homeowner also misses and you quickly run away")
                                                else:
                                                    print("you miss and the homeowner kills you")
                                                    self.game = False
                                        else:
                                            print()
                                        
                                else:
                                    print("you have a lovely conversation with the homeowner")
                                    if chance(80):
                                        item = self.items[randint(0, len(self.items) - 1)]
                                        print(f"the homeowner appreciates your company and gives you {item}")
                                        self.inventory.append(item)
                                    else:
                                        print("you leave the home happily")
                            elif c == 2:
                                print("you politely decline and walk away")
                            else:
                                self.insult(True)
                                print("you quickly run away")
                    elif b == 3:
                        if self.inventory:
                            self.inventoryAccess()
                            c = int(input("what would you like to bet:"))
                            betting = self.inventory[c - 1]
                            betting_opp = self.items[randint(0, len(self.items) - 1)]
                            d = rockPaperScissors()
                            if d == True:
                                print(f"the homeowner reluctantly gives you {betting_opp}")
                                self.inventory.append(betting_opp)
                            else:
                                print(f"you reluctantly give the homeowner {betting}")
                                del self.inventory[c - 1]
            else:
                scenario = "as you walk up to the house a man tries to rob you. he pulls out his gun"
                print(scenario)

                a = int(input("would you like to:\n1. get robbed\n2. fight back\n"))

                if a == 1:
                    if self.inventory:
                        b = int(input("would you like to give him\n1. money\n2. an item\n"))

                        if b == 1:
                            if self.cash > 0:
                                if self.cash >= 50:
                                    robbed = randint(20, 50)
                                    self.cash -= robbed
                                    print(f"he takes ${robbed}")
                                else:
                                    robbed = self.cash
                                    self.cash = 0
                                    print(f"he takes all your money because you only have ${robbed}")
                            else:
                                print("the man shoots you as soon as he sees your wallet is empty")
                                self.game = False
                        elif b == 2:
                            if self.inventory:
                                self.inventoryAccess()
                                robbed = self.inventory[randint(0, len(self.inventory) - 1)]
                                print(f"he looked through all your belongings and stole {robbed}")
                            else:
                                print("he shot you because you had nothing to give him")
                                self.game = False
                elif a == 2:
                    b = self.fight("he shoots you and collects all your items", "he laughs and shoots you", True)

                    if b == "firearm":
                        if chance(80):
                            if chance(50):
                                c = self.items[randint(0, len(self.items) - 1)]
                            else:
                                if chance(50):
                                    c = self.firearms[randint(0, len(self.firearms) - 1)]      
                                else:
                                    c = self.melee[randint(0, len(self.melee) - 1)]      

                            d = self.items[randint(0, len(self.items) - 1)]
                            print(f"you shoot the man and collect all the items he has robbed, including {c} and {d} ")
                            self.inventory.append(c)
                            self.inventory.append(d)

                        else:
                            print("the man shoots you and runs away before the cops show up")
                            self.game = False

                    elif b == "melee":
                        if chance(70):
                            print("you run towards the man with your melee weapon\nhe tries to dodge, but you're too quick")
                            item = self.firearms[randint(0, len(self.firearms)-1)]
                            if chance(50):
                                money = randint(10, 40)
                                print(f"you kill the man and find {item} and {money} dollars on him")
                                self.inventory.append(item)
                                self.cash += money
                            else:
                                print(f"you scare the man and he drops his gun\nhe drops his gun and you pick up {item}")
                                self.inventory.append(item)
                        else:
                            print("as you pull out your melee weapon, the man shoots and kills you")
                            self.game = False


    def obstacles(self, locations, x, y):
        #everytime a move is made find out which location the player moved to
        if self.map[self.y + y][self.x + x] in locations:
            #call encounters function and pass location index
            self.encounters(locations.index(self.map[self.y + y][self.x + x]))
        elif self.map[self.y + y][self.x + x] == "😈":
            self.boss()

    def move(self, direction, s, locations):
        if direction == "up":
            if self.y >= 1:
                self.obstacles(locations, 0, -1)
                self.map[self.y][self.x] = "⬛️"
                self.y -= 1
                self.map[self.y][self.x] = self.image
            else:
                print("\ncan not go up")

        if direction == "down":
            if self.y <= s - 2:
                self.obstacles(locations, 0, 1)
                self.map[self.y][self.x] = "⬛️"
                self.y += 1
                self.map[self.y][self.x] = self.image
            else:
                print("\ncan not go down")

        if direction == "left":
            if self.x >= 1:
                self.obstacles(locations, -1, 0)
                self.map[self.y][self.x] = "⬛️"
                self.x -= 1
                self.map[self.y][self.x] = self.image

            else:
                print("\ncan not go left")

        if direction == "right":
            if self.x <= s - 2:
                self.obstacles(locations, 1, 0)
                self.map[self.y][self.x] = "⬛️"
                self.x += 1
                self.map[self.y][self.x] = self.image

            else:
                print("\ncan not go right")

        if direction == "inventory":
            self.inventoryAccess()
        
        if direction == "cash":
            self.cashBalance()

        if direction == "instructions":
            self.instructions()