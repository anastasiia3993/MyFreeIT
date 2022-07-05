#Task 4.1
a = list(range(0, 11))
b = [i*i for i in a]
c = zip(a, b)
d = dict(c)
print(f"This my dictionary: \n {d}")

#Task 4.2
d1 = {'a': 1}
d2 = {'b': 2}
d2['b'] = 5
d1.update(d2)
print(f"This is my merged dictionary: \n {d1}")

#Task 4.3
d3 = {'key1': 1, 'key2': 2}
d4 = dict([(value, key) for key, value in d3.items()])
d4[1] = 'value1'
d4[2] = 'value2'
print(f"This is my modified dictionary: \n {d4}")

#Task 4.4
import os
print(f"These are my files: \n {os.listdir()}")

#Task 4.5
from datetime import datetime
print(f"Current time: \n {datetime.today().hour}-{datetime.today().minute} {datetime.today().month}-{datetime.today().day}-{datetime.today().year}")

#Task 4.6
import keyboard, time
print("Do you want to see my list?")
x = 0
while x < 11:
    if keyboard.is_pressed('Enter'):
        time.sleep(.1)
        print(x)
        x += 1

#Task 4.7
import re
string = 'LthHJKiHs GisH nKSiDJceFJ KASsolDIUKuJHtDHiSSonAK'
remove_upper = lambda text: re.sub('[A-Z]', '', text)
string2 = remove_upper(string)
print(f"This is my modified string: \n {string2}")

#Task 4.8
colors = ['красный', 'оранжевый', 'желтый', 'зеленый', 'голубой', 'синий', 'фиолетовый']
colors[0] = 'Красный'
print(f"This is my favourite color: \n {colors[0]} - 1 цвет радуги")
time.sleep(5)

#Task 4.9
import time
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







