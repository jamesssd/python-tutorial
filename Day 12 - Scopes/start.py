# ################### SCOPE #########################

# enemies = 1

# def increase_enemies():
#     enemies = 2
#     print(f"enemies inside functions: {enemies}")
    
# increase_enemies()
# print(f"enemies outside the function: {enemies}")

# #Local Scope: exist within the function
# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)
    
# drink_potion()
#print(potion_strength)

#Global Scope
# player_health = 10

# def drink_potion():
#     potion_strength = 2
#     print(player_health)

# drink_potion()

#No block scope for python
# game_level = 3
# enemis = ["Skeleton", "Zombies", "Alien"]
# if game_level < 5:
#     new enemy = enemis[0]
    
# print(new_enemy)  

#Modifying Global Scope
#variable before is a global scope
# enemies = 1

# #function below is a local scope
# def increase_enemies():
#     #To change a global variable, you must use a return ie,.
#     print(f"enemies insdie function: {enemies}")
#     return enemies + 1

# enemies = increase_enemies()
# print(f"enemies outside function: {enemies}")

#Global Constant Scope
#to declare a global constant scope, you must capitalize the declaration
PI = 3.14259
TWITTER_HANDLE = "@jamesssd"
print(PI)
PI = 1.12
print(PI)

