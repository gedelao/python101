from random import randint
input("Flip A Coin: ")

def flip_coin():
    flip = randint(0,1)
    if flip == 1:
        print("You flipped Head! ")
    else:
        print("You flipped Tails! ")

    
