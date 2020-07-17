import turtle
bob = turtle.Turtle()
print(bob)

# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)
# bob.lt(90)
# bob.fd(100)

# for i in range(4):
#     print('Hello!')

# for i in range(4):
#     bob.fd(100)
#     bob.lt(90)


def polyline(t, length, sides, angle):
    """Draws n line segments with the given length and
    angle (in degrees) between them. t is a turtle.
    """
    for i in range(sides):
        t.fd(length)
        t.lt(angle)


def square(t, length):
    for i in range(4):
        t.fd(length)
        t.lt(90)

#square(bob, 200)


def polygon(t, length, n):
    polyline(t, length, n, 360/n)
    # for i in range(n):
    #     t.fd(length)
    #     t.lt(360/n)

#polygon(bob, 100, 6)


def circle(t, r):
    pi = 3.141592653589793
    circum = 2 * pi * r
    #sides = 100
    sides = int(circum / 3) + 3
    n = circum / sides
    polygon(t, n, sides)

#circle(bob, 50)


def arc(t, r, angle):
    pi = 3.141592653589793
    circum = 2 * pi * r
    arc_length = circum * angle / 360
    arc_sides = int(arc_length / 3) + 1
    side_length = arc_length / arc_sides
    side_angle = float(angle) / arc_sides
    polyline(t, side_length, arc_sides, side_angle)

# arc(bob, r=100, angle=120)

# turtle.mainloop()


def is_between(x, y, z):
    if x <= y and y <= z:
        return True
    else:
        return False


print(is_between(0, -10, 1))


def factorial(n):
    space = ' ' * (4 * n)
    print(space, 'factorial', n)
    if n == 0:
        print(space, 'returning 1')
        return 1
    else:
        recurse = factorial(n-1)
        result = n * recurse
        print(space, 'returning', result)
        return result


factorial(5)


def Ackermann(m, n):
    if m == 0:
        return n + 1
    elif m > 0 and n == 0:
        return Ackermann(m - 1, 1)
    elif m > 0 and n > 0:
        return Ackermann(m - 1, Ackermann(m, n - 1))
    else:
        return print('Ackermann function is defiend for non negative numbers only.')


print(Ackermann(3, 4))


def countdown(n):
    while n > 0:
        print(n)
        n = n - 1
    print('Blastoff!')


countdown(10)


def my_sqrt(a):
    x = a/2
    while True:
        print(x)
        y = (x + a/x) / 2
        if abs(y - x) < 0.000001:
            break
        x = y


my_sqrt(9)

fruit = 'banana'
print(fruit[:])


def my_count(word, character):
    count = 0
    for letter in word:
        if letter == character:
            count += 1
    return count


print(my_count('testing', 't'))

# File and text strings operations

# Exercise 9.1: Print words with length greater than 20
fin = open('words.txt')
for line in fin:
    word = line.strip()
    if len(word) > 20:
        print(word)

# Exercise 9.2: Print and count numnber of words that have no 'e'


def has_no_e(word):
    if 'e' not in word:
        return True
    return False


count_no_e = 0
fin.seek(0)
for line in fin:
    word = line.strip()
    if has_no_e(word) == True:
        count_no_e = count_no_e + 1
        print(word)

print(count_no_e)

# Exercise 9.6: abecedarian


def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


fin.seek(0)
count_abecedarian = 0
for line in fin:
    word = line.strip()
    if is_abecedarian(word):
        print(word)
        count_abecedarian += 1
print(count_abecedarian)

test = [1, 2, 3, 4, 5]
for i in test:
    print(type(i))


test_str = 'test string'
print('test' in test_str)

# Exercise 10.1. Write a function called nested_sum that takes a list of lists of integers and adds up
# the elements from all of the nested lists. For example:
# >>> t = [[1, 2], [3], [4, 5, 6]]
# >>> nested_sum(t)
# 21


def nested_sum(t):
    total = 0
    for i in t:
        total += sum(i)
    return total


t = [[1, 2], [3], [4, 5, 6]]
print(nested_sum(t))

# Exercise 10.2. Write a function called cumsum that takes a list of numbers and returns the cumulative sum; that is, a new list where the ith element is the sum of the first i + 1 elements from the
# original list. For example:
# >>> t = [1, 2, 3]
# >>> cumsum(t)
# [1, 3, 6]


def cumsum(t):
    t_sum = []

    for i in range(len(t)):
        t_sum.append(sum(t[:i+1]))

    return t_sum


t = [1, 2, 3]
print(cumsum(t))


# Exercise 10.3. Write a function called middle that takes a list and returns a new list that contains
# all but the first and last elements. For example:
# >>> t = [1, 2, 3, 4]
# >>> middle(t)
# [2, 3]

def middle(t):
    return t[1:-1]


t = [1, 2, 3, 4]
print(middle(t))

eng2sp = {'one': 'uno', 'two': 'dos', 'three': 'tres'}
'one' in eng2sp
vals = eng2sp.values()
'dos' in vals
type(vals)


def histogram(s):
    d = dict()
    for c in s:
        if c not in d:  # search for c in the keys of the dictionary
            d[c] = 1
        else:
            d[c] += 1
    return d


print(histogram('I will alaways love you'))


def histogram2(s):
    d = dict()
    for c in s:
        d[c.upper()] = d.get(c.upper(), 0) + 1
    return d


print(histogram2('I will alaways love you'))


def print_hist(h):
    for key in sorted(h):
        print(key, h[key])


h = histogram2("Liverpool will win the EPL")
print_hist(h)


def reverse_lookup(h, v):
    for key in h:
        if h[key] == v:
            return key
    raise LookupError('No key found for value')


eng2num = {'one': '1', 'two': '2', 'three': '3'}

reverse_lookup(eng2num, '1')
#reverse_lookup(eng2num, '4')


def invert_dict(d):
    inverse = dict()
    for key in d:
        val = d[key]
        if val not in inverse:
            inverse[val] = [key]
        else:
            inverse[val].append(key)
    return inverse


h = histogram2("Liverpool will win the EPL")

print(invert_dict(h))

been_called = False


def example2():
    global been_called
    been_called = True
    print(been_called)
    been_called = False
    print(been_called)


example2()
print(been_called)

known = {0: 0, 1: 1}


def fibonacci(n):
    if n in known:
        return known[n]
    res = fibonacci(n-1) + fibonacci(n-2)
    known[n] = res
    return res


print(fibonacci(6))

# Exercise 11.2. Read the documentation of the dictionary method setdefault and use it to write a
# more concise version of invert_dict. Solution: http: // thinkpython2. com/ code/ invert_
# dict. py .


def invert_dict2(d):
    inverse = dict()
    for key in d:
        inverse.setdefault(d[key], []).append(key)
    return inverse


h = histogram2("Liverpool will win the EPL")
print(invert_dict2(h))
