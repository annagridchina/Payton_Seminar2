# Задача 14: Требуется вывести все целые степени двойки (т.е. числа вида 2k), не превосходящие числа N.  10 ->  2 4 8

N  = int(input('N = ')) 
i = 2
power = 1
while i <= N:
    i = 2 ** power
    if i > N:
            print('STOP')
    else:
         power = power + 1  
    print(i)
    
