import tkinter as tk
import random
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

#Game don't feature multiple heroes, or Multiplayer, or AI. Next Build hopefully AI
#Game only has full turn-based play, but both players see the cards

global warrior

    #Classes:
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

    def remove_item(self, weapon):
        self.items.pop(weapon)
        pass

    #MainActions Frame Design Functions
def gen_Turn():
    global TurnCount
    global T
    global turn
    turn = 1
    TurnCount = StringVar()
    T = tk.Frame(window, bg = "Red", highlightthickness = 5)
    T.place(bordermode = "inside", relheight = 0.2, relwidth = 0.3, rely = 0.8, relx = 0.4)
    L1 = tk.Label(T, textvariable = TurnCount)
    L1.place(bordermode = "inside", rely = 0.4, relx = 0.5, relheight = 0.2, relwidth = 0.2 )
    L2 = tk.Label(T, text = "Turn: ")
    L2.place(bordermode = "inside", rely = 0.4, relx = 0.25, relheight = 0.2, relwidth = 0.2 )
    TurnCount.set(turn)

def gen_TurnActions():
    global TA
    TA = tk.Frame(window, bg = "Purple", highlightthickness = 5)
    TA.place(bordermode = "inside", relheight = 0.4, relwidth = 0.3)
    draw = tk.Button(TA, text = "Draw Monster", wraplength = 80, command = gen_MainActions)
    draw.place(bordermode = "inside", rely = 0.05, relx = 0.1, width = 80)
    pss = tk.Button(TA, text = "Pass Turn", wraplength = 80, command = lambda: End_TurnStage1(items_dmg))
    pss.place(bordermode = "inside",  rely = 0.35, relx = 0.1, width = 80)

    #TurnActions Frame Design Functions
def gen_MainActions():
    global MA
    global card
    global DrawnMonster
    global MonsterLabel
    card = random.choice(list(dungeon))
    DrawnMonster = StringVar()
    MonsterLabel = tk.Label(TA, textvariable = DrawnMonster, wraplength = 80)
    MonsterLabel.place(bordermode = "inside", rely = 0.2, relx = 0.6)
    DrawnMonster.set(card)
    MA = tk.Frame(window, bg = "Blue", highlightthickness = 5)
    MA.place(bordermode = "inside", relheight = 0.4, relwidth = 0.3, rely = 0.4)
    pile = tk.Button(MA, text = "Submit Monster", wraplength = 80, command = End_TurnStage2)
    remove = tk.Button(MA, text = "Discard and Remove Hero Item", wraplength = 80, command = lambda : gen_Items(items_dmg))
    pile.place(bordermode = "inside", rely = 0.05, relx = 0.1, width = 80)
    remove.place(bordermode = "inside",  rely = 0.35, relx = 0.1, width = 80)

    #HeroTraits Frame Design Functions
def gen_HeroWindow(items):
    global HW
    HW = tk.Frame(window, bg = "Green", highlightthickness = 5)
    HW.place(bordermode = "inside", relheight = 0.4, relwidth = 0.5, relx = 0.3)
    l1 = tk.Label(HW, text = "The champion: Warrior (+3 HP)")
    l1.place(bordermode = "inside", rely = 0.05, relx = 0.1)
    hero_items(HW, items)

def hero_items(HW, items):
    labels = [] #creates an empty list for your labels
    labels1 = []
    count = 0.2
    count1 = 0.2
    for k in items.keys(): #iterates over your nums
        item_name = k
        label = tk.Label(HW, text = item_name) #set your text
        label.place(rely = count, relx = 0.1)
        labels.append(label) #appends the label to the list for further use
        count += 0.125
    for j in items.values():
        item_name = j
        label1 = tk.Label(HW, text = item_name) #set your text
        label1.place(rely = count1, relx = 0.3)
        labels1.append(label1) #appends the label to the list for further use
        count1 += 0.125

