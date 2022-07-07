import os
import keyboard
import time
import re


#Task 4.1
a = list(range(0, 11))
b = [i*i for i in a]
c = zip(a, b)
d = dict(c)
print(f"This my dictionary: \n {d}")

#Method 2
nums = [num for num in range(11)]
nums2 = [num**2 for num in range(11)]
res = {nums[i]:nums2[i] for i in range(len(nums))}
print(f"This my dictionary 2: \n {res}")

#Task 4.2
d1 = {'a': 1}
d2 = {'b': 2}
d2['b'] = 5
d1.update(d2)
print(f"This is my merged dictionary: \n {d1}")

#Metod 2
dict1 = {'a': 1}
dict2 = {'b': 2}
dict2['b'] = 5
dict3 = {**d1, **d2}
print(f"This is my merged dictionary 2: \n {dict3}")

#Task 4.3
d3 = {'key1': 1, 'key2': 2}
d4 = dict([(value, key) for key, value in d3.items()])
d4[1] = 'value1'
d4[2] = 'value2'
print(f"This is my modified dictionary: \n {d4}")

#Method 2
dict3 = {'key1': 1, 'key2': 2}
dict4 = {value: key for key, value in dict3.items()}
dict4[1] = 'value1'
dict4[2] = 'value2'
print(f"This is my modified dictionary 2: \n {dict4}")

#Task 4.4
print(f"These are my files: \n {os.listdir()}")

#Task 4.5
from datetime import datetime
print(f"Current time: \n {datetime.today().hour}-{datetime.today().minute} {datetime.today().month}-{datetime.today().day}-{datetime.today().year}")

#Task 4.6
print("Do you want to see my list?")
x = 0
while x < 11:
    if keyboard.is_pressed('Enter'):
        time.sleep(.1)
        print(x)
        x += 1

#Task 4.7
string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
remove_upper = lambda text: re.sub('[A-Z]', '', text)
string2 = remove_upper(string)
print(f"This is my modified string: \n {string2}")

#Method 2
string2 = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
lower = ''
for char in string:
    if char.islower():
        lower += char
    elif char == " ":
        lower += " "
print(f"This is my modified string 2: \n {lower}")

#Task 4.8
s = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
new = ""
for x in s:
    new += x
indexes = {0: 'К',
           7: ' - 1 цвет радуги О',
           33: ' - 2 цвет радуги Ж',
           56: ' - 3 цвет радуги З',
           80: ' - 4 цвет радуги Г',
           104: ' - 5 цвет радуги С',
           126: ' - 6 цвет радуги Ф',
           153: ' - 7 цвет радуги'}

for index, replacement in indexes.items():
    new = new[:index] + indexes[index] + new[index + 1:]
print(f"This is my rainbow: \n {new}")
time.sleep(5)

#Task 4.9
end = time.time() + 10
i = 0
print("This is my waterfall of numbers:")
while time.time() < end:
    i += 1
    print(i)

#Task 4.10
n = 9
print("This is my interesting sequence:")
for i in range(1,n+1):
    for j in range(1, i+1):
        print(i, end="")
    print()
