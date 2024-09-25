#%%
###### Lists
values = [1, 2, 3, 4]
items = []
for i in range(10):
    items.append(i)
print(items)
#%%
###### Dictionaries

#<key, Value>

###### Sets

a = {1, 2, 3}
b = {4, 5, 6, 3}

###### List Comprehension

values = []
for i in range(10):
    values.append(i)
print(values)

values = [ i for i in range(10) ]
print(values)

###### Lambda functions

def add_two(x):
    return x + 2

print(add_two(10))

print((lambda x: x + 2)(10))

###### Map() finction