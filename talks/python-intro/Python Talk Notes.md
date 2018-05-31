Python Talk Notes
=================

Java Differences to point out
-----------------------------

for loop:
    - uses iterator protocol. Don't think of it as regular `for(int i = 0; i < len; i++) {}`
    - introduce `range()`
    - for loop is like `for each` rather than for.
    - introduce `enumerate()`

## Looping over numbers
```python
for i in [0, 1, 2, 3, 4]:
    print(i ** 2)

for i in range(5):
    print(i ** 2)
```

Looping over collections
```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(colors[i])

for color in colors:
    print(color)
```

Loop backwards
```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors) - 1, -1, -1):
    print(colors[i])

for color in reversed(colors):
    print(color)
```

Looping with indicies
```python
colors = ['red', 'green', 'blue', 'yellow']

for i in range(len(colors)):
    print(i, '-->', colors[i])

for i, color in enumerate(colors):
    print(i, '-->', colors[i])
```

Looping over two collections
```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue', 'yellow']

n = min(len(names), len(colors))
for i in range(n):
    print(names[i], '-->', colors[i]])

for name, color in zip(names, colors):
    print(name, '-->', color)
```

Looping in sorted order
```python
colors = ['red', 'green', 'blue', 'yellow']

for color in sorted(colors):
    print(color)

for color in sorted(colors, reverse=True):
    print(color)
```

Custom Sort Order
```python
colors = ['red', 'green', 'blue', 'yellow']

def compare_length(c1, c2):
    if len(c1) < len(c2):
        return -1
    if len(c1) > len(c2):
        return 1
    return 0

print(sorted(colors, cmp=compare_length))

print(sorted(colors, key=len))
```

Loop Until Sentinel
```python
blocks = []

while True:
    block = f.read(32)
    if block == '':
        break
    blocks.append(block)

blocks = []
for block in iter(partial(f.read, 32), ''):
    blocks.append(block)
```

Distinguishing multiple exit points in loops
```python
def find(seq, target):
    found = False

    for i, value in enumerate(seq):
        if value == target:
            found = True
            break

    if not found:
        return -1
    return i


def find(seq, target):
    for i, value in enumerate(seq):
        if value == target:
            break
    else:
        return -1

    return i
```


## Dictionaries
  - Python is dictionaries all the way down!

Loop over dictionary keys
```python
d = {
    'matthew': 'blue',
    'rachel': 'green',
    'raymod': 'red'
}

# iterating over dictionaries yields the keys
for k in d:
    print(k)

# calling dict.keys() provides a set-like view on the keys
for k in d.keys():
    if k.startswith('r'):
        del d[k]
```

Looping over dictionary keys and values
```python

for k in d:
    print(k, '-->', d[k])

for k, v in d.items():
    print(k, '-->', v)
```


Construct a dictionary from pairs
```python
names = ['raymond', 'rachel', 'matthew']
colors = ['red', 'green', 'blue']

d = dict(zip(names, colors))
```

Counting with dictionary
```python
colors = ['red', 'green', 'red', 'blue', 'green', 'red']

d = {}
for color in colors:
    if color not in d:
        d[color] = 0
    d[color] += 1


d = {}
for color in colors:
    d[color] = d.get(color, 0) + 1


from collections import defaultdict

d = defaultdict(int)
for color in colors:
    d[color] += 1
```

Grouping with dictionaries
```python
names = ['raymond', 'rachel', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']

d = {}
for name in names:
    key = len(name)
    if key not in d:
        d[key] = []
    d[key].append(name)
    
d = {}
for name in names:
    key = len(name)
    d.setdefault(key, []).append(name)

from collections import defaultdict

d = defaultdict(list)
for name in names:
    key = len(name)
    d[key].append(name)
```

Dictionary popitem is atomic
```python
d = {
    'matthew': 'blue',
    'rachel': 'green',
    'raymond': 'red'
}

while d:
    key, value = d.popitem()
    print(key, '-->', value)
```

