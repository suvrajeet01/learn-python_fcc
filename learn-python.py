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



dogs = ['roger','syd',1,'True']
print('roger' in dogs)
print('sid' in dogs)

dogs[2]='kaal'
print(dogs[2])



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