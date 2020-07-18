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

verbose = True


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
# fin = open('words.txt')
# for line in fin:
#     word = line.strip()
#     if len(word) > 20:
#         print(word)

# Exercise 9.2: Print and count numnber of words that have no 'e'


def has_no_e(word):
    if 'e' not in word:
        return True
    return False


# count_no_e = 0
# fin.seek(0)
# for line in fin:
#     word = line.strip()
#     if has_no_e(word) == True:
#         count_no_e = count_no_e + 1
#         print(word)

# print(count_no_e)

# Exercise 9.6: abecedarian


def is_abecedarian(word):
    if len(word) <= 1:
        return True
    if word[0] > word[1]:
        return False
    return is_abecedarian(word[1:])


# fin.seek(0)
# count_abecedarian = 0
# for line in fin:
#     word = line.strip()
#     if is_abecedarian(word):
#         print(word)
#         count_abecedarian += 1
# print(count_abecedarian)

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

# Exercise 10.7. Write a function called has_duplicates that takes a list and returns True if there
# is any element that appears more than once. It should not modify the original list.

def has_duplicates(x):
    unique = []
    count = []

    for index, val in enumerate(x):
        if val not in unique:
            unique.append(val)
            count.append(1)
        else:
            count[unique.index(val)] += 1

    print(unique)
    print(count)
    
    for i in count:
        if i > 1:
            return True
        return False

x = ['a', 'b', 'c', 'a', 'd', 'b', 'f', 'c']
print(has_duplicates(x))

# Exercise 11.4. If you did Exercise 10.7, you already have a function named has_duplicates that
# takes a list as a parameter and returns True if there is any object that appears more than once in the
# list.

# Use a dictionary to write a faster, simpler version of has_duplicates. Solution: http: //
# thinkpython2. com/ code/ has_ duplicates. py

def has_duplicates2(x):
    index = dict()

    for i in x:
        if i not in index:
            index[i] = 1
        else:
            index[i] += 1

    if verbose:
        print(index)

    for j in index:
        if index[j] > 1:
            return True
    return False

x = ['a', 'b', 'c', 'a', 'd', 'b', 'f', 'c']
print(has_duplicates2(x))


# Exercise 8.5 Write a function called rotate_word that takes a string and an integer as parameters, and returns
# a new string that contains the letters from the original string rotated by the given amount.
# You might want to use the built-in function ord, which converts a character to a numeric code, and8.13. Exercises 81
# chr, which converts numeric codes to characters. Letters of the alphabet are encoded in alphabetical
# order, so for example:
# >>> ord('c') - ord('a')
# 2
# Because 'c' is the two-eth letter of the alphabet. But beware: the numeric codes for upper case
# letters are different.

def rotate_word(word, n):
    rotated_word = ''
    a_as_n = ord('a')
    A_as_n = ord('A')

    for c in word:
        rotated_c_as_n = ord(c) + n
        if c.islower() and rotated_c_as_n > a_as_n + 26 or c.isupper() and rotated_c_as_n > A_as_n + 26:
            rotated_c_as_n -= 26
        rotated_c = chr(rotated_c_as_n)
        rotated_word = rotated_word + rotated_c

    if verbose:
        print(rotated_word)

    return rotated_word

print(rotate_word('iBz', 3))

# write a function called sumall that takes any number of arguments and
# returns their sum.

def sumall(*args):
    sum = 0

    if verbose:
        print(args)

    for i in args:
        sum = sum + i

    return sum

print(sumall(1,2,3,4,5))

t = tuple('abcde')
print(t)

t = tuple([1,2,3,4,5])
print(t)

t = tuple(('a', 'b', 'c', 'd', 'e'))
print(t)

t = t + ('f', 'g')
print(t)

a, b = 1, 2

print(a, b)

def has_match(t1, t2):
    for x, y in zip(t1, t2):
        if x == y:
            return True
    return False

print(has_match([1,2,3], [2,2,4]))

def most_frequent(x):
    t = tuple(x)
    l = sorted(t)
    print(l)


most_frequent('abhehehrkwherkcckfkhfkjhfkwhf')

# Exercise 13.1. Write a program that reads a file, breaks each line into words, strips whitespace and
# punctuation from the words, and converts them to lowercase.

def my_split(sentence, delimiters):
    words = []
    word = ''
    for c in sentence:
        if c not in delimiters:
            word = word + c
        elif word != '':
            words.append(word)
            word = ''
    if word != '':
        words.append(word)
    return words

import string

print(string.punctuation)

fin = open("sample2.txt")

for line in fin:
    line = line.strip('\r\n')
    words = line.split(' ')
    for i, word in enumerate(words):
        words[i] = word.strip(string.punctuation).lower()
    print(words)


tweet = {
    "user" : "joelgrus",
    "text" : "Data Science is Awesome",
    "retweet_count" : 100,
    "hashtags" : ["#data", "#science", "#datascience", "#awesome", "#yolo"]
}

tweet_keys = tweet.keys() # list of keys

tweet_values = tweet.values() # list of values

tweet_items = tweet.items() # list of (key, value) tuples

"user" in tweet_keys # True, but uses a slow list in

"user" in tweet # more Pythonic, uses faster dict in

"joelgrus" in tweet_values # True



# Imagine that you’re trying to count the words in a document. An obvious approach is
# to create a dictionary in which the keys are words and the values are counts. As you
# check each word, you can increment its count if it’s already in the dictionary and add
# it to the dictionary if it’s not:

big_string = 'This is a test string to see how word count using dictionaires work in Python. This string contains a lot of words to see how count works'

document = big_string.split()

word_counts = {}

for word in document:
    if word in word_counts:
        word_counts[word] += 1
    else:
        word_counts[word] = 1

# sort the words and counts from highest count to lowest
wc = sorted(word_counts.items(), key=lambda item: item[1], reverse=True)
print(wc)

# You could also use the “forgiveness is better than permission” approach and just han‐
# dle the exception from trying to look up a missing key:

word_counts = {}
for word in document:
    try:
        word_counts[word] += 1
    except KeyError:
        word_counts[word] = 1

# A third approach is to use get, which behaves gracefully for missing keys:7

word_counts = {}
for word in document:
    previous_count = word_counts.get(word, 0)
    word_counts[word] = previous_count + 1

# Every one of these is slightly unwieldy, which is why defaultdict is useful. A
# defaultdict is like a regular dictionary, except that when you try to look up a key it
# doesn’t contain, it first adds a value for it using a zero-argument function you pro‐
# vided when you created it. In order to use defaultdicts, you have to import them
# from collections:


from collections import defaultdict
word_counts = defaultdict(int) # int() produces 0
for word in document:
    word_counts[word] += 1


from collections import Counter

c = Counter(document)
print(c)

# print the 10 most common words and their counts
for word, count in c.most_common(3):
    print(word, count)

# You can write a ternary if-then-else on one line, which we will do occasionally:
x = 5
parity = "even" if x % 2 == 0 else "odd"


# Python has an all function, which takes a list and returns True precisely when every
# element is truthy, and an any function, which returns True when at least one element
# is truthy:
print(all([True, 1, { 3 }])) # True
print(all([True, 1, {}])) # False, {} is falsy
print(any([True, 1, {}])) # True, True is truthy
print(all([])) # True, no falsy elements in the list
print(any([])) # False, no truthy elements in the list


