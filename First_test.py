'''def func(a, b):
    i = a
    while i < b:
        if i%2 == 0:
            print(i)
        i+=1

x = func
x(34, 37)'''

'''def ariphmetic(*args):
    res = 0
    a = float(input("Введите a"))
    b = float(input("Введите b"))
    c = input("Введите действие")
    if c == "+":
        res = a + b
    elif c == "-":
        res = a - b
    elif c == "*":
        res = a * b
    elif c == "/":
        res = a / b
    else:
        print("Неизвестная операция")
    print("Результат:", res)
ariphmetic()'''

'''def is_year_leap(*args):
    a = int(input("Введите год"))
    def recurs(a):
        b = 0
        if a % 4 != 0:
            print ("Год обычный")
        elif a / 4 == 1 or a / 4 == -1:
            print ("Год высокосный")
        else:
            if a > 0:
                while a > 1:
                    a = a / 4
                    b = b + 1
                if a == 1:
                    print ("Год высокосный. Степень =", b)
                else:
                    print ("Год обычный")
            else:
                while a < -1:
                    a = a / 4
                    b = b + 1
                if a == -1:
                    print ("Год высокосный. Степень =", b)
                else:
                    print ("Год обычный")
    return recurs(a)

is_year_leap()'''

'''def is_year_leap(*args):
    a = int(input("Введите год"))
    b = a
    if a > 0:
        while a > 0:
            a -= 4
        if a == 0:
            print("Год " + str(b) + " - высокосный")
        else:
            print("Год " + str(b) + " - обычный")
    else:
        while a < 0:
            a += 4
        if a == 0:
            print("Год " + str(b) + " - высокосный")
        else:
            print("Год " + str(b) + " - обычный")
is_year_leap()'''

'''a = int(input("Введите год"))
def is_year_leap(a):
    if a > 0:
        a -= 4
        return is_year_leap(a)
    else:
        if a == 0:
            print("Высокосный")
        else:
            print("Обычный")

is_year_leap(a)'''

'''import math
def square(*args):
    a = int(input("Please, enter a square side: "))
    p = 4*a
    s = a**2
    d = round(math.sqrt(a**2 + a**2), 2)
    res = ("Perimeter = {}".format(p), "Square = {}".format(s), "Diagonal = {}".format(d))
    print(res)
square()'''

'''def encrypt (*args):
    s = input("Введите строку: ")
    num = 0
    prev = s[0]
    res = ''
    for i in range(len(s)):
        if s[i] == prev:
            num += 1
            prev = s[i]
        else:
            numb = num if num > 0 else 1
            res = res + prev + str(numb)
            num = 1
            prev = s[i]
        if i == len(s) - 1:
            numb = num if num > 0 else 1
            res = res + prev + str(numb)
    return res
output = encrypt()
print(output)'''

'''def decrypt (*args):
    s = input("Введите зашифрованую строку: ")
    res = ''
    i = 0
    letter = s[::2]
    number = list(s[1::2])
    for let in letter:
        res = res + let * int(number[i])
        i += 1
    return res
print(decrypt())'''

'''def field(*args):
    x = int(input("Введите ширину: "))
    y = int(input("Введите высоту: "))
    s = [str(i+1) + "x" + str(j+1) for i in range(x) for j in range(y)]
    return(s)
s = field()

z = int(input("Введите количество мин: "))
def bom_loc(s):
    i = 1
    s_bom = []
    while i <= z:
        a = input("Введите расположение мины в формате: коор х коор: ")
        if s.count(a):
            s_bom.append(a)
            i += 1
        else:
            print("Вы ввели неправильное значение. Попробуйте снова.")
            print(s)
    return(s_bom)
s_bomb = bom_loc(s)
print(s_bomb)

def shoot(s):
    i = 0
    while i < z:
        k = 0
        a = input("Координаты исследования: ")
        if s.count(a):
            if s_bomb.count(a):
                i += 1
                s_bomb.remove(a)
                print("Вы нашли бомбу!")
            lv = list(a)
            for x in range(int(lv[0])-1, int(lv[0]) + 2 ):
                for y in range(int(lv[2]) - 1, int(lv[2]) + 2):
                    b = str(x) + 'x' + str(y)
                    if s_bomb.count(b):
                        k += 1
            print("Рядом находится " + str(k) + " бомб") if k > 1 else print("Рядом находится " + str(k) + " бомба")
        else:
            print("Такого значения не существует. Попробуйте значение с этого ряда: " + str(s))
    print("Вы нашли все бомбы!")
shoot(s)'''

'''def num_row(*args):
    n = int(input("Введите число: "))
    s = 0
    i = 1
    res = []
    mid = ''
    while s <= n:
        res = res + [i] * i
        i += 1
        s = len(res)
    if s != n:
        while s > n:
            res.pop()
            s -= 1
    for j in res:
        mid = mid + str(j)
    fin = ' '.join(mid)
    print(fin)
num_row()'''



'''def ent_num(*args):
    with open("../../Python/Test/task.txt") as lst:
        l = [line.strip() for line in lst]
        n = l[0].count(l[1])
        j = 0
        for i in l[0]:
            if i == l[1]:
                print(j, end = ' ')
            j += 1
        if n == 0:
            print("Отсутствует.")
    'with open("../../Python/Test/task.txt", 'wt') as lst_w:
        line_wr = input("Новое число: ")
        lst_w.write[1](line_wr)'
ent_num()'''

'''fib = lambda x: 1 if x <= 2 else fib(x - 1) + fib(x - 2)
fib(31)'''

