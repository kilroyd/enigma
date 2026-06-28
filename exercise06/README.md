# Coding Enigma - Exercise 6

In this exercise we will implement a function to help us rotate the alphabet.

## Background

### Rotor

The rotors are cylinders. As keys are pressed the rotors turn.

On the outside of each rotor, the alphabet is printed in
sequence. When placed in the machine, a single letter for each rotor
is visible through a window. This defines the position of the rotor.

Since the rotor is a cylinder, once we reach the letter 'Z' the next
letter will be 'A'.

```
             <--
           Z  A   
      X Y        B C
    W                 D
    V                 E
  U                     F
  T                     G
  S                     H
    R                 I
    Q                 J
      P O        L K
           N  M
          -->
```

## Exercise

Write a function to return the letter we will be on after rotating N
positions.

### Copy template

Copy the template function from `exercise06/template.py` into
`src/enigma.py`.

```
def alpha_rotate(char, positions):
    return char
```

### Usage

How will this be used?

```python
c1 = alpha_rotate('A', 1)   # B
c2 = alpha_rotate('A', 5)   # F
c3 = alpha_rotate('A', -1)  # Z
c4 = alpha_rotate('Z', 1)   # A
c5 = alpha_rotate('Z', 5)   # E
c6 = alpha_rotate('Z', -1)  # Y
```

The function should return a character.

### Unit tests

Create a new file `src/test_alpha_rotate.py` and setup some tests.

### Implementation

Implement the function. You should only need some addition,
subtraction, and the use of `ord` and `chr`.

### Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_rotate.py`.

Merge the `exercise07` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise07
```
