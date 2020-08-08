def is_prime(number):
    counter = 0
    for i in range (1, number + 1): #Runs all the numbers between 2 and the input number
        if i == 1 or i == number: # skips the number 1 and the input number
            continue
        if number % i == 0: #cheks the module 
            counter += 1
    if counter == 0:
        return True
    else:
        return False


def run():
    number = int(input('Write a number please: '))
    if is_prime(number):
        print('is prime')
    else:
        print('is not prime')


if __name__ == '__main__':
    run()