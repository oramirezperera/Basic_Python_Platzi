menu = """
Welcome to the exchange calculator 😎💲💱

1- Colombian pesos
2- Argenitinian pesos
3- Mexican pesos

choose your option
"""

def conversor(type_pesos,dollar_value):
    colombian_pesos = float(input('How many '+ type_pesos +' pesos do you have? '))
    dollars = colombian_pesos/dollar_value
    print(f'You have {dollars:.2f} dollars')


option = int(input(menu))

if option == 1:
    conversor('Colombian', 3875)
elif option == 2:
    conversor('Argentinian', 65)
elif option == 3:
    conversor('Mexican', 24)
else:
    print('please choose a right option')
