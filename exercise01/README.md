Coding Enigma - Exercise 1
---

In this exercise we will get familiar with our tools, and write a
simple python function.

## Creating your own branch

A branch in source control is used to keep your changes separate from
everyone elses. A branch can be used for other reasons:

* Control what is about to be released (a release branch)

* To develop a particular feature (a feature branch)

* To pull together changes from multiple branches (an
  integration branch)

Run the following commands, replacing `joe` with your name.

```bash
git branch joe
git checkout joe
```

You will make all your changes on this branch.

## Python identifiers

'Identifiers' are the names we assign to things in Python that we need
to refer to. This includes functions, variables and classes.

The characters in an identifier must come from the characters `A`-`Z`,
`a`-`z`, `0`-`9`, and `_`. A digit (`0`-`9`) cannot be the first
character of an identifier.

It is good practice to follow a naming convention for identifiers, so
that you know what type of thing they represent. Different codebases
use different conventions.

In these exercises we will use:

`camelCase` - functions. No underscores, `_`, first letter lower case,
subsequent words capitalized.

`snake_case` - variables. All lower case. Words separated by
underscores.

`PascalCase` - classes. Camel Case with the first letter capitalised.

`ALL_CAPS` - constants. All upper case. Words separated by
underscores.

## Python indentation

Indentation is important in Python. Indentation groups statements that
belong to the same block of code.

Be careful with tabs - they are usually setup to look the same as 4
spaces. If you encounter issues, try to configure your IDE (or text
editor) to avoid using tabs (make it insert spaces instead).

## Copy function prototype

Copy the template `prepare()` function that is in
`exercise01/template.py` into `src/enigma.py`.

## Fill in the prepare function

The prepare function takes a string as input. We want to return a
similar string that only contains characters that the Enigma machine
can handle. These are the uppercase letters 'A' to 'Z'.

## Useful Python functions

Pythons [string manipulation
functions](https://docs.python.org/3/library/stdtypes.html#string-methods)
are useful here. These functions operate on string objects.

The `text` argument of the `prepare` function is expected to be a
string, so would call the `upper()` function like:

```python
new_text = text.upper()
```

`new_text` will be a variable that is also a string.

The functions that are useful for implementing `prepare()` are
`upper()` and `replace()`.

## Git commit messages

A commit message is used to describe what changes you are making. This
is useful for anyone who wants to double check your code. It is also
useful if you find a bug in six months and need to remember what you
were trying to do.

[Commit message advice](https://www.datacamp.com/tutorial/git-commit-message)

## Next

Merge the `exercise02` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise02
```
