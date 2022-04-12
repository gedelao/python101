from flipCoin import flip_coin
from Dice_Roll import roll_die

def main():
    while True:
        user_input = (input('''
        1 - Flip a coin: 
        2 - Roll a die: 
        q - exit: 
        '''))

        if user_input == "1":
            flip_coin()
        if user_input == "2":
            roll_die()
        if user_input == "q":
            exit
main()