Coding Enigma - Exercise 3
---

In this exercise we will create a function that inverts a
`SubstitutionCipher`.

## Copy template code

Copy the template function `createInvertedCipher` from
`exercise03/template.py` into `src/enigma.py`.

## Usage

How will this be used?

```python
cipher2 = createInvertedCipher(cipher1)
cipher2.process('A')
```

## Unit tests

Create a new file `src/test_inverted_cipher.py`.

Add the following lines to allow the test to see your implementation,
and to start the first test.

```python
from enigma import *

def test_inverted():
    pass
```

Implement functions to test `createInvertedCipher`. Since you haven't
implemented it yet, these will mostly fail.

To start with, write a test that:
* creates a `SubstitutionCipher`
* calls `createInvertedCipher` with the result
* encodes some characters with the first cipher
* decodes some characters with the second cipher
* checks that you get the original text

## Fill in the function

Have a think about how you will implement the function.

How do you do it by hand? Write down the steps in English. Then try to
translate that to python.

* Do you need to use a loop?

* Do you need a variable like a list?

Try to implement the function.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_inverted.py`.

```
git add src/enigma.py
git add src/test_inverted.py
git commit
```

Merge the `exercise04` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise04
```
