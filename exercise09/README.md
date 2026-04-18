Coding Enigma - Exercise 9
---

In this exercise we will put together the code to handle an
Enigma entry rotor.

## Copy template code

Copy the template class `EntryRotor` from `exercise09/template.py` into
`src/enigma.py`.

## Usage

How will this be used?

```python
R = EntryRotor("EKMFLGDQVZNTOWYHXUSPAIBRCJ")
m = R.encCipher().process('B')
n = R.invCipher().process('C')
R.rotate()
```

## Implementation

Create a new file `src/test_entry_rotor.py`. Add some simple tests,
and then complete the `EntryRotor` class as described.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_entry_rotor.py`.

Merge the `exercise10` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise10
```
