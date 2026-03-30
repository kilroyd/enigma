Coding Enigma - Exercise 2
---

In this exercise we will create a class to handle substitution
ciphers.

## Python classes

The keyword `class` introduces a class.

```python
class Square:
    def __init__(self, x):
        self.x = x

    def area(self):
        return self.x * self.x

    def circumference(self):
        return 4 * self.x

class Circle:
    def __init__(self, r):
        self.r = r

    def area(self):
        return math.pi * self.r * self.r

    def circumference(self):
        return 2 * math.pi * self.r

s = Square(4)
c = Circle(2)

print("s has area {}".format(s.area()))
print("c has area {}".format(c.area()))
```

A class is composed of data (variables) and functions. The functions
defined under the `class` line are part of the class. The functions
and data that are part of a class are called class members. Functions
may be refered to as member functions.

The first argument of member functions is always `self`, and allows
the function to access class members.

The `__init__()` function is a special function known as a
constructor. It runs when an object of that class type is instantiated
(created). This function should be used to assign initial values to
all member variables. Assigning a value to a class variable all that
you need to do to create that variable.

In the above code, `s = Square(4)`, creates an instance of the Square
class, calling the constructor with the argument 4. The instance is
assigned to the variable `s`. `s.area()` calls the `Square` member
function `area()`. Within that call `self` refers to the object `s`.

## Copy template code

Copy the template `SubstitutionCipher` class from
`exercise02/template.py` into `src/enigma.py`.

## Usage

How will this class be used?

```python
cipher = SubstitutionCipher("ABCDEFGHIJKLMNOPQRSTUVWXYZ")
print(cipher.process('H'))
print(cipher.process('E'))
print(cipher.process('L'))
print(cipher.process('L'))
print(cipher.process('O'))
```

We want to initialise the cipher with a particular mapping that
describes the substitution that we are interested in.

Then we will call the `process()` function once for each character
that we want encoded.

The constructor needs to setup the class data such that the
`process()` call can do the encoding.

## init_string

In the template `SubstitutionCipher.__init__()` we have an
`init_string` argument. This string describes the substitution. The
first letter is the value that 'A' will be encoded as. The second
letter is the value that 'B' will be encoded as. And so on, upto the
26th letter being the letter that 'Z' will be encoded as.

```python
# You can make this easier to see by writing the alphabet above
# the init_string when it is used
#                  ABCDEFGHIJKLMNOPQRSTUVWXYZ      <- in
SubsitutionCipher("ZYXWVUTSRQPONMLKJIHGFEDCBA")  # -> out
```

This notation is chosen because it is a compact way to describe the
substitution.

## Fill in the constructor

The data that you want to store in the class depends on how you plan
on doing the substitution. There are multiple ways you could do this.

In this case, you can store the init_string in the class.

At this point we can try and detect potential problems.

* check that we have a substitution for every letter

* encoding different letters as 'A' would be an error. Why is this?
  Can we detect this and report it?

Use the python `assert` keyword to stop the program on detecting an
invalid condition.

```python
# This says the variable x must hold the value 4
# at this point in the program.
assert x == 4
```

## Fill in the process member function

Make the `process()` member function return the encoded version of the
input character.

## Useful python functions

```python
len(string)   # return the number of characters in string
len(list)     # return the number of objects in a list
ord(char)     # return the ASCII value of a character
chr(ascii)    # return the character associated with an ASCII value
```

## Unit tests

Create a new file `src/test_substitution_cipher.py`. The `test_`
prefix indicates that this file will contain tests.

At the beginning of the file, add the following line

```python
from enigma import SubstitutionCipher
```

This allows the file to see your new class.

We add tests by defining functions with a `test_` prefix. Create a
test function that instantiates a `SubstitutionCipher`, and then assert
that `A` is correctly encoded.

Run `pytest` in the terminal to see if your test passed.

We want unit tests to be as thorough as possible. Add more tests to
check that your class behaves as expected.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_substitution_cipher.py`.

```bash
git add src/enigma.py
git add src/test_substitution_cipher.py
git commit
```

Merge the `exercise03` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise03
```
