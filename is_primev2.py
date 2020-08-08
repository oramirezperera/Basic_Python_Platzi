"""Second version of is_prime trying to use another method"""
def is_prime(number):
    counter = 0 
    if number % 2 == 0:
        counter += 1
    elif number % 3 == 0:
        counter += 1
    elif number % 5 == 0:
        counter += 1
    elif number % 7 == 0:
        counter += 1
    elif number % 11 == 0:
        counter += 1
    
    if counter == 0:
        return True
    else:
        return False
    


def run():
    number = int(input('Write a number please: '))
    if is_prime(number):
        print('Is a prime number')
    else:
        print('Is not a prime number')


if __name__ == '__main__':
    run()