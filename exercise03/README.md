# Coding Enigma - Exercise 3

In this exercise we will create a function that inverts a
`SubstitutionCipher`.

## Background

### Enigma Rotors

The core of the Enigma are the rotors. These are cylinders with
electrical contacts on the flat faces. Each face has 26 contacts, one
for each letter. Inside the rotor, the electical contacts on one face
are wired to different contacts on the other face. This effectively
produces a substitution.

### Enigma Internals

```
UKW    R3    R2    R1   EKW      PB

+--+  +--+  +--+  +--+  +--+    +--+       Keyb
|  |  |  |  |  |  |  |  |  |    |  |
| +----~~----~~----~~----~~------~~------- 'A' ----  +ve
| |   |  |  |  |  |  |  |  |    |  |                Batt
| |   |  |  |  |  |  |  |  |    |  |
| +----~~----~~----~~----~~------~~------> 'X' ----  -ve
|  |  |  |  |  |  |  |  |  |    |  |
+--+  +--+  +--+  +--+  +--+    +--+       Lamp
```

PB - Plugboard. Swaps 10 selectable pairs of letters, and passes the
others through unchanged.

EKW - Entry rotor. Fixed position.

R1 - First rotor. Swappable. Rotates on every keypress.

R2, R3 - Further rotors. Swappable. Rotates when nudged by a notch on
the previous rotor.

UKW - Reflector. Fixed position. The reflector also has 26 contacts on
its right hand face. These contacts are paired and wired together.

### Inverted Substitution Cipher

After plaintext is encoded by a subsitution cipher, you want to be
able to decode it. We want to be able to do this with the
`SubstitutionCipher` class you have just written.

To do this we need to calculate the `init_string` that undoes the
original substitution, and then use that to instantiate a new
`SubstitutionCipher`.

This happens to model the signal going back through the rotor after
the reflector.

Before trying to code this, try do an example.
```
ABCDEFGHIJKLMNOPQRSTUVWXYZ
EFGHMNOPABCDIJKLUVXWYZQRST

ABCDEFGHIJKLMNOPQRSTUVWXYZ
??????????????????????????
```

## Exercise

### Copy template code

Copy the template function `createInvertedCipher` from
`exercise03/template.py` into `src/enigma.py`.

### Usage

How will this be used?

```python
cipher2 = createInvertedCipher(cipher1)
cipher2.process('A')
```

### Unit tests

Before we implement the function, let's create tests for it. By doing
this first, we can clarify how we expect the function to behave.

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
* decodes the output with the second cipher
* checks that you get the original text

Can you create a test that checks that every possible character will be
decoded correctly?

Add a test with a different initial `init_string`.

### Fill in the function

Have a think about how you will implement the function.

How did you do it by hand? Write down the steps in English. Then try to
translate that to python.

* Do you need to use a loop?

* Do you need a variable like a list?

Try to implement the function, and run `pytest` when you think it should
work. It's likely to fail - is the problem with the implementation or
the test?

### Next

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
