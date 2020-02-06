import tkinter as tk
import random
from tkinter import font
from tkinter import *
from tkinter import ttk
from tkinter import messagebox

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
        items_description.pop(weapon)


class AI:
    def __init__(self, name, strat):
        self.name = name
        self.strat = strat

    def strat_lvl():

    #AI Stay Clear
    #BASE AI FUCNITONS WORK CORRECTLY
    #MUST IMPLEMENT MULTIPLE STRATEGIES

def Check():
    global turn
    if turn % 2 == 0:
        AI()
    else:
        pass

def AI():
    global turn
    global MonsterLabel
    global DrawnMonster
    global AIcard
    global AIPocket

    n1 = random.choice([5, 6, 7, 8, 9])
    n2 = random.choice([4, 5, 6])
    n3 = random.choice([4, 5, 6])

    if len(pile) > n1:
        End_TurnStage1(items_dmg)
    else:
        AIcard = random.choice(list(dungeon))
        if len(pile) < n2:
            if len(items_dmg) > n3:
                AIpile()
            else:
                AIPocket.append(AIcard)
                AIremove()
        else:
            End_TurnStage1(items_dmg)

def AIpile():
    global turn
    global Psize
    global pile
    pile[AIcard] = dungeon[AIcard]
    dungeon.pop(AIcard)
    turn += 1
    TurnCount.set(turn)
    Psize.set(len(pile))

def AIremove():
    global turn
    to_remove = random.choice(list(warrior.items.keys()))
    warrior.remove_item(to_remove)
    HW.forget()
    gen_HeroWindow(items_description)
    turn += 1
    TurnCount.set(turn)

def ItemCheck_AI(pile, items, E):
    global combo2
    if "vorpal sword" in warrior.items:
        if len(AIPocket) > 0:
            AIVS = []
            for item in list(DIndex):
                if item not in AIPocket:
                    AIVS.append(item)
            target = random.choice(AIVS)
        else:
            target = random.choice(list(DIndex))
        menubar.add_command(label="AI Kill", command = lambda: Hack2(target))
        Evict(target)
    else:
        AllOtherItems()

    #MainActions Frame Design Functions
def gen_Turn():
    global TurnCount
    global T
    global turn
    global window
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
    Pkt = tk.Button(TA, text = "Check Pocket", wraplength = 80, command = ChkPkt)
    Pkt.place(bordermode = "inside",  rely = 0.65, relx = 0.1, width = 80)

    #TurnActions Frame Design Functions
def gen_MainActions():
    global MA
    global card
    global DrawnMonster
    global MonsterLabel
    global pile
    global Psize
    card = random.choice(list(dungeon))
    card_for_pocket = card + " " + str(dungeon.get(card))
    DrawnMonster = StringVar()
    MonsterLabel = tk.Label(TA, textvariable = DrawnMonster, wraplength = 80)
    MonsterLabel.place(bordermode = "inside", rely = 0.2, relx = 0.6)
    DrawnMonster.set(card)
    Psize = StringVar()
    PileSize = tk.Label(TA, text = "Nr of Monsters in pile", wraplength = 80)
    PileSize.place(bordermode = "inside", rely = 0.4, relx = 0.6)
    PileNr = tk.Label(TA, textvariable = Psize)
    PileNr.place(bordermode = "inside", rely = 0.7, relx = 0.725)
    Psize.set(len(pile))
    MA = tk.Frame(window, bg = "Blue", highlightthickness = 5)
    MA.place(bordermode = "inside", relheight = 0.4, relwidth = 0.3, rely = 0.4)
    add = tk.Button(MA, text = "Submit Monster", wraplength = 80, command = End_TurnStage2)
    add.place(bordermode = "inside", rely = 0.05, relx = 0.1, width = 80)
    remove = tk.Button(MA, text = "Pocket and Remove Hero Item", wraplength = 80, command = lambda : gen_Items(items_dmg, card_for_pocket))
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
    global init_items
    global init_items_descriptions
    init_items = [] #creates an empty list for your labels
    init_items_descriptions = []
    count = 0.2
    count1 = 0.2
    for k in items.keys(): #iterates over your nums
        item_name = k
        label = tk.Label(HW, text = item_name) #set your text
        label.place(rely = count, relx = 0.1)
        init_items.append(label) #appends the label to the list for further use
        count += 0.125
    for j in items.values():
        item_name = j
        label1 = tk.Label(HW, text = item_name) #set your text
        label1.place(rely = count1, relx = 0.3)
        init_items_descriptions.append(label1) #appends the label to the list for further use
        count1 += 0.125

