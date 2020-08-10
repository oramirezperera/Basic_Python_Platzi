import random

def run():
    aleatory_number = random.randint(1, 100)
    chosen_number = int(input('Choose a number between 1 and 100: '))
    while chosen_number != aleatory_number:
        if chosen_number < aleatory_number:
            print('The number is bigger')
        else:
            print('The number is smaller')
        chosen_number = int(input('Choose another number'))
    print('You won!')

if __name__ == '__main__':
    run()