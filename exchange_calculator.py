menu = """
Welcome to the exchange calculator 😎💲💱

1- Colombian pesos
2- Argenitinian pesos
3- Mexican pesos

choose your option
"""
option = input(menu)

if option == '1':
    colombian_pesos = float(input('How many Colombian pesos do you have? '))
    dollar_value = 3875
    dollars = colombian_pesos/dollar_value
    print(f'You have {dollars:.2f} dollars')
elif option == '2':
    argentinian_pesos = float(input('How many Argentinian pesos do you have? '))
    dollar_value = 65
    dollars = argentinian_pesos/dollar_value
    print(f'You have {dollars:.2f} dollars')
elif option == '3':
    mexican_pesos = float(input('How many Mexican pesos do you have? '))
    dollar_value = 24
    dollars = mexican_pesos/dollar_value
    print(f'You have {dollars:.2f} dollars')
else:
    print('please choose a right option')
