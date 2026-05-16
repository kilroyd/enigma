# Coding Enigma - Exercise 7

In this exercise we will implement a rotating substitution cipher.

## Background

### Plan for Implementing Rotor

When we implement the rotor, we want to take account of:

* The signal passes through the rotor twice. Once from the entry rotor
  towards the reflector, and another time in the opposite
  direction. The second time, the transformation is the inverse of the
  first.

* The rotor position will change.

The rotor class will record the current position. It will have two
cipher classes, one for the forward direction, and one for the
reverse. We will also have the cipher classes account for the rotor
position changing.

In this exercise we will implement this new cipher class, the
`RotatingCipher`.

## Exercise

### Copy template class

Copy the `RotatingCipher` class from `exercise07/template.py` into
`src/enigma.py`.

```python
class RotatingCipher:
    def __init__(self, cipher, position):
        pass

    def process(self, char):
        pass

    def rotate(self):
        pass
```

### Usage

How will this be used?

```python
cipher = SubstitutionCipher(init_string)
rot_cipher = RotatingCipher(cipher, 'A')
out = rot_cipher.process('A')
rot_cipher.rotate()
```

### Behaviour of __init__

The `RotatingCipher` will be initialized with a `SubstitutionCipher`
and an initial position, indicated by a letter (the rotor position
visible in the window). Both these can be stored in class variables.

### Behaviour of rotate()

The `rotate()` member function should increment the stored position of
the rotor. You can call the `rotate()` function you implemented
previously to calculate the new position.

### Behaviour of process()

```
                   |
Fixed ref          ABCDEFGHIJKLMNOPQRSTUVWXYZ
Rotor ref in   ABCDEFGHIJKLMNOPQRSTUVWXYZABCD
Subst          XXXXXXXXXXXXXXXXXXXXXXXXXXXXXX
Rotor ref out  ABCDEFGHIJKLMNOPQRSTUVWXYZABCD
Fixed ref          ABCDEFGHIJKLMNOPQRSTUVWXYZ
```

The above figure attempts to show what we need to do in the
`process()` member function that will encode in input character. The
first and last lines identify the fixed letter positions on the
machine, with the `|` indicating the position of the window at
`A`. The rotor is in position `E`.

The input to the rotor is in the fixed reference position. To pass it
through the `SubstitutionCipher` we must first account for the rotor's
position. We can do this with the `rotate()` function implemented
earlier.

In the above example, how many positions do we need to rotate by?

The ouput of `SubstitionCipher` is also in the rotor's reference. So
we similarly need to account for the rotor's position and revert to
the fixed reference.

### Unit tests

Create a new file `src/test_rotating_cipher.py` and setup some tests.

### Implementation

Implement the class as described on the slides.

### Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_rotating_cipher.py`.

Merge the `exercise08` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise08
```
