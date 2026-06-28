# Coding Enigma - Exercise 13

In this exercise we will implement a command line interface to encode
and decode Enigma messages.

## Background

### Command Line

We want to be able to call `src/enigma.py` on the command line,
specifying the initial state of the machine, and a message to
encrypt/decrypt.

### Flag arguments

For a flag argument, the meaning of the argument is determined by the
flag.

Short flags are single characters prefixed by `-`. e.g. `-v`

Long flags are short words prefixed by `--`. e.g. `--verbose`

These can set (or clear) boolean options, or take a value from the
next argument.

* `--verify`
* `--no-verify`
* `--name Jack`

### Positional arguments

The meaning of the argument is determined by the position on the
command line. Usually there will only be one or two positional
arguments specifying a filename, or text to operate on.

* `cp a.txt b.txt`

If there are too many positional arguments, it can be difficult to
remember the correct order.

## Exercise

Create a `main()` function and call it from the `if __name__ ==
"__main__"` check.

Use python's
[argparse](https://docs.python.org/3/library/argparse.html) library to
specify how to handle the command line.

Identify the parameters that you need to setup an Enigma M3, and
decide how you specify these on the command line. Include a way to
pass in message text to encode and decode.

Implement the command line parsing, setup the `EnigmaM3` class, and
encode/decode the message. This will use code that you've implemented
in previous exercises. `EnigmaM3` was implemented in exercise12. We
should use `prepare()` from exercise01 to sanitise the input message
and `processMessage()` from exercise04 to encode/decode the whole
message.

Print the output to the console. Use `quintet()` implemented in
exercise05 to format the output.

## Next

Commit `src/enigma.py` and any tests you may have created.

This is the end of the guide. Here are some things that you
might consider doing next:

* Implement the plugboard. How will you specify letter pairs on the
  command line?

* Implement the index ring - the letters on the outer part of the
  rotor can be rotated relative to the wiring.

* Add an [Enigma
  M4](https://www.cryptomuseum.com/crypto/enigma/m4/index.htm)
  decoder. The M4 has an extra rotor which doesn't move on keypresses.

If you manage to implement the above, you should be able to decrypt
the following message sent by Grand Admiral Donitz.

| Setting                        | Value |
| -------                        | ----- |
| Enigma                         | M4    |
| Umkehrwalze (reflector)        | C     |
| Zusatzwalze (Greek wheel)      | Beta  |
| Walzenlage (wheel order)       | 568   |
| Ringstellung (ring setting)    | EPEL  |
| Grundstellung (start position) | NAEM  |
| Steckern (plugs)               | AE BF CM DQ HU JN LX PR SZ VW |
| | |
| Message indicator              | DUHF TETO |
| Spruchschlussel (message key)  | CDSZ (derived from Grundstellung and message indicator) |

```
LANO TCTO UARB BFPM HPHG CZXT DYGA HGUF XGEW KBLK GJWL QXXT
GPJJ AVTO CKZF SLPP QIHZ FXOE BWII EKFZ LCLO AQJU LJOY HSSM
BBGW HZAN VOII PYRB RTDJ QDJJ OQKC XWDN BBTY VXLY TAPG VEAT
XSON PNYN QFUD BBHH VWEP YEYD OHNL XKZD NWRH DUWU JUMW WVII
WZXI VIUQ DRHY MNCY EFUA PNHO TKHK GDNP SAKN UAGH JZSM JBMH
VTRE QEDG XHLZ WIFU SKDQ VELN MIMI THBH DBWV HDFY HJOQ IHOR
TDJD BWXE MEAY XGYQ XOHF DMYU XXNO JAZR SGHP LWML RECW WUTL
RTTV LBHY OORG LGOW UXNX HMHY FAAC QEKT HSJW
```

[Ref](https://www.cryptomuseum.com/crypto/enigma/msg/p1030681.htm)

* Note: the initial position is `NAEM`, but you need to process the
  message indicator (the first two character groups, `DUHF TETO`) to
  get the actual message key (from tables) and reset the rotor
  positions. [Enigma message
  procedure](https://ciphermachinesandcryptology.com/en/enigmaproc.htm)
