# Coding Enigma - Exercise 8

In this exercise we will put together the code to handle a complete
Enigma rotor.

## Background

### Rotor Notches

On an Enigma, the first rotor on the right turns with every keypress.

Each rotor has one or more notches in it. These cause the rotor _and_
the one on its left to rotate one position when the notch is
appropriately aligned. Earlier rotors have a single notch. Later
rotors have two notches.

With 3 single notch rotors, the middle rotor will rotate once every 26
keypresses. The left most rotor will only rotate after 26*26
keypresses (676).

We now have all the information to put together for a `Rotor` class.

### Assembling the Rotor

The constructor needs to take 3 arguments describing the setup of the rotor:

* The wiring layout (the substitution's `init_string`)
* A list of turnover positions (positions the notch engages)
* The initial rotor position

It should create two rotating ciphers, and store the current position
and turnover positions.

We want two member functions, `encCipher()` and `invCipher()` to
return the relevant ciphers. The caller will call `process()` on these
ciphers to do the encoding.

We want a `rotate()` member function. This must call `rotate()` on
each cipher, and also update the stored position.

Finally we want a `notch()` member function to report if the current
position is a turnover postition. This should return `True` or
`False`.

## Exercise

## Copy template code

Copy the template class `Rotor` from `exercise08/template.py` into
`src/enigma.py`.

## Usage

How will this be used?

```python
R1 = Rotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ", ['Q'], 'A')
m = R1.encCipher().process('B')
n = R1.invCipher().process('C')
R1.rotate()
notch = R1.notch()
```

## Testing

This class will use the helpers we have written. It is tricky to fully
test this class on its own. We can rely on the existing tests of the
helpers.

Add tests in `test_rotor.py` to check:
* `encCipher()` returns a class that is an instance of a `RotatingCipher`.
* `invCipher()` returns a class that is an instance of a `RotatingCipher`.
* `rotate()` calls both cipher's `rotate()` member functions.
* `notch()` returns `True` after the expected number of calls to `rotate()`.

The `instanceof()` python function should be used to check the class type.

## Implementation

Create a new file `src/test_rotor.py`. Add some simple tests, and then
complete the `Rotor` class as described.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_rotor.py`.

Merge the `exercise09` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise09
```
