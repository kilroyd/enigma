# Overview

This repository contains a series of exercises intended to introduce
early learners to simple software engineering. The exercises will
build into a functional
[enigma](https://en.wikipedia.org/wiki/Enigma_machine) machine.

# Requirements

* Command line access
* Python and git installed
* pytest module available
* No internet required (except to download the repository)

# Assumed knowledge

* Previous programming experience
* Some basic python

# Course plan

The `main` branch contains the initial state that learners should
begin with. With each exercise, the student is asked to implement some
code based on a simple specification. The instructions will be in an
`exerciseXX` directory. The student should save and commit their code in
the `src` directory. There will be some verification involved
during each lesson.

When progressing to the next lesson, the learner should merge from the
relevant `exerciseXX` branch, and follow the exercise
instructions. These merges will not modify the `src` directory.

# First step

* Open a terminal. On windows this will be "Command Prompt" or
  "Powershell". On Linux and macOS this will be a program called
  "Terminal".

* Clone this repository with git by typing the following:

```bash
git clone https://github.com/kilroyd/enigma
```

* Change to the new directory created by git

```bash
cd enigma
```

* Open `intro/index.html` in a browser for an introductory
  presentation about what we will be doing.

* Open `intro/README.md` for a guide to get familiar with the tools we
  will be using.

* Each exercise in an `exerciseXX` directory contains:

  * a presentation in `index.html` introducing the background and
    outline of the exercise. This can be used when a group of students
    are doing the exercise together.

  * a `README.md` going into more detail. It should be possible for
    students working on their own to just refer to these files.

  * a `main.py` file demonstrating how the code the exercise is
    intended to produce will be called. This can be used as a basic
    test by running `exerciseXX/main.py` from a terminal.

  * a `template.py` file containing a skeleton function or class that
    is intended to be copied to `src/enigma.py`. It contains some
    documentation about what needs to be implemented. It effectively
    defines the interface that the student must adhere to in their
    implementation.

# References

[Enigma on Wikipedia](https://en.wikipedia.org/wiki/Enigma_machine)

[Enigma at Crypto Museum](https://www.cryptomuseum.com/crypto/enigma/index.htm)
