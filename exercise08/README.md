Coding Enigma - Exercise 8
---

In this exercise we will put together the code to handle a complete
Enigma rotor.

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
