import random

def password_generator():
    upper_case = ['A', 'B', 'C', 'D', 'F', 'G']
    lower_case = ['a', 'b', 'c', 'd', 'f', 'g']
    symbols = ['!', '#', '$', '&', '/', '(', ')']
    numbers = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    
    char = upper_case + lower_case + symbols + numbers
    password = []

    for i in range(15):
        char_random = random.choice(char)
        password.append(char_random)
    
    password = ''.join(password)
    return password

def run():
    password = password_generator()
    print(f'Your new password is {password}')


if __name__ == '__main__':
    run()