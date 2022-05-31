import math

eps = 0.00001


# info
# classes: Point, Line, triangle, circle, fraction
# defs: площаь треугольника через три вершины striangle(a, b, c)
# высота треугольника по трем точкам из точки a htriangle(a, b, c)
# точка пересечения высот треугольника по трем вершинам triangleHpoint(a, b, c)
# точка пересечения медиан треугольника по трем вершинам triangleMpoint(a, b, c)
# точка пересечения биссектрис треугольник по трем вершинам triangleBpoint(a, b, c)
# точка персечения серперов треугольника по трем вершинам trianglePpoint(a, b, c)
# лежит ли точка в треугольнике (включая стороны) pointintriangle(point, a, b, c)
# лежит ли точка в выпуклом многоугольнике pointinfigure1(point, n, list)
# расстояние от точки до прямой dist_pl(point, line)
# расстояние от точки до отрезка dist_pi(p1, p2, p3)
# лежит ли точка на прямой pointonline(point, line)
# равенство приблизительное eq(a, b)
# неравенство больше ли а, чем б на eps greater(a, b)
# две точки с одной стороны от прямой pointsandline(a,b,line)
# задача прямой двумя точками line2point(a, b)
# считать точку через входные данные readpoint()
# считать прямую через три строки readline()
# параллельная прямая на расстояние parallellinedist(line, r)
# расстояние между парой точек dist(a, b)
# середина отрезка пары точек middle(a, b)
# пересечение двух прямых intersection(a, b) не готово
# создать новый круг через точку и радиус или координаты центра и радиус newcirc(a, b, (c))
# перпендекуляр к прямой через точку вне нее normaltoline(point, line)
# проверка на простоту issimple(a)
# разбиение на простые множители simples(a)
# красивое деление выдает два массива простых не делящихся друг на друга цифр dev(a, b)
# красивое деление выдает целую часть и дробь devrem(a, b)
# сложение дробей sumfracts(a, b)
# вычитание дробей subfracts(a,b)
# сравнение дробей greaterfract(a, b) True if a>b
# считывание дроби через входные данные readfract()
# равенство дробей eqfracts(a,b)

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def printpoint(self):
        print(self.x, self.y)


class Line:
    def __init__(self, a, b, c):
        self.a = a
        self.b = b
        self.c = c


def htriangle(x, y, z):
    return striangle(x, y, z) * 2 / dist(y, z)


class triangle:
    def __init__(self, a, b, c):
        self.x = a
        self.y = b
        self.z = c
        self.s = striangle(a, b, c)
        self.r = 0
        self.R = 0


class circle:
    def __init__(self, a, b, r):
        self.x = a
        self.y = b
        self.r = r


def line2point(k, l):
    xx = l.x - k.x
    yy = l.y - k.y
    a = yy
    b = xx * (-1)
    c = (k.x * yy * (-1) + k.y * xx)
    return (Line(a, b, c))


def readline():
    a = int(input())
    b = int(input())
    c = int(input())
    return Line(a, b, c)


def readpoint1():
    a = input().split()
    return (Point(int(a[0]), int(a[1])))


def readpoint2():
    a = int(input())
    b = int(input())
    return (Point(a, b))


def readpoint():
    a = input()
    if len(a.split()) == 2:
        return Point(float(a.split()[0]), float(a.split()[1]))
    else:
        b = float(input())
        a = float(a)
        return (Point(a, b))


def pointsandline(m, mm, line):
    x = (m.x * line.a + m.y * line.b + line.c) * (mm.x * line.a + mm.y * line.b + line.c)
    if x > 0:
        print('YES')
    else:
        print('NO')


def fine(n, list):
    nlist = []
    for i in range(n - 2):
        nlist.append(line2point(list[i], list[i + 1]))
    sum = 0
    for i in range(n - 2):
        if (list[i + 2].x * nlist[i].a + list[i + 2].y * nlist[i].b + nlist[i].c) < 0:
            sum += 1
    return sum


def pointonline(a, b):
    x = a.x
    y = a.y
    smth = (x * b.a + y * b.b + b.c)
    return (eq(smth, 0))


def dist_pl(p, l):
    if l.b != 0:
        c = Point(100, (((l.a * 100 + l.c) / l.b) * (-1)))
        d = Point(200, (((l.a * 200 + l.c) / l.b) * (-1)))
    else:
        c = Point((((l.b * 100 + l.c) / l.a) * (-1)), 100)
        d = Point((((l.b * 100 + l.c) / l.a) * (-1)), 200)
    return htriangle(p, c, d)


