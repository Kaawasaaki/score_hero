import random


print("Welcome to the choose your own adventure game, where you get to decide your destiny!")

name = input("What is your name, O great one?: ").lower()
print("Welcome ", name)

choice = input("Are you ready to start your epic journey to become the next CR7!(Yes/No): ").lower()

if choice.lower() == "yes":
    print()
else:
    print("Not a valid input")
    quit
    
print("You are currently 18 years old, you just finished high school and you want to join an academy to kickstart your career. You are offered 3 choices:")
print("1.Kerala Blasters\n  2.Bengaluru FC\n  3.Mumbai City FC")

answer = input("Enter the option number to choose your club: ")

if answer.isdigit():
    if answer == "1":
        print("Welcome to Kerala Blasters FC!")
    elif answer == "2":
        print("Welcome to Bengaluru FC!(You made a good choice!)")
    elif answer == "3":
        print("Welcome to Mumbai FC")
else:
    print("Invalid Choice!")
    quit()
    
print("which position do you wish to play?:")

print("1.Attacker\n 2.Midfielder\n 3.Defender\n 4.Goalkeeper\n")

position = input("Enter the option number to choose your position: ").lower()

if position.isdigit():
    if position == "1":
        print("You are an Attacker!")
        print("Select one of the following: ")
        print("1. Left Winger\n 2.Right Winger\n 3.Striker\n")
        specific_postion = input("Enter the number of choice: ")
        if specific_postion == "1":
            print("You are a left winger!")
        if specific_postion == "2":
            print("You are a right winger!")
        if specific_postion == "3":
            print("You are a striker!")
            
    if position == "2":
        print("You are a midfielder")
        print("Select one of the following:")
        print("1. Central Midfielder\n 2. Central Attacking Midfielder\n 3. Central Defensive Midfielder\n")
        midfielder_position = input("Enter the cumber of choice: ")
        if midfielder_position == "1":
            print("You are a CM!")
        if midfielder_position == "2":
            print("You are a CAM!")
        if midfielder_position == "3":
            print("You are a CDM!")
            
    if position == "3":
        print("You are a defender")
        print("Select your position: ")
        print("1. Left Back\n 2. Center Back\n 3. Right Back\n")
        defender_position = input("Enter the number of choice: ")
        if defender_position == "1":
            print("You are a left back!")
        if defender_position == "2":
            print("You are a Center Back!")
        if defender_position == "3":
            print("You are a Right Back!")
            
    if position == "4":
        print("You are a goalkeeper!")
else:
    print("Invalid Choice!")
    quit()


user_input = input("type 's' to generate your stats: ")

pace = 0
dribbling = 0
diving = 0
shooting = 0
passing = 0
defending = 0

if user_input.lower() == "s":

    stats_pace = random.randrange(1,99)
    stats_dribbling = random.randrange(1,99)
    stats_shooting = random.randrange(1,99)
    stats_passing = random.randrange(1,99)
    stats_defending = random.randrange(1,99)
    stats_diving = random.randrange(1,99)

    print("Pace: ", stats_pace )
    print("Dribbling: ", stats_dribbling)
    print("Shooting: ", stats_shooting)
    print("Passing: ",stats_passing)
    print("Diving: ", stats_diving)
    print("Defending: ", stats_defending)
    
    total_stats =  str(stats_pace + stats_defending + stats_diving + stats_shooting + stats_passing + stats_dribbling)
    print("Overall:" , int(total_stats) % 100)
else:
    print('Invalid input!')
    quit()
    
goal_scored =  random.randint(1,500)

answer = input("type 'g' to find how many goals you have scored: ")

if answer.lower() == "g":
    print("You have scored "+ str( goal_scored) + " goals")
else:
    print("Invalid Input")
    quit()
    
assists = random.randint(1,500)

answer = input("Enter 'a' to find how many assists you got: ")

if answer.lower() == "a":
    print("You have got " + str(assists) + " assists")
else:
    print("Invalid Input")
    quit()
    
answer = input("Enter 'r' to see at what age you would retire: ")

age = random.randint(19,45)

if answer.lower() == "r":
    print("You retired at " + str(age) + " years old")


    






    
