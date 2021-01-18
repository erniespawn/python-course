# python-course


# Conversion 

https://www.youtube.com/watch?v=hCzcJdzW6Vk
### list to tuple & tuple to list

```
l = ["hello", "2", "draw"]

l_tuple = tuple(l)
print l_tuple

tuple_2_list = list(l_tuple)
print tuple_2_list

ernie@ernie-Server-2016:class$ python test.py 
('hello', '2', 'draw')
['hello', '2', 'draw']

```




### dict to list & list to dict 

```
d = {'a' : 1, 'b' : 2, 'c' : 3 }

print d.keys()  # dictionary keys 

print list(d.keys())  # dictionary keys same as above

print list(d.values())  # dictionary values


# Convert 2 list into dictionary
d_list = list(d.keys())
d_values = list(d.values())

print d_list, d_values

d_dict2list = dict(
    zip(
        d_list, d_values
    )
)

print d_dict2list

ernie@ernie-Server-2016:class$ python test.py 
['a', 'c', 'b']
['a', 'c', 'b']
[1, 3, 2]
['a', 'c', 'b'] [1, 3, 2]
{'a': 1, 'c': 3, 'b': 2}

```






### Dicts => keys

```
>>> d = {'a' : 1, 'b' : 2, 'c' : 3 }
>>> for k in d:
...     print k
... 
a
c
b
```

```
>>> d = {'a' : 1, 'b' : 2, 'c' : 3 }
>>> for k,v in d.iteritems():
...     print k, v 
... 
a 1
c 3
b 2
```
# enumerate 

```
>>> names = ["bart", "ernie", "goofy"]
>>> list(enumerate(names))
[(0, 'bart'), (1, 'ernie'), (2, 'goofy')]
>>> for num, name in enumerate(names):
...     print num, name
... 
0 bart
1 ernie
2 goofy
>>> 
```

# zip() makes pair-wise loops
```
>>> names = ["Eiffel Tower", "Empire State", "Sears Tower"]
>>> heights = [324, 382, 442]
>>> for name, height in zip(names, heights):
...     print "%s: %s meters" % (name, height)
... 
Eiffel Tower: 324 meters
Empire State: 382 meters
Sears Tower: 442 meters
>>> 
```
