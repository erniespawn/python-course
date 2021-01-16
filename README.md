# python-course

```
…or create a new repository on the command line

echo "# python-course" >> README.md
git init
git add README.md
git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/erniespawn/python-course.git
git push -u origin main
                

…or push an existing repository from the command line

git remote add origin https://github.com/erniespawn/python-course.git
git branch -M main
git push -u origin main
```

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


