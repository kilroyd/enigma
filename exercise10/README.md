Coding Enigma - Exercise 10
---

In this exercise we will put together the code to handle an
Enigma reflector.

## Copy template code

Copy the template class `Reflector` from `exercise10/template.py` into
`src/enigma.py`.

## Usage

How will this be used?

```python
R = Reflector("EKMFLGDQVZNTOWYHXUSPAIBRCJ", 'A')
m = R.encCipher().process('B')
R.rotate()
```

## Implementation

Create a new file `src/test_reflector.py`. Add some simple tests, and
then complete the `Reflector` class as described.

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_reflector.py`.

Merge the `exercise10` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise10
```
