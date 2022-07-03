# Task 3.1
print('Hello world')
# Task 3.2
print('Enter your name:')
user = str(input("What is your name?"))
print(f"Hello, {user}")
# Task 3.3
b = 100
print(f"Hi, I'm a string variable {b}")
# Task 3.4
import math
print ("The factorial of 100 is : ", math.factorial(100))
# Task 3.5
c = range(0,101)
tup = tuple(c)
print(f"This is my tuple:\n {tup[0:101:2]}")
# Task 3.6
lst = list(tup)
d = [i*i for i in lst]
print(f"This is my list:\n {d}")
# Task 3.7
e = "sounds/lofi/chilstep.wav"
print("This is my modified string:")
print(e.replace("sounds", "midi"))
print(f"This is file extension: \n {e[20:]}")
# Task 3.8
f = [1, 1, 2, 3, 5, 8, 10, 10]
g = set(f)
print(f"This is my list with unique elements:\n {g}")
# Task 3.9
h = [i+1 for i in f]
print(f"This is my modified list:\n {h}")
# Task 3.10
i = "Python is the most popular programming language"
print("Amount of 'p' in string 'Python is the most popular programming language':")
print(i.count('p'))
# Task 3.11
j = [0, 2, 3, 4]
k = [2, 2, 5]
l = set(j) - set(k)
m = list(l)
print(f"This is the difference between two lists:\n {m}")
