# Coding Enigma - Exercise 4

In this exercise we will implement a function that passes all the
characters of a message into a cipher, and returns the resulting
ciphertext. You may already have the code to do this.

## Background

### Refactoring

After coding for a while, you may recognise things about your code
that you want to change.  For example:

* Repeated patterns in your code.
* A better implementation for a function.

Making these changes is called refactoring.

Having unit tests for existing code allows us to refactor without
worrying that we might break something.

### Processing a message

Our `SubstitutionCipher` class operates on a single character at a
time. We mostly want to encode whole messages. So it's likely that you
have a loop somewhere to pass each character of a message into the
`SubstitutionCipher`.

Move this code into a `processMessage()` function, add some tests, and
update any code in `src/enigma.py` to use this function.

## Exercise

### Copy template

Copy the template function from `exercise04/template.py` into
`src/enigma.py`.

```python
def processMessage(cipher, plaintext):
    pass
```

### Usage

How will this be used?

```python
ciphertext = processMessage(cipher, plaintext)
```

### Write the test

Create a new file `src/test_process_message.py`.

At the beginning of the file, add the following line to allow the file
to see your implementation.

```python
from enigma import *
```

### Implement

Create a loop over every character in the message. For each character,
call the cipher's process function, and append the result to the
output string.

### Next

Once the tests are passing, commit `src/enigma.py` and
`src/test_process_message.py`.

```
git add src/enigma.py
git add src/test_process_message.py
git commit
```

Merge the `exercise05` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise05
```
