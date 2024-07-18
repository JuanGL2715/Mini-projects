import random
points = [0,0,0,0]
players = input("How many players will play 2-4?")
index = 0
def roll():
    cont = 0
    while cont < int(players):
        dice = random.randrange(1, 7)
        print("you took ", dice, "in the dice player", cont+1)
        points[cont]+=dice
        if points[cont]>=50:
            index = cont
            return True
        print("Now you have", points[cont], "points")
        cont+=1
    return False
        

while True:
    if players.isdigit():
        if 2<= int(players) <= 4:
            if roll() :
                print("The winner is player", index+1, "with",points[index], "points")
                break
            else:
                print("###MARCADOR###")
                for i in range(0, int(players)):
                    print("player", i+1, ":", points[i])
                roll()
                
        else:
            print("Players must be between 2 and 4")
            players = input("How many players will play 2-4?")
    else:
        print("Invalid, try again.")
        players = input("How many players will play 2-4?")