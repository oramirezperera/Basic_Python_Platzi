import random

def run():
    aleatory_number = random.randint(1, 100)
    chosen_number = int(input('Choose a number between 1 and 100: '))
    steps = 0
    while chosen_number != aleatory_number:
        if chosen_number < aleatory_number:
            print('The number is bigger')
        else:
            print('The number is smaller')
        chosen_number = int(input('Choose another number: '))
        steps += 1
    print(f'You won! in {steps} steps')

if __name__ == '__main__':
    run()