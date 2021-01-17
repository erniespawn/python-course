# python-course


# Dicts => keys

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
