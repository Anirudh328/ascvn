import random

rand=random.randint(0,9)
chance=0
print("guessano 1 or 9")

while chance<3 :
    guess=int(input("type it in (hint:its a no)"))
    if guess ==rand:
        print("ulose,sike u win")
        break
    elif guess <rand:
        print("your dreams are too steap")
    else :
        print("u dreams r not going to come true,start low and go big")
    chance +=1
if not chance <3:
    print("youlost",rand)
