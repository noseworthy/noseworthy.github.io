A Pythonic Intro to Python
==========================

  - I'm Mike
  - Who here uses python daily?
  - Who has been using python for more than 1 month? 1 year? 5 years?
  - I love python
  - Do you love your language?
  - Hopefully this talk will give you a greater appreciation for python
  - Python is 28 years old! Python 3 is 10 years old!
  - Python culture:
    + A little silly
    + Named after Monty Python
    + Guido is the BDFL
  - Writing idiomatic code is important in any language, in python we call this being "pythonic"
    + Pep8
    + Introduce what a PEP is, and what PEP8 is
    + "Foolish Consistency is the hobgoblin of little minds..."
    + Zen of Python
  - 8 Fold Path of Pythonic Zen
    + Loops
    + Dictionaries
    + Clarity: namedtuples, function args, Unpacking and Multiple Assignment
    + Generators, don't copy data
    + Strings are immutable, how to do concatenation
    + Updating sequences (use deque for left access/update)
    + Decorators and Context Managers
    + Comprehensions help with clarity and organizing thoughts
  - Big Java Example
- Mike's Set-up
  + MacOS python is bad.
    * Usually old and out of date
    * requires system/root level access to install or modify stuff (yikes)
    * Dirts up the system install which might break things
  + Install with brew or pyenv instead
  + Manage virtualenvironments with pyenv-virtualenv or pipenv
  + Sublime text editor with SublimeLinter and SublimeLinter-flake8 installed.
  + Sublime anaconda package (not related to the other anaconda) can turn sublime into a pretty fully featured but lightweight IDE.
- Thanks for listening
- Questions
- References
  + Stop writing classes
  + Raymond Hettinger: Beyond PEP-8, Transforming Code into Beautiful Idiomatic Python
  + Hitchhikers guide to python

<!-- 1. Avoid Classes
      i.   One function and init (really just a function)
      ii.  Don't use getters and setters, use @property
      iii. Don't use weird methods, just the dunders where possible
      iv.  Use an adapter class to wrap bad non-pythonic apis
      v.   Example: Greeting/Hello world
    2. Avoid excessive use of packages (weak)
      i.   "Flat is better than Nested"
      ii.  Why are you separating things into multiple packages?
      iii. Packages are for removing namespace conflicts. Not for creating taxonomies
      iv.  You either remember the module you want to use, or you look it up. Deeply nesting it doesn't help.
    3. Avoid indexes (Sequences)
      i.   Sequences are great, and python3.6 sequences are fast
      ii.  Using indexes makes for hard to read code. 99% of the time
           we just want to iterate over the elements in a sequence and
           don't care about the index.
      iii. If we do care, use `enumerate()`
      iv.  Sequences are (list, tuple, range, set, string)
      v.   Example: Iterate printing stuff from a list.
    4. Comprehensions are your friend
      i.   Comprehensions are clear and concise.
      ii.  Help to express one English sentence per line of code.
      iii. Example: some map/filter thing
    5. Dictionaries all the way down
      i.   At it's core, pretty much everything in python is a dictionary
      ii.  Keys have to be immutable, (string, int, float, tuple, frozenset)
      iii. Example: Use for function lookups like a switch statement 
      iv.  Example: Counting things
    6. Generators are great!
      i.   Generators turn functions into iterators
      ii.  Generators are used to make performant and space conserving code.
      iii. Can start using the results from generators before all results are yielded. Enables lazy loading/evaluation
      iiii. Example: Fibonnacci
    7. Decorators help to modularize utils and keep your code clean
      i.   Decorators allow you to encapsulate useful utilities and use across your code base.
      ii.  Keeps code clean and composable.
      iii. Example: in-memory cache (memoization)
    8. Context managers keep things clean
      i.   If you have frequent set-up and tear-down steps (e.g. IO) use context manager
      ii.  If you have some special context but you need to temporarily modify it, use context managers.
      iii. Example: file handler and suppress. -->
