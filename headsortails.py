import random
import colorsys
import time

class colors:
    green = '\033[92m'
    yellow = '\033[93m'
    red = '\033[91m'

def whole():
    go = input("Ready to flip the coin? \"Y/N\"")

    if go == "y" or go == "Y":
        num = random.randint(1,2)
        if int(num) == 1:
            time.sleep(1)
            print(colors.red + "You got -> " + colors.green + " HEADS")
        if int(num) == 2:
            time.sleep(1)
            print(colors.red + "You got -> " + colors.green + " TAILS")
            time.sleep(1)
            whole()

        
    if go == "n" or go == "N":
                time.sleep(1)
                whole()
                
    else:
        pass

print (colors.red + "Welcome to heads or tails")
whole()
