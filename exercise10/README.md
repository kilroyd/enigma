# Coding Enigma - Exercise 10

In this exercise we will put together the code to handle an
Enigma reflector.

## Background

### Reflector

The reflector is at the end of the stack of rotors, and feeds the
signal coming out of the last rotor back into the rotor on another
pin.

This clever setup is what allows the Enigma machine to act as both the
encoder and decoder when the machines are setup the same. It also
causes a weakness in the encryption - a letter can never be encoded as
itself.

We will also make the `Reflector` class very similar to the `Rotor`
class.

## Exercise

### Copy template code

Copy the template class `Reflector` from `exercise10/template.py` into
`src/enigma.py`.

### Usage

How will this be used?

```python
R = Reflector("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'A')
m = R.encCipher().process('B')
R.rotate()
```

### Testing

Create a new file `src/test_reflector.py` and add tests to check:

* `encCipher()` returns an instance of `RotatingCipher`.
* `invCipher()` returns `None`.
* `rotate()` does _not_ call the cipher's `rotate()`

### Implementation

Complete the `Reflector` class.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_reflector.py`.

Merge the `exercise10` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise10
```
