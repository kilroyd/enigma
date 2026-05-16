# Coding Enigma - Exercise 9

In this exercise we will put together the code to handle an
Enigma entry rotor.

## Background

### Entry Rotor

The entry rotor is where the wiring from the keyboard enters the
series of rotors. On commercial Enigma machines it was setup to do an
extra substitution. On the Enigma M3 this is actually a no-op, but
we'll implement it for completeness.

## Exercise

We will make the `EntryRotor` class very similar to the `Rotor` class,
even though it does not have all the same functionality. Using a
similar structure potentially allows us to write neater code.

### Copy template code

Copy the template class `EntryRotor` from `exercise09/template.py` into
`src/enigma.py`.

### Usage

How will this be used?

```python
R = EntryRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
m = R.encCipher().process('B')
n = R.invCipher().process('C')
R.rotate()
```

### Testing

Create a new file `src/test_entry_rotor.py`. Add tests to check:

* `encCipher()` returns an instance of `SubstitutionCipher`.
* `invCipher()` returns an instance of `SubstitutionCipher`.

### Implementation

Complete the `EntryRotor` class.

For the `EntryRotor` use `SubstitutionCipher`s and leave `rotate()`
empty.

### Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_entry_rotor.py`.

Merge the `exercise10` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise10
```
