'''#tuple  repetation
weeks=("mon","tue","wed","tue")
print(weeks.count("tue"))
print(weeks.index("wed"))
print(weeks[0])'''
'''
#list
list=[10,80,30,40]
list.sort()
print(list)

print(list[0])
print(list[0],[3])

list.append(1)
print(list)

list.extend([2,3,4])
print(list)

list.reverse()
print(list)

list.remove(80)
print(list)

list.pop(1)
print(list)

list1=[1.1,5.5,3.2,8.9]
newlist=list+list1
print(newlist)

print(list.index(10))

li=[2,3,4,5]
for i in range(6):
    print(li[i])
'''
#sets
'''num=[1,2,3,4,5,6,7,8,9]
even=[]
odd=[]
for i in num:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print(even)
print(odd)
'''

'''#dictionary=collection of keys values
dict={"mon":1,"tue":2,"wed":3,"thur":4}
print(dict)

print(dict["tue"])

#copy
dict1=dict.copy()
print(dict1)

print(dict1.clear())
print(dict.items())

keys=dict.keys()
print(keys)

val=dict.values()
print(val)
'''

#sets-unorders collection elemts

set1={"mon","tue","wed","mon"}
set2={" frid","sat"}
weeks=set1.union(set2)
print(weeks)

set1=set()
set2=set()

for i in range(4):
    set1.add(i)

for i in range(3,9):
    set2.add(i)

set3=set1.difference(set2)
print(set3)

print(set3.clear())