def dist_pi(a, b, c):
    line = line2point(b, c)
    if dist(a, b) ** 2 > (dist(a, c) ** 2 + dist(b, c) ** 2) or dist(a, c) ** 2 > (dist(a, b) ** 2 + dist(b, c) ** 2):
        return (min(dist(a, b), dist(a, c)))

    else:

        return (dist_pl(a, line))


def sign(a):
    if a > 0:
        return 1
    elif eq(a, 0):
        return 0
    else:
        return -1


def sfigure(n, list):
    a = 0
    b = 0
    for i in range(n - 1):
        a += list[i].x * list[i + 1].y
    a += list[n - 1].x * list[0].y
    for i in range(n - 1):
        b += list[i].y * list[i + 1].x
    b += list[n - 1].y * list[0].x
    return abs(a - b) / 2


def pointintriangle(p, a, b, c):
    l1 = line2point(a, b)
    l2 = line2point(b, c)
    l3 = line2point(c, a)
    s1 = p.x * l1.a + p.y * l1.b + l1.c
    s2 = p.x * l2.a + p.y * l2.b + l2.c
    s3 = p.x * l3.a + p.y * l3.b + l3.c
    if (sign(s1) == sign(s2) == sign(s3)) or (sign(s1) == sign(s2) and sign(s3) == 0) or (
            sign(s1) == sign(s3) and sign(s2) == 0) or (sign(s3) == sign(s2) and sign(s1) == 0):
        return True
    else:
        return False


def pointinfigure1(p, n, list):
    nlist = []
    for i in range(n):
        l = line2point(list[i], list[(i + 1) % n])
        nlist.append(l)
    a = sign(p.x * nlist[0].a + p.y * nlist[0].b + nlist[0].c)
    b = sign(p.x * nlist[1].a + p.y * nlist[1].b + nlist[1].c)
    c = min(a, b)
    check = 0
    if abs(a - b) == 2:
        check += 1
    if c >= 0:
        for i in range(n - 2):
            if not sign(sign(p.x * nlist[i + 2].a + p.y * nlist[i + 2].b + nlist[i + 2].c)) >= 0:
                check += 1
    else:
        for i in range(n - 2):
            if not sign(sign(p.x * nlist[i + 2].a + p.y * nlist[i + 2].b + nlist[i + 2].c)) <= 0:
                check += 1
    if check == 0:
        return True
    else:
        return False


def vectorangle(a, b):
    c = Point(0, 0)
    cos = (a.x * b.x + a.y * b.y) / (dist(a, c) * dist(b, c))
    return math.acos(cos)


def readfract():
    a = input()
    if len(a.split()) == 2:
        return fraction(int(a.split()[0]), int(a.split()[1]))
    else:
        b = int(input())
        a = int(a)
        return (fraction(a, b))


def eq(a, b):
    return (abs(a - b) < eps)


def eqfracts(a, b):
    if a.nnum == b.nnum and a.nden == b.nden:
        return True
    else:
        return False


def greater(a, b):
    if eq(a, b):
        return False
    elif a > b:
        return True
    else:
        return False


def greaterfract(a, b):
    x = subfracts(a, b)
    if x.nnum > 0:
        return True
    else:
        return False


def dist(a, b):
    return math.sqrt((a.x - b.x) ** 2 + (a.y - b.y) ** 2)


def middle(a, b):
    x = (a.x + b.x) / 2
    y = (a.y + b.y) / 2
    return (Point(x, y))


def normaltoline(point, line):
    x = point.x
    y = point.y
    a = line.b
    b = line.a * (-1)
    c = line.a * y - a * x
    return Line(a, b, c)


def triangleHpoint(a, b, c):
    l1 = line2point(a, b)
    l2 = line2point(a, c)
    h1 = normaltoline(b, l2)
    h2 = normaltoline(c, l1)
    x = intersection(h1, h2)
    return (Point(x[1], x[2]))


def triangleMpoint(a, b, c):
    a1 = middle(b, c)
    b1 = middle(a, c)
    l1 = line2point(b, b1)
    l2 = line2point(a, a1)
    x = intersection(l1, l2)
    return Point(x[1], x[2])


def triangleBpoint(a, b, c):
    A = dist(b, c)
    B = dist(a, c)
    C = dist(b, a)
    x = ((a.x * A) + (b.x * B) + (c.x * C)) / (A + B + C)
    y = ((a.y * A) + (b.y * B) + (c.y * C)) / (A + B + C)
    return Point(x, y)


def trianglePpoint(a, b, c):
    l1 = line2point(a, b)
    l2 = line2point(a, c)
    p1 = middle(a, b)
    p2 = middle(a, c)
    per1 = normaltoline(p1, l1)
    per2 = normaltoline(p2, l2)
    x = intersection(per1, per2)
    return Point(x[1], x[2])


