import random as random
import time as time
#Classes
class Dinosaur:
    def __init__(self, name, health, attack, defense, speed, type, move1, move2, move3, move4):
        self.name = name
        self.health = health+100
        self.attack = attack
        self.defense = defense
        self.speed = speed
        self.type = type
        self.move1 = move1
        self.move2 = move2
        self.move3 = move3
        self.move4 = move4
class Attack:
    def __init__(self, name, power, accuracy, type):
        self.name = name
        self.power = power
        self.accuracy = accuracy
        self.type = type
#Attacks
frost_bolt= Attack("Frost Bolt", 90, 100, "Frost")
grassy_horn= Attack("Grassy Horn", 110, 90, "Plant")
rock_slam = Attack("Rock Slam", 105, 95, "Stone")
shadow_bite = Attack("Shadow Bite", 90, 100, "Dark")
fire_claw = Attack("Fire Claw", 100, 95, "Fire")
water_beam = Attack("Water Beam", 90, 100, "Water")
sand_tornado = Attack("Sand Tornado", 130, 70, "Sand")
bite = Attack("Bite", 70, 100, "Plain")
sun_blast = Attack("Sun Blast", 130, 70, "Fire")
bubble_storm = Attack("Bubble Storm", 130, 70, "Water")
forest_fury = Attack("Forest Fury", 130,70,"Plant")
leafy_healing = Attack("Leafy Healing", 0, 100, "Plant")
dust_storm = Attack("Dust Storm", 90, 100, "Sand")
rest = Attack("Rest", 0, 100, "Plain")
ice_lance = Attack("Ice Lance", 130, 70, "Frost")
tail_smack = Attack("Tail Smack", 120, 80, "Plain")
continental_tremor= Attack("Continental Tremor",160,60,"Stone")
tree_slap = Attack("Tree Slap", 90, 100, "Plant")
malicious_ambush= Attack("Malicious Ambush", 130, 70, "Dark")
#Dinosaurs
cryolophosaurus= Dinosaur("Cryolophosaurus", 105, 100, 75, 90, "Frost", frost_bolt,bite,rest,ice_lance)
triceratops= Dinosaur("Triceratops", 140, 120, 100, 40, "Plant", grassy_horn,forest_fury,leafy_healing,tail_smack)
huaxiazhoulong = Dinosaur("Huaxiazhoulong", 125, 70, 120, 50, "Stone", rock_slam,dust_storm,rest,tail_smack)
koleken = Dinosaur("Koleken", 90, 120, 70, 100, "Plain",bite,rest,tail_smack,shadow_bite)
alamosaurus = Dinosaur("Alamosaurus", 160, 90, 90, 20, "Stone", rock_slam,rest,tail_smack,continental_tremor)
yuanmouraptor = Dinosaur("Yuanmouraptor", 90, 110, 80, 120, "Dark", shadow_bite,bite,rest,malicious_ambush)
erlikosaurus = Dinosaur("Erlikosaurus", 100, 140, 60, 70, "Fire", fire_claw,sun_blast,rest,tail_smack)
cetiosaurus = Dinosaur("Cetiosaurus", 150, 80, 100, 30, "Water", water_beam,bubble_storm,rest,tail_smack)
concavenator = Dinosaur("Concavenator", 110, 90, 70, 100, "Sand", sand_tornado,bite,dust_storm,rest)
austrosaurus = Dinosaur("Austrosaurus", 130, 80, 100, 40, "Plant",forest_fury,leafy_healing,tail_smack,tree_slap)
dinos= [cryolophosaurus, triceratops, huaxiazhoulong, koleken, alamosaurus, yuanmouraptor, erlikosaurus, cetiosaurus, concavenator, austrosaurus]
#player dinos
player1_dinos=[]
player2_dinos=[]
player1_active=1
player2_active=1
#Functions
def attack(attacker,defender,move):
    #Damage Calc
    damage = int((((42*move.power*(attacker.attack/defender.defense))/50)+2))
    #Accuracy
    if random.randint(1,100)> move.accuracy:
        damage = 0
        return print("Missed")
    #STAB
    if attacker.type==move.type:
        damage*=1.5
    #Healing Moves
    if move.name == "Rest":
        attacker.health += 30
    if move.name == "Leafy Healing":
        attacker.health += 40
    #Type Chart
    if move.type == "Frost" and defender.type == "Plant":
        damage *= 2
    elif move.type == "Plant" and defender.type == "Frost":
        damage *= 0.5
    #Damage Dealt
    defender.health -= int(damage)
    return print(f"It did {damage} damage, {defender.name} has {defender.health} health remaining")
