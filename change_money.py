import os
import os.path
import pathlib

print('------------------')
print(os.getcwd()) # Путь к месту запуска
print(pathlib.Path(__file__).parent.resolve()) # Путь к папке, где лежит этот скрипт
print('------------------')



if os.path.isfile('money_1.txt') is False:
            a = open('money_1.txt', 'w+')
            a.write(str(0))
            a.close()
            b = open('money_1.txt')
            c = b.read()
            b.close()
            b = open('money_1.txt','w+')
            v = int(c) + 500
            v = str(v)
            b.write(str(v))
            b.close()
            n = open('money_1.txt')
elif os.path.isfile('money_1.txt') is True:
            b = open('money_1.txt')
            c = b.read()
            b.close()
            b = open('money_1.txt', 'w+')
            v = int(c) + 500
            v = str(v)
            b.write(str(v))
            b.close()
            n_1 = open('money_1.txt')



if os.path.isfile('money_2.txt') is False:
        a = open('money_2.txt', 'w+')
        a.write(str(0))
        a.close
        b = open('money_2.txt', 'r')
        c = b.read()
        b.close()
        b = open('money_2.txt', 'w+')
        v = int(c) + 500
        v = str(v)
        b.write(v)
        b.close()
        n = open('money_2.txt')
elif os.path.isfile('money_2.txt') is True:
        b = open('money_2.txt')
        c = b.read()
        b.close()
        b = open('money_2.txt', 'w+')
        v = int(c) + 500
        v = str(v)
        b.write(v)
        b.close()
        n = open('money_2.txt')


