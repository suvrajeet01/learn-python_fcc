from functools import reduce
import argparse
import sys
from enum import Enum
#import mod
#from mod import bark
#from lib import mod
from lib.mod import bark


name = 'langs'
print(type(name))
print(isinstance(name, str))

number = '20'
age = int(number)
print(isinstance(age, int))

age += age



def is_adult(age):
    return True if age > 18 else False



print("""multiple
lines 
in print
aka
multi-line string""")


a=True
b=False
c=any([a,b])
d=all([a,b])



class State(Enum):
    inactive = 0
    active = 1

print(State.active)
print(State.active.value)
print(State.inactive.value)

print(State(1))
print(State['active'])
print(State['active'].value)

print(list(State))
print(len(State))




age = input('Whats ur age? ')



dogs = ['roger','syd',1,'True','quincy',7]
print('roger' in dogs)
print('sid' in dogs)

dogs[2]='kaal'
print(dogs[-1])
print(dogs[2])
print(dogs[2:4])
print(dogs[2:])
print(dogs[:])
print(dogs[:3])
print(len(dogs))
dogs.append('judy')
dogs.extend('judy',5)
dogs += ['judy',5]
dogs.remove('quincy')
print(dogs)
print(dogs.pop())
print(dogs)

items = ['roger',1,'syd',True, 'quincy',7]
items.insert(2, 'test')
print(items)


items[1:1] = ['test','test2']
print(items)




items = ['roger','syd', 'quincy','Syd']
items.sort(items)
print(items)
items = ['roger','syd', 'quincy']
items.sort(items)
print(items)
items = ['roger','syd', 'quincy','Syd']
items.sort(key=str.lower)

itemscopy = items[:]
print(itemscopy)


print(sorted(items), key=str.lower)
print(items)








names = ('roger','syd')
len(names)
names[0:2]
sorted(names)






dict1 = {
    'name':'roger',
    'age':12,
    'color':'green'
}
print(dict1['name'])
dict1['name']='syd'

print(dict1.get('name'))
print(dict1.get('age'))
print(dict1.get('color','brown'))


print(dict1.pop('name'))
print(dict1.popitem())
print('color' in dict1)

print(list(dict1.keys()))
print(list(dict1.values()))

print(list(dict1.items()))

dict1['food']='meat'

del dict1['age']
print(dict1)
dict1Copy=dict1.copy()






set1={'roger','syd','roger'}
set2={'roger'}
intersect = set1 & set2
union = set1 | set2
diff = set1 - set2
superset = set1 >set2
subset = set1 < set2
print(intersect,union,diff,superset,subset)

print(list(set1))








def change(value):
    value['name'] = 'syd'

val = {'name': 'roger'}
change(val)
print(val)



def talk(phrase):
    def say(word):
        print(word)
    words = phrase.split(' ')
    for word in words:
        say(word)

talk('I am goin to buy milk')


def counter():
    count = 0

    def increment():
        nonlocal count
        count = count + 1
        return count #print(count)
        
    return increment #increment()

#count()
increment = counter()

print(increment())
print(increment())
print(increment())









age = 8
print(age.real)
print(age.imag)
print(age.bit_length())


items = [1,2]
items.append(3)
items.pop()
print(id(items))



count = 0
while count < 10:
    print('the condition is true')
    count += 1
print('loop exited')


items = [1,2,3,4,5]
for item in items:
    print(item)

for item in range(50):
    print(item)

for item in enumerate(items):
    print(item)

items = ['roger','syd','quincy']

for index, item in enumerate(items):
    print(index, item)



items = [1,2,3,4,5]
for item in items:
    if item == 2:
        continue
    print(item)



items = [1,2,3,4,5]
for item in items:
    if item == 2:
        break
    print(item)










class Animal:
    def walk(self):
        print('walking.. ')





class c1(Animal):

    def __init__(self,name,age):
        self.name = name
        self.age = age

    def b1(self):
        print('a')

#c2 = c1()
#print(type(c2))

c2 = c1('roger',8)
print(c2.name, c2.age)
c2.b1()
c2.walk()







# mod.bark()
# bark()
# mod.bark()
bark()


print('hello')

print(sys.argvw)
name=sys.argv[1]
print('hello'+names)








parser = argparse.ArgumentParser(description='this program prints name of dogs')
parser.add_argument('-c','--color',metavar='color',required=True,choioces= {'red','yellow'},help='the color to search for')
args = parser.parse_args()
print(ar.color)























lambda num : num + 2
lambda a,b : a*b
multiply = lambda a,b : a*b

print(multiply(2,4))






numbers=[1,2,3]

def double(a):
    return a*2
result = map(double, numbers)
print(result)
print(list(result))


double = lambda a : a*2
result = map(double, numbers)
print(result)
print(list(result))



result = map(lambda a:a*2, numbers)
print(result)
print(list(result))


numbers = [1,2,3,6,4,5]
def is_even:
    return n%2 == 0

result = filter(is_even, numbers)
print(result)
print(list(result))





numbers = [1,2,3,5,4,6]

result = filter(lambda n : n%2 ==0, numbers)
print(result)
print(list(result))


expenses = [
    ('Dinner',80),
    ('car repair', 120)
]

sum = 0
for expense in expenses:
    sum += expense[1]

print(sum)





expenses = [
    ('Dinner',80),
    ('car repair', 120)
]

sum = reduce(lambda a,b: a[1]+b[1], expenses)

print(sum)