def gen_Items(items, card):
    global I
    global combo
    global PlayerPocket
    PlayerPocket.append(card)
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
    hax = pile.copy()
    menubar.add_command(label="Hax", command = lambda: Hack(hax))
    turn += 1
    TurnCount.set(turn)
    ENTER(items)

def End_TurnStage2():                                                                           #Occurs when a player Submits a monster in Dungeon(Pile)
    global turn
    global MonsterLabel
    global DrawnMonster
    global Psize
    global pile
    MonsterLabel.place(bordermode = "inside", rely = 0.2, relx = 0.6)
    MA.destroy()
    pile[card] = dungeon[card]
    dungeon.pop(card)
    turn += 1
    TurnCount.set(turn)
    DrawnMonster.set(card)
    MonsterLabel.place_forget()
    Psize.set(len(pile))
    AI_Check()

def End_TurnStage3(items):                                                                           #Occurs when a player Removes an item from the Hero
    global turn
    global MonsterLabel
    global HW
    ComboVar = combo.get()
    warrior.remove_item(ComboVar)
    I.destroy()
    MA.destroy()
    MonsterLabel.place_forget()
    HW.forget()
    gen_HeroWindow(items_description)
    turn += 1
    TurnCount.set(turn)
    AI_Check()

def gen_Dungeon(template):
    D = tk.Frame(window, bg = "Brown", highlightthickness = 5)
    D.place(bordermode = "inside", relheight = 0.8, relwidth = 0.2, relx = 0.8)
    l1 = tk.Label(D, text = "The dungeon contains: ", wraplength = 80)
    l1.grid(column = 0, row = 0, padx = 5)
    l2 = tk.Label(D, text = "Monsters ATK:", wraplength = 50)
    l2.grid(column = 1, row = 0, padx = 5)
    labels = [] #creates an empty list for your labels
    labels_val = []
    count = 1
    for k in template.keys(): #iterates over your nums
        label = tk.Label(D, text = k) #set your text
        label.grid(column = 0, row = count, pady = 6, ipadx = 5)
        labelv = tk.Label(D, text = str(template[k]))
        labelv.grid(column = 1, row = count, pady = 6, ipadx = 20)
        labels.append(label) #appends the label to the list for further use
        labels_val.append(labelv)
        count += 1

def ENTER(items):
    global E
    global warrior
    global turn
    E = tk.Frame(window, bg = "Pink", highlightthickness = 5)
    E.place(bordermode = "inside", relheight = 0.4, relwidth = 0.8, rely = 0.4)
    if turn % 2 == 0:                                                                   #Panic Player Turn Check
        ItemCheck_AI(pile, items, E)
    else:
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
        b1 = tk.Button(E, text = "OK", command = lambda: Evict(combo2.get()))
        b1.place(bordermode = "inside", rely = 0.8, relx = 0.1)
    else:
        AllOtherItems()

def Evict(player_kill):
    global pile
    player_kill2 = player_kill + "2"
    if player_kill in pile:
        pile.pop(player_kill)
    if player_kill2 in pile:
        pile.pop(player_kill2)
    AllOtherItems()

