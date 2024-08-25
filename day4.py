import random
choice=int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors."))
comp_choise=random.randint(0, 2)
zero='''
 _____         
| | | |/\  
|_|_|_|\ \    
|        /
\_______/     
 \______\   
'''
one='''
          ___..__
  __..--""" ._ __.'
              "-..__
            '"--..__";
 ___        '--...__"";
    `-..__ '"---..._;"
          """"----'   
'''
two='''
.-.  _
    | | / )
    | |/ /
   _|__ /_
  / __)-' )
  \  `(.-')
   > ._>-'
  / \/
'''

game=[zero,one,two]
print(game[choice])
print(f"Computer chose: {game[comp_choise]}")

if choice==0:
    if comp_choise==1:
        print("you lose")
    elif comp_choise==2:
        print("you win!")
    elif comp_choise==0:
        print("its a draw")
if choice==1:
    if comp_choise==2:
        print("you lose")
    elif comp_choise==0:
        print("you win!")
    elif comp_choise==1:
        print("its a draw")
if choice==2:
    if comp_choise==0:
        print("you lose")
    elif comp_choise==1:
        print("you win!")
    elif comp_choise==2:
        print("its a draw")