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
frost_bolt= Attack("Frost Bolt", 90, 100, "Ice")
grassy_horn= Attack("Grassy Horn", 110, 90, "Plant")
rock_slam = Attack("Rock Slam", 80, 95, "Stone")
shadow_bite = Attack("Shadow Bite", 90, 100, "Dark")
fire_claw = Attack("Fire Claw", 100, 95, "Fire")
water_beam = Attack("Water Beam", 90, 100, "Water")
sand_tornado = Attack("Sand Tornado", 130, 70, "Sand")
#Dinosaurs
cryolophosaurus= Dinosaur("Cryolophosaurus", 105, 100, 75, 90, "Ice", frost_bolt,1,1,1)
triceratops= Dinosaur("Triceratops", 140, 120, 100, 40, "Plant", grassy_horn,1,1,1)
huaxiazhoulong = Dinosaur("Huaxiazhoulong", 125, 70, 120, 50, "Stone", rock_slam,1,1,1)
koleken = Dinosaur("Koleken", 90, 120, 70, 100, "Plain",1,1,1,1)
alamosaurus = Dinosaur("Alamosaurus", 160, 90, 90, 20, "Stone", rock_slam,1,1,1)
yuanmouraptor = Dinosaur("Yuanmouraptor", 90, 110, 80, 120, "Dark", shadow_bite,1,1,1)
erlikosaurus = Dinosaur("Erlikosaurus", 100, 140, 60, 70, "Fire", fire_claw,1,1,1)
cetiosaurus = Dinosaur("Cetiosaurus", 150, 80, 100, 30, "Water", water_beam,1,1,1)
concavenator = Dinosaur("Concavenator", 110, 90, 70, 100, "Sand", sand_tornado,1,1,1)
austrosaurus = Dinosaur("Austrosaurus", 130, 80, 100, 40, "Plant",1,1,1,1)
dinos= [cryolophosaurus, triceratops, huaxiazhoulong, koleken, alamosaurus, yuanmouraptor, erlikosaurus, cetiosaurus, concavenator, austrosaurus]
#player dinos
player1_dinos=[]
player2_dinos=[]
player1_active=1
player2_active=1
#Functions
def attack(attack,defense,power,attack_type,accuracy,defense_type,defender_health):
    damage = int((((42*power*(attack/defense))/50)+2))
    if random.randint(1,100)> accuracy:
        damage = 0
        return print("Missed")
    if attack_type == "Ice" and defense_type == "Plant":
        damage *= 2
    elif attack_type == "Plant" and defense_type == "Ice":
        damage *= 0.5
    defender_health -= int(damage)
    return print(f"It did {damage} damage, {defender_health} health remaining")
#attack(cryolophosaurus.attack, triceratops.defense, frost_bolt.power, frost_bolt.type, frost_bolt.accuracy, triceratops.type, triceratops.health)
def fight():
    print(f"{player1} choose your action:")
    action=int(input("1. Attack   2. Swap "))
    if action==1:
        print("Choose your attack:")
        time.sleep(0.5)
        print(f"1.{player1_dinos[(player1_active-1)].move1.name}")
        print(f"2.{player1_dinos[(player1_active-1)].move2.name}")
        print(f"3.{player1_dinos[(player1_active-1)].move3.name}")
        print(f"4.{player1_dinos[(player1_active-1)].move4.name}")
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