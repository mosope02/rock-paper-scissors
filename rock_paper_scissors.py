from random import randint 
print("please select the element you want ")
player=input('rock,paper,or scissors')
while (player != ('rock' or 'paper' or 'scissors')):
    print("check your input")
print(player,'vs')
computer=randint(1,3)
#print(computer)
if computer==1:
    computer='rock'
elif computer==2:
    computer='paper'
else:
    computer='scissors'
print(computer)