#attack(cryolophosaurus.attack, triceratops.defense, frost_bolt.power, frost_bolt.type, frost_bolt.accuracy, triceratops.type, triceratops.health)
def fight():
    game="running"
    while(game=="running"):
        print(f"{player1} choose your action:")
        action=int(input("1. Attack   2. Swap "))
        if action==1:
            print("Choose your attack:")
            time.sleep(0.5)
            print(f"1.{player1_dinos[(player1_active-1)].move1.name}")
            print(f"2.{player1_dinos[(player1_active-1)].move2.name}")
            print(f"3.{player1_dinos[(player1_active-1)].move3.name}")
            print(f"4.{player1_dinos[(player1_active-1)].move4.name}")
            move_number = int(input(f"{player1} choose the number of the attack that {player1_dinos[(player1_active-1)].name} will use: "))
            if move_number==1:
                attack(player1_dinos[(player1_active-1)],player2_dinos[(player2_active-1)],player1_dinos[(player1_active-1)].move1)
            elif move_number==2:
                attack(player1_dinos[(player1_active-1)],player2_dinos[(player2_active-1)],player1_dinos[(player1_active-1)].move2)
            elif move_number==3:
                attack(player1_dinos[(player1_active-1)],player2_dinos[(player2_active-1)],player1_dinos[(player1_active-1)].move3)
            elif move_number==4:
                attack(player1_dinos[(player1_active-1)],player2_dinos[(player2_active-1)],player1_dinos[(player1_active-1)].move4)
        elif action==2:
            count=1
            print(f"{player1}, which dino will you switch in to:")
            for i in range(len(player1_dinos)):
                if (player1_dinos[player1_active-1].name != player1_dinos[i].name):
                    print(f"{count}. {player1_dinos[i].name}")
                    count+=1
            time.sleep(0.5)
            input(int(f"{player1}, enter the number of the dino to switch in to:"))
#Initial Start Up
print("Welcome to the Dino Battle Simulator")
player1=input(str("Player 1, what is your name? "))
player2=input(str("Player 2, what is your name? "))
print(f"Choose Your Dinos:")
time.sleep(1)
for i in range(len(dinos)):
    print(f"{i+1}. {dinos[i].name}")
time.sleep(2)
#Dino Selections
choice1 = int(input(f"{player1}, enter the number of your first choice:"))
player1_dinos.append(dinos[choice1-1])
choice2= int(input(f"{player1}, enter the number of your second choice:"))
player1_dinos.append(dinos[choice2-1])
choice3= int(input(f"{player1}, enter the number of your third choice:"))
player1_dinos.append(dinos[choice3-1])
choice4= int(input(f"{player2}, enter the number of your first choice:"))
player2_dinos.append(dinos[choice4-1])
choice5= int(input(f"{player2}, enter the number of your second choice:"))
player2_dinos.append(dinos[choice5-1])
choice6= int(input(f"{player2}, enter the number of your third choice:"))
player2_dinos.append(dinos[choice6-1])
time.sleep(1)
#Active Dino Picker
print(f"{player1}, choose your active dinosaur:")
for i in range(len(player1_dinos)):
    print(f"{i+1}. {player1_dinos[i].name}")
player1_active = int(input(f"{player1}, enter the number of your active dinosaur:"))
print(f"{player2}, choose your active dinosaur:")
for i in range(len(player2_dinos)):
    print(f"{i+1}. {player2_dinos[i].name}")
player2_active = int(input(f"{player2}, enter the number of your active dinosaur:"))
time.sleep(1)
#Battle Begins
print(f"{player1} sends out {player1_dinos[player1_active-1].name}")
time.sleep(1)
print(f"{player2} sends out {player2_dinos[player2_active-1].name}")
time.sleep(1)
print("FIGHT")
time.sleep(1)
fight()