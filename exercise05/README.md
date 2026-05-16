# Coding Enigma - Exercise 5

In this exercise we will implement a helper to output plaintext and
ciphertext in groups of 5 characters.

## Background

### Printing plaintext and ciphertext

```
RHUBARBBARBARABARBARBARIANBEARDS
```

The above is pretty hard to read. It's also hard to keep track of
where you are in the text (if you were decoding by hand).

The standard way to make this easier is to break the text into groups
of 4 or 5 characters for printing.

```
RHUBA RBBAR BARAB ARBAR BARIA NBEAR DS
```

## Exercise

### Copy template code

Copy the template code from `exercise05/template.py` into
`src/enigma.py`.

```python
def quintet(text):
    pass
```

### Usage

How will this be used?

```python
print("Plaintext:  {}".format(quintet(plaintext)))
```

The function should return a modified string.

### Create Tests

Create `src/test_quintet.py` and add a few tests showing how you
expect the function to behave.

## Implementation

Implement the `quintet()` function.

### Useful python

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

### Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_quintet.py`.

Merge the `exercise06` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise06
```
