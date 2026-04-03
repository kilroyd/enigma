Coding Enigma - Exercise 5
---

In this exercise we will implement a helper to output plaintext and
ciphertext in groups of 5 characters.

## Copy template code

Copy the template code from `exercise05/template.py` into
`src/enigma.py`.

```python
def quintet(text):
    pass
```

## Usage

How will this be used?

```python
print("Plaintext:  {}".format(quintet(plaintext)))
```

## Create Tests

Create `src/test_quintet.py` and add a few tests defining how you
expect the function to behave.

## Implementation

Implement the `quintet()` function.

## Useful python

Use slices to refer to consecutive elements in a list or string.

```python
string = "The quick brown fox jumps"
begin = string[:3]     # The first 3 characters (0-2)
mid = string[5:8]      # Characters 5 to 7
end = string[20:]      # Character 20 until the end
```

Concatenate two strings with `+` or `join()`

```
str1 = "First"
str2 = "Second"
str3 = str1 + " " + str2
str4 = " ".join([str1, str2])
```

## Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_quintet.py`.

Merge the `exercise06` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise06
```