def gen_Items(items):
    global I
    global combo
    I = tk.Frame(window, bg = "Teal", highlightthickness = 5)
    I.place(bordermode = "inside", relheight = 0.4, rely = 0.4, relx = 0.3, relwidth = 0.5)
    HeroItems = []
    combo = ttk.Combobox(I)
    for item in items.keys():
        HeroItems.append(item)
        combo.place(bordermode = "inside", rely = 0.65, relx = 0.1)
    combo["values"] = HeroItems
    combo.current(0)
    l2 = tk.Label(I, text = "Select the item you wish to remove:")
    l2.place(bordermode = "inside", rely = 0.1, relx = 0.1)
    b1 = tk.Button(I, text = "OK", command = lambda: End_TurnStage3(items))
    b1.place(bordermode = "inside", rely = 0.8, relx = 0.1)

def End_TurnStage1(items):                                                                           #Occurs when A player Passes
    global turn
    global hax
    turn += 1
    TurnCount.set(turn)
    hax = pile.copy()
    menubar.add_command(label="Hax", command= lambda: Hack(hax))
    ENTER(items)

def End_TurnStage2():                                                                           #Occurs when a player Submits a monster in Dungeon(Pile)
    global turn
    global MonsterLabel
    global DrawnMonster
    MonsterLabel.place(bordermode = "inside", rely = 0.2, relx = 0.6)
    MA.destroy()
    pile[card] = dungeon[card]
    dungeon.pop(card)
    turn += 1
    TurnCount.set(turn)
    DrawnMonster.set(card)
    MonsterLabel.place_forget()

def End_TurnStage3(items):                                                                           #Occurs when a player Removes an item from the Hero
    global turn
    global MonsterLabel
    ComboVar = combo.get()
    warrior.remove_item(ComboVar)
    I.destroy()
    MA.destroy()
    MonsterLabel.place_forget()
    turn += 1
    TurnCount.set(turn)

def gen_Dungeon(template):
    D = tk.Frame(window, bg = "Brown", highlightthickness = 5)
    D.place(bordermode = "inside", relheight = 0.8, relwidth = 0.2, relx = 0.8)
    l1 = tk.Label(D, text = "The dungeon contains: ")
    l1.grid(column = 0, row = 0)
    labels=[] #creates an empty list for your labels
    count = 1
    for k in template.keys(): #iterates over your nums
        monster_hp = k + ":" + str(template[k])
        label = tk.Label(D,text = monster_hp) #set your text
        label.grid(column = 0, row = count, pady = 2, padx = 10)
        labels.append(label) #appends the label to the list for further use
        count += 1

def ENTER(items):
    global E
    global warrior
    E = tk.Frame(window, bg = "Pink", highlightthickness = 5)
    E.place(bordermode = "inside", relheight = 0.4, relwidth = 0.8, rely = 0.4)
    ItemCheck(pile, items, E)

def ItemCheck(pile, items, E):
    global combo2
    if "vorpal sword" in warrior.items:
        l1 = tk.Label(E, text = "Select the Monster you wish to Slay:")
        l1.place(bordermode = "inside", rely = 0.1, relx = 0.1)
        global combo2
        combo2 = ttk.Combobox(E)
        Mons = []
        for item in DIndex.keys():
            Mons.append(item)
        combo2.place(bordermode = "inside", rely = 0.65, relx = 0.1)
        combo2["values"] = Mons
        combo2.current(0)
        b1 = tk.Button(E, text = "OK", command = Evict)
        b1.place(bordermode = "inside", rely = 0.8, relx = 0.1)
    else:
        AllOtherItems()

def Evict():
    global pile
    global combo2
    player_kill = combo2.get()
    player_kill2 = player_kill + "2"
    if player_kill in pile:
        pile.pop(player_kill)
        print("VS")
    if player_kill2 in pile:
        pile.pop(player_kill2)
        print("VS")
    AllOtherItems()

