import random
computerPoints=0
UserPoints=0
round =1
while True :
 print("Game ",round)
 userChoice = input("Enter your choice  Rock(R) or Paper(P) or Scissor(S): ")
 Choice = ["Rock","Paper","Scissor"]
 computer = random.choice(Choice)

 print("Computer choice is : "+computer)
 if computer =="Rock" and userChoice =="P":
    UserPoints += 1
    print("You Win")
 elif computer == "Scissor" and userChoice =="P":
    computerPoints += 1
    print("You Lost")
 elif computer =="Paper" and userChoice =="R":
    print("You Lost")
    computerPoints +=1
 elif computer == "Scissor" and userChoice =="R":
    print("You Win")
    UserPoints +=1
 elif computer =="Rock" and userChoice =="S":
    print("You Lost")
    computerPoints += 1
 elif computer == "Paper" and userChoice =="S":
    print("You Win")
    UserPoints+=1
 elif computer[0] == userChoice :
    print("Draw")

 print("User points: " ,UserPoints)
 print("Computer points: ",computerPoints)
 x =input("Do you want to play another? Y-yes N-exit: ")
 if x=='Y' :
     round+=1
     print("\n")
     continue
 elif x=='N':
     break