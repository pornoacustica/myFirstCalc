from colorama import init
from colorama import Fore, Back, Style
init()

print( Back.GREEN )
print( Fore.BLACK )

what = input('''Что делаем? (+, -, /, *, **, //, +%, -%)''')


print( Back.YELLOW )


if what == "+":
    a = float (input('Первое чиcло: '))
    b = float (input('Второе число: '))
    c = a + b
    print( Back.RED ) 
    print('Результат ' + str(c))
    
elif what == "-":
    a = float (input('Первое чиcло: '))
    b = float (input('Второе число: '))
    c = a - b
    print( Back.RED ) 
    print('Результат ' + str(c))
    
elif what == "*":
    a = float (input('Первое чиcло: '))
    b = float (input('Второе число: '))
    c = a * b
    print( Back.RED ) 
    print('Результат ' + str(c))
    
elif what == "/":
    a = float (input('Первое чиcло: '))
    b = float (input('Второе число: '))
    c = a / b
    print( Back.RED ) 
    print('Результат ' + str(c))

elif what == "**":
    a = float (input('Первое чиcло: '))
    b = float (input('Второе число: '))
    c = a ** b
    print( Back.RED ) 
    print('Результат ' + str(c))

elif what == "//":
    a = float (input('Корень из: '))
    c = a ** 0.5
    print( Back.RED ) 
    print('Результат ' + str(c))

elif what == "+%":
    a = float (input('Число: '))
    b = float (input("Процент: "))
    x = b / 100 + 1
    c = a * x
    print( Back.RED )
    print('Результат ' + str(c))

elif what == "-%":
    a = float (input('Число: '))
    b = float (input("Процент: "))
    c = a - (a / 100 * b)
    print( Back.RED )
    print('Результат ' + str(c))

else:
    print( Back.RED ) 
    print("ERROR!")

