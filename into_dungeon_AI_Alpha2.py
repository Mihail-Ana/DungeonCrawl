import random
global turn
global card
turn = 1
#Defining the PLAYER class with attribute NAME
class player:
    def __init__(self, name):
        self.name = name
        self.pocket = {}
        self.pass_token = 0

    def PileRemove(self):
        action = input("Place monster on Pile (pile), or Remove Equipment (remove)? \n")
        return action

    def ItemRemove(self):
        action = input("What item do you want to remove? \n")
        return action

    def DrawPass(self, playerB):
        action = input("Type Draw or Pass: \n")
        if action in ["draw", "Draw", "play"]:
            self.Draw(dungeon, champion)
        elif action == "pass":
            self.Pass(playerB, champion)
        elif action in ["q", "quit", "Quit"]:
            quit()
        else:
            print("action unknown try again:")
            self.DrawPass(playerB)

    def Draw(self, dungeon, champion, card = None):
        if card == None:
            card = random.choice(list(dungeon))
            print(card, dungeon[card])
        else:
            print(card, dungeon[card])

        if champion.items == {}:
            print(champion.name, "is naked!! Monster added to Pile!")
            action = 'pile'
        else:
            action = self.PileRemove()

        if action == "pile":
            pile[card] = dungeon[card]
            dungeon.pop(card)
        elif action == "remove":
            self.pocket[card] = dungeon[card]
            dungeon.pop(card)
            champion.remove_item(self)
        elif action in ['q', "quit", "Quit", "close"]:
            quit()
        else:
            print("Invalid action, try again: \n")
            self.Draw(dungeon, champion, card)

    def Pass(self, playerB, champion):
        #This is for 3 or more players only. Pass_Token
        '''
        if playerB.pass_token == 0:
            playerA.pass_token = 1
        else:
            '''
        print(playerB.name, "is going in the dungeon. Good luck!")
        tally(playerB, champion)

    def vorpal(self, champion):
        choice = input('Which monster type do you want to kill using the vorpal sowrd? \n')
        if choice not in template:
            print("That is not a real Monster, try again:")
            return self.vorpal(champion)
        else:
            return choice
#AI class definition
class AI:
    def __init__(self, name):
        self.name = name
        #print("Hi, I am " + name + ", I will be your opposing AI. Have fun!")
        self.pocket = {}
        self.pass_token = 0

    def PileRemove(self):
        print("Place monster on Pile (pile), or Remove Equipment (remove)? \n")
        if len(pile) > 3:
            action = "remove"
        else:
            action = "pile"
        return action

    def ItemRemove(self):
        print("What item do you want to remove? \n")
        action = random.choice(list(champion.items.keys()))
        return action

    def DrawPass(self, playerB):
        print("Type Draw or Pass: \n")
        if len(pile) > 5:
            action = "pass"
        else:
            action = "draw"
        if action in ["draw", "Draw", "play"]:
            self.Draw(dungeon, champion)
        else:
            self.Pass(playerB, champion)


    def Draw(self, dungeon, champion, card = None):
        if card == None:
            card = random.choice(list(dungeon))
        else:
            pass

        if champion.items == {}:
            print(champion.name, "is naked!! Monster added to Pile!")
            action = 'pile'
        else:
            action = self.PileRemove()

        if action == "pile":
            pile[card] = dungeon[card]
            dungeon.pop(card)
        else:
            self.pocket[card] = dungeon[card]
            dungeon.pop(card)
            champion.remove_item(self)


    def Pass(self, playerB, champion):
        #This is for 3 or more players only. Pass_Token
        '''
        if playerB.pass_token == 0:
            playerA.pass_token = 1
        else:
            '''
        print(playerB.name, "is going in the dungeon. Good luck!")
        tally(playerB, champion)

    def vorpal(self, champion):
        print('Which monster type do you want to kill using the vorpal sowrd? \n')
        action = random.choice(list(template.keys()))
        return action
