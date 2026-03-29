Coding Enigma - Intro
---

## Explore your development environment

* Point your development environment at the `enigma` directory.

* Open the file `src/enigma.py`

* Can you run the file from the IDE?

## Explore using a terminal

Go to the `src` directory and list the files.

```bash
cd enigma\src # Windows
dir           # Windows
cd enigma/src # Unix
ls            # Unix
```

Can you run `enigma.py` in the terminal?

```bash
# These are different ways you can try running it. Not all will work.
python enigma.py
python3 enigma.py
./enigma.py
```

## Make a change

Try and modify the text message that is printed. Run `enigma.py` again.

* Does your IDE indicate that the file is modified?

* Check the status on the command line

```bash
git status
```

## Undo the change

We'll pretend this change was an error. Let's try to undo it.

* Can you see a way in your IDE to undo your changes. It may say
  'Discard changes' or 'Reset'. Try it.

On the command line:

```bash
git reset --hard HEAD
# This says to reset the working directory to match the latest commit
```

## References

[git](https://git-scm.com)

[Python tutorial](https://docs.python.org/3/tutorial/index.html)
