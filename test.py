#import random

list = [1, 4, 1, 2, 1, 5]

# Random list
'''
x = 0
while x <= 5:
    list.append(random.randrange(1, 7))
    x = x +1
'''
if all(x == list[0] for x in list):
    print("five of a kind")


poker_values = [list.count(number) for number in set(list)]

print(poker_values)

print(set(list))