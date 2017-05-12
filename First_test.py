
# ..........................LEAP YEAR (version 1).......................
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
# ---------------------------------------------------------------------

# ........................LEAP YEAR (version 2).........................
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
# ----------------------------------------------------------------------

# .......................LEAP YEAR (elegantly).......................
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
# ----------------------------------------------------------------------

# ................Encrypting a string (aaabb = 3a2b).................
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
# ---------------------------------------------------------------------

# ..................Decrypting a string (3a2b = aaabb)...............
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
# ----------------------------------------------------------------------

# ................................SAPPER..............................
'''
# Game field creation
def field(*args):
    x = int(input("Введите ширину поля игры: "))
    y = int(input("Введите высоту поля игры: "))
    s = [str(i+1) + "x" + str(j+1) for i in range(x) for j in range(y)]
    return(s)
s = field()

# Location of mines
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

# Game process
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
# --------------------------------------------------------------------