def AllOtherItems():
    if "dragon spear" in warrior.items:
        if "dragon" in pile:
            pile.pop("dragon")

    if "holy grail" in warrior.items:
        for x in pile.copy():
            if pile[x] % 2 == 0:
                pile.pop(x)

    if "torch" in warrior.items:
        for x in pile.copy():
            if pile[x] <= 3:
                pile.pop(x)
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
        messagebox.showinfo("You Win!", player + " wins!")
        #window.destroy()
    else:
        messagebox.showinfo("You Died!", player + " has died!")
        #window.destroy()

def ChkPkt():
    global PlayerPocket
    messagebox.showinfo("In Pocket", PlayerPocket)

        #Menu Functions

def information():
    messagebox.showinfo("Information about the Items and Monsters", "Bla bla bla")

def Hack(hax):
    messagebox.showinfo("Hacking, I see", hax)

def Hack2(items):
    messagebox.showinfo("Cool, items:", items)

def Hack3():
    global pile
    messagebox.showinfo("Current Pile: ", pile)

def Hack4(AIPocket):
    messagebox.showinfo("AI Pocket", AIPocket)

def retry():
    import os
    os.execv(sys.executable, [sys.executable, 'ITD_GUI_VS_AI_ALPHA_V1.py'] + sys.argv)

def New_Game():
    global pile
    global DIndex
    global combo2
    global champion
    global hax
    global menubar
    global window
    global dungeon
    global items_dmg
    global items_description
    global warrior
    global PlayerPocket
    global AIPocket
    Main_Menu.destroy()
    window = tk.Tk()

    default_font = font.nametofont("TkFixedFont")
    default_font.configure(family = "Verdana", size = 10)
    window.option_add("*Label.Font", default_font)
    window.option_add("*Font", default_font)

    window.title("Into the Dungeon")
    window.geometry("1200x786")
    quit = tk.Button(text = "Quit", bg = "red", command = window.destroy)
    quit.place(bordermode = "inside", relheight = 0.08, relwidth = 0.08, rely = 0.85, relx = 0.05)
    info = tk.Button(text = "INFO", bg = "blue", command = information)
    info.place(bordermode = "inside", relheight = 0.08, relwidth = 0.08, rely = 0.85, relx = 0.15)

    restart = tk.Button(text = "Restart?", bg = "Green", command = retry)
    restart.place(bordermode = "inside", relheight = 0.08, relwidth = 0.08, rely = 0.85, relx = 0.25)

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
    PlayerPocket = []
    AIPocket = []
    #GUI Structure setup
    menubar = tk.Menu(window)
    menubar.add_command(label="Current Pile", command= Hack3)
    menubar.add_command(label="Current Items", command = lambda: Hack2(items_dmg))
    menubar.add_command(label="AI Pocket", command = lambda: Hack4(AIPocket))

    gen_Turn()
    gen_TurnActions()
    gen_HeroWindow(items_description)
    gen_Dungeon(template)
    # display the menu
    window.config(menu=menubar)
    #Initializing the GAME start stage
    window.mainloop()



    #Main Window Setup
if __name__ == "__main__":
    global pile
    global DIndex
    global combo2
    global champion
    global hax
    global menubar

    Main_Menu = tk.Tk()

    ALG36 = font.Font(family='Algerian', size=36, weight= 'bold')
    Main_Menu.title("Into the Dungeon - Main Menu")
    Main_Menu.geometry("800x600")
    New_Game = tk.Button(text = "New Game", font = ALG36, bg = "Green", command = New_Game)
    New_Game.place(bordermode = "inside", relheight = 0.4, relwidth = 0.8, rely = 0.05, relx = 0.1)
    quit = tk.Button(text = "Quit", font = ALG36, bg = "red", command = Main_Menu.destroy)
    quit.place(bordermode = "inside", relheight = 0.4, relwidth = 0.8, rely = 0.5, relx = 0.1)
    Main_Menu.mainloop()
