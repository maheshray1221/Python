# 01.

# f = open("poem.txt")

# content = f.read()

# if("twinkle" in content ):
#     print("yes there is a twinkle")
# else:
#     print("there is No twinkle")
    
# f.close()

# 02.

import random

def game():
    print("welcome to the game")
    score = random.randint(1,15)

    with open("hiscore.txt") as f:
        hiscore = f.read()

    if(hiscore != ""):
        hiscore = int(hiscore)
    else:
        hiscore = 0
    print(f"You are score is : {score}")

    if(score> hiscore):
        with open("hiscore.txt","w") as f:
            f.write(str(score))
    else:
        print("play again")
    
    
    
game()