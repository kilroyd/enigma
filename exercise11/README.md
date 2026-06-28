# Coding Enigma - Exercise 11

In this exercise we will create factory functions for rotors and
reflectors.

## Background

### Factories

Factories are used to simplify the creation of some classes. We will
use them to encapsulate the configuration of the Enigma components.

We want to be able to create named rotors that match those available
for the Enigma M3.

## Exercise

### Copy template code

Copy the template code from `exercise11/template.py` into
`src/enigma.py`.

This includes skeleton code for the functions `EntryRotorFactory`,
`RotorFactory`, and `ReflectorFactory`.

### Usage

How will these be used?

```python
ekw = EntryRotorFactory("ABC")
r1 = RotorFactory("IV", 'A')
ukw = ReflectorFactory("B", 'A')
```

### Components

The components that we need to create, and their configuration are
listed below. The classes that we need to use, `EntryRotor`, `Rotor`
and `Reflector` were implemented in exercise08, exerise09, and
exercise10.

| Type        | Name    | Wiring                      | Turnover |
| ----------- | ------- | --------------------------- | -------- |
| EntryRotor  | ABC     | ABCDEFGHIJKLMNOPQRSTUVWXYZ  | - |
| EntryRotor  | QWERTZ  | QWERTZUIOASDFGHJKPYXCVBNML  | - |
| Rotor       | I       | EKMFLGDQVZNTOWYHXUSPAIBRCJ  | Q |
| Rotor       | II      | AJDKSIRUXBLHWTMCQGZNPYFVOE  | E |
| Rotor       | III     | BDFHJLCPRTXVZNYEIWGAKMUSQO  | V |
| Rotor       | IV      | ESOVPZJAYQUIRHXLNFTGKDCMWB  | J |
| Rotor       | V       | VZBRGITYUPSDNHLXAWMJQOFECK  | Z |
| Rotor       | VI      | JPGVOUMFYQBENHZRDKASXLICTW  | Z, M |
| Rotor       | VII     | NZJHGRCXMYSWBOUFAIVLPEKQDT  | Z, M |
| Rotor       | VIII    | FKQHTLXOCBJSPDZRAMEWNIUYGV  | Z, M |
| Reflector   | B       | YRUHQSLDPXNGOKMIEBFZCWVJAT  | - |	 	 
| Reflector   | C       | FVPJIAOYEDRZXWGCTKUQSBNMHL  | - |

Also see [M3 on CryptoMuseum](https://www.cryptomuseum.com/crypto/enigma/m3/index.htm)

Add tests to `src/test_factories.py` that verify that you can create each
of the named components, and they return the correct class.

### Next

Once the tests are passing, commit `src/enigma.py` and `src/test_factories.py`.

Merge the `exercise12` branch into your branch to pick up the next
exercise.

```bash
git merge origin/exercise12
```
