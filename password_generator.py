import random

def password_generator():
    upper_case = ['A', 'B', 'C', 'D', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    lower_case = ['a', 'b', 'c', 'd', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
    symbols = ['!', '#', '$', '&', '/', '(', ')', '.']
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