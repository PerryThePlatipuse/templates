# 2
print("x y z w")
for x in range(0, 2):
    for y in range(0, 2):
        for z in range(0, 2):
            for w in range(0, 2):
                if not((x <= y) == (z <= w) or (x and w)):
                    print(x, y, z, w)


# 5
a = []
for x in range(10, 1001):
    i = int(bin(x)[3:], 2)
    if x - i not in a:
        a.append(x-i)
print(len(a))

# 6
import turtle as t

t.speed(0)
t.left(90)  # изначально голова направлена вправо
k = 40  # масштаб
for i in range(8):
    t.forward(6 * k)
    t.right(120)

t.pu()  # поднимаем перо
# решётка
for x in range(-5, 10):
    for y in range(-5, 10):
        t.goto(x * k, y * k)
        t.dot(5)

input() # чтобы не закрывалось мгновенно


# 12
s = '9' * 1000
while ('999' in s) or ('888' in s):
    if '888' in s:
        s = s.replace ('888', '9', 1)
    if '999' in s:
        s = s.replace ('999', '8', 1)
print(s)

# 14
x = 4**2020 + 2**2017 - 15
s = ''
while x != 0:
    s += str(x % 2)
    x //= 2
s = s[::-1]
print(s.count("1"))

# 15
for a in range(300, 0, -1):
    k = 0
    for x in range(0, 300):
        for y in range(0, 300):
            if (2*x + 3*y < 30) or (x + y >= a):
                k += 1
    if k == 90_000:
        print(a)
        break


# 16
def F(n):
    if n == 1:
        return 1
    if n > 1:
        return F(n - 1) + n
print(F(40))


# 17
f = open('17.txt')
a = [int(i) for i in f]
count = 0
mx = 0
s = 0
n = 0
for i in range(len(a)):
    if (a[i] % 2 == 0):
        s += a[i]
        n += 1
x = s / n
for i in range(len(a) - 1):
    if ((a[i] % 3 == 0) or (a[i + 1] % 3 == 0)) and ((a[i] < x) or (a[i + 1] < x)):
        count += 1
        mx = max(mx, a[i] + a[i + 1])
print(count, mx)


# 19
n1 = 7
target = 66


def win(x1, x2, move):
    if x1 + x2 >= target: return False
    possible_moves = [
        lose(x1 + 2, x2, move - 1),
        lose(x1 * 2, x2, move - 1),
        lose(x1, x2 + 2, move - 1),
        lose(x1, x2 * 2, move - 1)
    ]
    return any(possible_moves)


def lose(x1, x2, move):
    if x1 + x2 >= target: return True
    if move == 0: return False
    possible_moves = [
        win(x1 + 2, x2, move),
        win(x1 * 2, x2, move),
        win(x1, x2 + 2, move),
        win(x1, x2 * 2, move)
    ]
    return all(possible_moves)


ans_20 = []
ans_21 = []
for S in range(14, target):
    if win(n1, S, 2) and not(win(n1, S, 1)):
        ans_20.append(S)
    if lose(n1, S, 2) and not(lose(n1, S, 1)):
        ans_21.append(S)
print("20", ans_20)
print("21", ans_21)
