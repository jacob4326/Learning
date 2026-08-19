health=100
dead=False
speed = 20
damageM = 1
class Condition:
    def __init__(self, name, speed_modifier, damage_multiplier, time):
        self.name=name
        self.speed_modifier=speed_modifier
        self.damage_multiplier=damage_multiplier
        self.time=time

resistance= Condition("resistance", 1, 0.5, 30)
poisoned = Condition("poisoned", 0.5, 1, 60)
vulnerable = Condition("vulnerable", 1, 2, 15)
current_conditions=[]

def dead_check():
    global dead
    if health <=0:
        dead = True
    else:
        dead = False
def condition_check():
    global speed
    global damageM
    for i in range (len(current_conditions)):
        speed=  speed *current_conditions[i].speed_modifier
        damageM= damageM * current_conditions[i].damage_multiplier

def damage(value):
    global health
    condition_check()
    health=health-(value*damageM)
    dead_check()

def add_condition(condition):
    global current_conditions
    in_stack = False
    for i in range (len(current_conditions)):
        if current_conditions[i]==condition:
            in_stack = True
            break
    if not in_stack:
        current_conditions.append(condition)

def sort_conditions():
    global current_conditions
    for i in range(len(current_conditions)):
        shortest = i
        for j in range(i + 1, len(current_conditions)):
            if current_conditions[j].time > current_conditions[shortest].time:
                shortest = j
        current_conditions[i], current_conditions[shortest] = current_conditions[shortest], current_conditions[i]
    print(current_conditions[0].name, current_conditions[1].name, current_conditions[2].name)

def remove_earliest_condition():
    global current_conditions
    sort_conditions()
    if len(current_conditions)>=1:
     current_conditions.pop()
    else:
        print("No current conditions")