def pointonsection(a, b, c):
    line = line2point(a, b)
    if not pointonline(c, line):
        return False
    else:
        if min(a.x, b.x) < c.x < max(a.x, b.x) or min(a.y, b.y) < c.y < max(a.y, b.y) or (
                a.x == c.x and a.y == c.y) or (b.x == c.x and b.y == c.y):
            return True
        else:
            return False


def parallellinedist(line, r):
    c2 = line.c - (r * ((line.a ** 2 + line.b ** 2) ** 0.5))
    return Line(line.a, line.b, c2)


def striangle(x, y, z):
    s = abs((x.x * y.y + y.x * z.y + z.x * x.y) - (x.y * y.x + y.y * z.x + z.y * x.x)) / 2

    return s


def intersection(A, B):
    if not eq(A.a * B.b, B.a * A.b):
        e = (A.b * B.c - A.c * B.b) / (A.a * B.b - A.b * B.a)
        f = (A.a * B.c - A.c * B.a) / (A.b * B.a - A.a * B.b)
        return ([1, e, f])
    else:
        if eq(A.a * B.c, B.a * A.c) and eq(A.b * B.c, A.c * B.b):
            return (["2"])
        else:
            return (["0"])


def newcirc(a, b, c=-1):
    if c == -1:
        a = circle(a.x, a.y, b)
    else:
        a = circle(a, b, c)
    return a


def issimple(a):
    b = 0
    for i in range(int(a ** 0.5) - 1):
        if a % (i + 2) == 0:
            b += 1
    if b == 0:
        return True
    else:
        return False


def simples(a):
    arr = []
    x = a
    a = a
    b = 2
    while b <= int(x / 2):
        if a % b == 0 and issimple(b):
            arr.append(b)
            a = a / b
        else:
            b += 1
    if arr == []:
        arr.append(x)
    return (arr)


def dev(a, b):
    a = simples(a)
    b = simples(b)
    res = []
    for i in range(len(a)):
        c = 0
        x = -1
        for v in range(len(b)):
            if a[i] == b[v] and c == 0:
                c += 1
                x = v
        if x != -1:

            b.pop(x)
        else:
            res.append(a[i])
    if res == []:
        res = [1]
    if b == []:
        b = [1]

    return res, b


def devtofine(a, b):
    x = 1
    y = 1
    for i in a:
        x *= i
    for i in b:
        y *= i
    return x, y


def devrem(a, b):
    x = a
    y = b
    res = a // b
    x = x - res * b
    q, w = dev(x, b)
    q, w = devtofine(q, w)
    return res, q, w


class fraction:
    def __init__(self, a, b):
        if type(a) is float:
            a = int(a)
            b = int(b)
        if type(a) is int:
            n = a
            m = b
            a = simples(abs(a))
            b = simples(abs(b))
            if n < 0:
                a.append(-1)
            if m < 0:
                b.append(-1)

        res = []
        for i in range(len(a)):
            c = 0
            x = -1
            for v in range(len(b)):
                if a[i] == b[v] and c == 0:
                    c += 1
                    x = v
            if x != -1:

                b.pop(x)
            else:
                res.append(a[i])
        if res == []:
            res = [1]
        if b == []:
            b = [1]

        z = -1
        q = 0
        for i in range(len(res)):
            if res[i] < 0:
                if q == 1:
                    res[i] = abs(res[i])
                    res[z] = abs(res[z])
                    q = 0
                else:
                    q = 1
                    z = i
        t = -1
        r = 0
        for i in range(len(b)):
            if b[i] < 0:
                if r == 1:
                    b[i] = abs(b[i])
                    b[t] = abs(b[t])
                    r = 0
                else:
                    r = 1
                    t = i

        if r == 1 and q == 1:
            res[z] = abs(res[z])
            b[t] = abs(b[t])
        elif r == 1:
            b[t] = abs(b[t])
            b.append(-1)
        elif q == 1:
            res[z] = abs(res[z])
            res.append(-1)

        x = devtofine(res, b)

        self.nnum = x[0]
        self.nden = x[1]
        self.num = res
        self.den = b


def sumfracts(a, b):
    num = a.nnum * b.nden + b.nnum * a.nden
    den = a.nden * b.nden
    return fraction(num, den)


def subfracts(a, b):
    num = a.nnum * b.nden - b.nnum * a.nden
    den = a.nden * b.nden
    return fraction(num, den)


def multfracts(a, b):
    num = a.nnum * b.nnum
    den = a.nden * b.nden
    return (fraction(num, den))


def divfracts(a, b):
    num = a.nnum * b.nden
    den = a.nden * b.nnum
    return fraction(num, den)


def giveup():
    a = readpoint()
    b = readpoint()
    print(vectorangle(a, b))


def me():
    while True:
        giveup()


giveup()
# me()
