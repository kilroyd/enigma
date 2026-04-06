Coding Enigma - Exercise 6
---

In this exercise we will implement a function to help us rotate the alphabet.

## Copy template

Copy the template function from `exercise06/template.py` into
`src/enigma.py`.

```
def rotate(char, positions):
    return char
```

## Usage

How will this be used?

```python
c1 = rotate('A', 1)   # B
c2 = rotate('A', 5)   # F
c3 = rotate('A', -1)  # Z
c4 = rotate('Z', 1)   # A
c5 = rotate('Z', 5)   # E
c6 = rotate('Z', -1)  # Y
```

## Unit tests

Create a new file `src/test_rotate.py` and setup some tests.

## Implementation

Implement the function. You should only need some addition,
subtraction, and the use of `ord` and `chr`.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_rotate.py`.

Merge the `exercise07` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise07
```
