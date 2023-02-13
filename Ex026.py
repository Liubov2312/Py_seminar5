'''Задача 26: Напишите программу, которая на вход принимает 
два числа A и B, и возводит число А в целую степень B с 
помощью рекурсии.'''

def exponentiation(A, B):   
    if B == 0:
        return 1
    elif B == 1:
        return A
    else:
        return A * exponentiation(A, (B - 1))

print(exponentiation(int(input('Введите число А: ')), int(input('Введите число В - степень: '))))