Linking dictionaries
```python

defaults = {'color': 'red', 'user': 'guest'}
command_line_args = {'color': 'blue'}

d = defaults.copy()
d.update(os.environ)
d.update(command_line_args)


# returns a new ChainMap object which successively checks each dict for value
d = ChainMap(defaults, os.environ, command_line_args)
```

## Clarity
  - Use keywords and names over positional args and indicies.
  - Clarify function calls with keywords
  - use namedtuple() to have names on tuple fields.

Unpacking Sequences
```python
p = 'Raymond', 'Hettinger', 0x30, 'python@example.com'

fname = p[0]
lname = p[1]
...

fname, lname, age, email = p
```

Updating multiple state variables
```python

def fibonacci(n):
    x = 0
    y = 1
    for i in range(n):
        print(x)
        t = y
        y = x + y
        x = t

def better_fib(n):
    x, y = 0, 1
    for i in range(n):
        x, y = y, x+y
```

## Efficiency
  - Don't move data around unnecesarily
  - Cache hits are fast, cache misses are slow. Use generators, don't copy data.

## String Concatenation
  - Use Join. Not `+`

## Updating Sequences

```python
names = ['raymond', 'rache', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie']  

# SLOW
del names[0]
names.pop(0)
names.insert(0, 'mark')

# FAST
# Use deque, a list-like sequence optimized for data accesses near its endpoints.
names = deque(['raymond', 'rache', 'matthew', 'roger', 'betty', 'melissa', 'judith', 'charlie'])

del names[0]
names.popleft()
names.appendleft('mark')
```

## Decorators and Context Managers
```python
# Advanced usages

# Cache
def web_lookup(url, saved={}):
    if url in saved:
        return saved[url]
    page = urllib.urlopen(url).read()
    saved[url] = page
    return page

from functools import wraps
def cache(func):
    saved = {}

    @wraps(func)
    def newfunc(*args):
        if args in saved:
            return newfunc(*args)

        result = func(*args)
        saved[args] = result
        return result

@cache
def web_lookup(url):
    return urllib.urlopen(url).read()
```

Factor out temporary context
```python

old_context = getcontext().copy()
getcontext().prec = 50
print(Decimal(355) / Decimal(113))
secontext(old_context)

from decimal import localcontext
with localcontex() as ctx:
    ctx.prec = 42
    s = calculate_something()

s = +s # round the result back to the default precision
```

How to open and close files
```python
f = open('data.txt')
try:
    data = f.read()
finally:
    f.close()

with open('./file.txt', 'r') as r:
    print(r.read())
```

How to use Locks
```python
#Make a lock
lock = threading.Lock()

#old way to use a lock
lock.acquire()
try:
    print('Critical section 1')
finally:
    lock.release()

with lock:
    print('Critical section 1')
```

Factor out temporary contexts
```python
try:
    os.remove('somefile.tmp')
except OSError:
    pass


from contextlib import suppress

with suppress(OSError):
    os.remove('somefile.tmp')
```

Factor out temporary contexts (redirect std out)
```python
with open('help.txt', 'w') as f:
    oldstdout = sys.stdout
    sys.stdout = f

    try:
        help(pow)
    finally:
        sys.stdout = oldstdout

from contextlib import redirect_stdout
with open('help.txt', 'w') as f:
    with redirect_stdout(f):
        help(pow)
```

## Concise Expressive One-Liners

  - Don't put too much on one line
  - Don't break atoms of thought into subatomic particles

These conflict though. Try:
  - One logical line of code equals one sentence in english

List comprehensions and Generator Expressions
```python
result = []
for i in range(10):
    s = i ** 2
    result.append(s)

print(sum(result))


print sum(i ** for i in range(10))
```

---------------------------------

PYTHON TALK:
============

Important things:
  - Zen of Python
  - PEP-8

Format:
    - Why Python?
    - Python language description
        + Syntax
        + Features
    - Python differences with Java
        + Classes
        + Loops
        + Dictionaries
        + Multiple Assignment
        + Decorators
        + Context Managers
    - Mike's Workspace
        + mac python
        + brew python
        + pyenv
        + venv
        + pipenv
        + tools
            * iterm2
            * sublime
            * ipython
            * pudb
            * pytest
            * httpie
    - Packaging
        + libraries
        + applications
