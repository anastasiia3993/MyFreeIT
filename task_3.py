# Task 3.1
print('Hello world')
# Task 3.2
print('Enter your name:')
user = str(input())
print('Hello,' + user + '!')
# Task 3.3
a = "Hi, I am string variable"
b = 100
print(a,b)
# Task 3.4
import math
print ("The factorial of 100 is : ", math.factorial(100))
# Task 3.5
c = range(0,101)
tup = tuple(c)
print("This is my tuple:")
print(tup[0:101:2])
# Task 3.6
lst = list(tup)
d = [i*i for i in lst]
print("This is my list:")
print(d)
# Task 3.7
e = "sounds/lofi/chilstep.wav"
print("This is my modified string:")
print(e.replace("sounds", "midi"))
print("This is file extension:")
print(e[20:24])
# Task 3.8
f = [1, 1, 2, 3, 5, 8, 10, 10]
g = set(f)
print("This is my list with unique elements:")
print(g)
# Task 3.9
h = [i+1 for i in f]
print("This is my modified list:")
print(h)
# Task 3.10
i = "Python is the most popular programming language"
print("Amount of 'p' in string 'Python is the most popular programming language':")
print(i.count('p'))
# Task 3.11
j = [0, 2, 3, 4]
k = [2, 2, 5]
l = set(j) - set(k)
m = list(l)
print("This is the difference between two lists:")
print(m)