#Defining the HERO class with attributes HP and ITEMS
class hero:
    def __init__(self, name, hp, items):
        self.name = name
        self.hp = hp
        self.items = items

    def final_hp(self):
        f_hp = self.hp
        for value in self.items.values():
            f_hp += value
        return f_hp

    def remove_item(self, player):
        for x in self.items:
            print(x)
        item = player.ItemRemove()
        if item in self.items:
            self.items.pop(item)
            print("The", item, "was removed from the Champion's inventory!\nThis is what is left:")
            for x in self.items:
                print(x)
        else:
            print("The", self.name, "does not have that item \n")
            self.remove_item(player)

    def vorpal_sword(self, choice):
        if choice[-1] == "2":
            choice = choice[:-1]
        choice2 = choice + "2"
        if "vorpal sword" in champion.items:
            found = False
            if choice in pile:
                pile.pop(choice)
                found = True
                print(choice, "removed from pile! \n" )
            if choice2 in pile:
                pile.pop(choice2)
                found = True
                print(choice, "removed from pile! \n")
            if found == False:
                print(choice, "was not in the pile... \n")

'''
------------------------------------------------------------------------
'''

def hero_select():
    return warrior

#See what items the HERO has left:
def item_check(champion, pile, player):
    if champion == warrior:
        if "vorpal sword" in champion.items:
            choice = player.vorpal(champion)
            champion.vorpal_sword(choice)
            print("pile has: ", pile, "\n")

        if "dragon spear" in champion.items:
            if "dragon" in pile:
                pile.pop("dragon")
                print("Dragon was killed with Dragon Spear! \n")

        if "holy grail" in champion.items:
            for x in pile.copy():
                if pile[x] % 2 == 0:
                    pile.pop(x)
                    print(x, "was killed with Holy Grail! \n")

        if "torch" in champion.items:
            for x in pile.copy():
                if pile[x] <= 3:
                    pile.pop(x)
                    print(x, "was killed with Torch! \n")

        return pile
    else:
        print("Hero not added yet...")
        quit()



#Check to see if the HERO can defeat the Pile Monsters:
def tally(player, champion):
    attack = 0
    item_check(champion, pile, player)
    health = champion.final_hp()
    for x in pile.values():
        attack += x
    print("attack value is: ", attack, "\n")
    print("health value is: ", health, "\n")
    if health > attack:
        print(player.name, "wins the game!!!")
    else:
        print(player.name, "has died!")
    quit()


"""
----------------------------------------------------------------
"""


def game(playerA, playerB, dungeon, champion):
    global turn
    while True:
        print("It is turn ", turn, "and there are ", len(dungeon), "monsters remaining.")
        if dungeon == {}:
            if turn % 2 != 0:
                print(playerA.name, "Is going in the dungeon with the ", champion.name)
                tally(playerA, champion)
            else:
                print(playerB.name, "Is going in the dungeon with the ", champion.name)
                tally(playerB, champion)
        if turn % 2 != 0:
            print(playerA.name, "'s turn:", '\n')
            print("What would you like to do: ", '\n')
            playerA.DrawPass(playerB)
        else:
            print(playerB.name, "'s turn:", '\n')
            print("What would you like to do: ", '\n')
            playerB.DrawPass(playerA)
        turn += 1


#Initializing the GAME start stage
player1 = player("Alexandra")
player2 = AI("Xella")


dungeon = {"goblin": 1, "goblin2": 1, "skeleton2": 2,
 "skeleton": 2, "grunt": 3, "grunt2": 3, "vampire": 4,
  "vampire2": 4, "golem": 5,  "golem2": 5, "reaper": 6,
   "deamon": 7, "dragon": 9}
pile = {}
template = dungeon.copy()
#print("These are the enemies inside the dungeon: \n", dungeon)
warrior = hero("Warrior", 3, {
"knight shield": 3,
"plate armor": 5,
"dragon spear": 0,
"holy grail": 0,
"vorpal sword": 0,
"torch": 0
})
champion = hero_select()

#MAIN GAME

game(player1, player2, dungeon, champion)
