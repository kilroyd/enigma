Coding Enigma - Exercise 7
---

In this exercise we will implement a rotating substitution cipher.

## Copy template class

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

## Usage

How will this be used?

```python
cipher = SubstitutionCipher(init_string)
rot_cipher = RotatingCipher(cipher, 'A')
out = rot_cipher.process('A')
rot_cipher.rotate()
```

## Unit tests

Create a new file `src/test_rotating_cipher.py` and setup some tests.

## Implementation

Implement the class as described on the slides.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_rotating_cipher.py`.

Merge the `exercise08` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise08
```