def AllOtherItems():
    if "dragon spear" in warrior.items:
        if "dragon" in pile:
            pile.pop("dragon")
            print("DS")

    if "holy grail" in warrior.items:
        for x in pile.copy():
            if pile[x] % 2 == 0:
                pile.pop(x)
                print("HG")

    if "torch" in warrior.items:
        for x in pile.copy():
            if pile[x] <= 3:
                pile.pop(x)
                print("T")
    TallyTime()

def TallyTime():
    atk = 0
    Atk = StringVar()
    health = warrior.final_hp()
    HP = StringVar()
    for x in pile.values():
        atk += x
    Latk_text = tk.Label(E, text = "The Attack of all Enemies is:")
    Latk_text.place(bordermode = "inside",  rely = 0.35, relx = 0.1)
    Latk = tk.Label(E, textvariable = Atk)
    Latk.place(bordermode = "inside",  rely = 0.5, relx = 0.1)
    Atk.set(atk)
    Lhp_text = tk.Label(E, text = "The Health of your Hero is:")
    Lhp_text.place(bordermode = "inside",  rely = 0.35, relx = 0.5)
    Lhp = tk.Label(E, textvariable = HP)
    Lhp.place(bordermode = "inside",  rely = 0.5, relx = 0.5)
    HP.set(health)
    if turn % 2 == 0:
        player = "Player2"
    else:
        player = "Player1"

    if health > atk:
        messagebox.showinfo("You Win!", player + "wins!")
    else:
        messagebox.showinfo("You Died!", player + "has died!")


def information():
    messagebox.showinfo("Information about the Items and Monsters", "Bla bla bla")

def Hack(hax):
    messagebox.showinfo("Hacking, I see", hax)

def Hack2(items):
    messagebox.showinfo("Cool, items:", items)

def Hack3():
    global pile
    messagebox.showinfo("Current Pile: ", pile)

    #Main Window Setup
if __name__ == "__main__":
    global pile
    global DIndex
    global combo2
    global champion
    global hax
    global menubar
    window = tk.Tk()
    window.title("Into the Dungeon")
    window.geometry("800x600")
    quit = tk.Button(text = "Quit", bg = "red", fg = "blue", command = window.destroy)
    quit.place(bordermode = "inside", relheight = 0.08, relwidth = 0.08, rely = 0.8, relx = 0.075)
    info = tk.Button(text = "INFO", bg = "blue", fg = "Red", command = information)
    info.place(bordermode = "inside", relheight = 0.08, relwidth = 0.08, rely = 0.8, relx = 0.175)


    #Starter Info
    dungeon = { "goblin": 1, "goblin2": 1, "skeleton2": 2,
                "skeleton": 2, "grunt": 3, "grunt2": 3, "vampire": 4,
                "vampire2": 4, "golem": 5,  "golem2": 5, "reaper": 6,
                "deamon": 7, "dragon": 9}
    DIndex = { "goblin": 1, "skeleton": 2, "grunt": 3, "vampire": 4,
                "golem": 5, "reaper": 6,
                "deamon": 7, "dragon": 9}

    items_dmg = {   "knight shield": 3, "plate armor": 5,
                    "dragon spear": 0, "holy grail": 0,
                    "vorpal sword": 0, "torch": 0}
    items_description = {   "knight shield": "+ 3 HP", "plate armor": "+ 5 HP",
                    "dragon spear": "Slays the Dragon", "holy grail": "Slay Even Monsters",
                    "vorpal sword": "Choose Monster Type before entering. Slay it", "torch": "Slay Monsters with 3 Hp or Less"}
    pile = {}

    template = dungeon.copy()

    warrior = hero("Warrior", 3, items_dmg)

    #GUI Structure setup
    menubar = tk.Menu(window)
    menubar.add_command(label="Current Pile", command= Hack3)
    menubar.add_command(label="Current Items", command = lambda: Hack2(items_dmg))
    menubar.add_command(label="Info", command=information)

    gen_Turn()
    gen_TurnActions()
    gen_HeroWindow(items_description)
    gen_Dungeon(template)
    # display the menu
    window.config(menu=menubar)
    #Initializing the GAME start stage

    window.mainloop()
