#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import RotorFactory, ReflectorFactory, EntryRotorFactory

components = []
components.append(EntryRotorFactory("ABC"))
components.append(EntryRotorFactory("QWERTY"))
components.append(RotorFactory("I", 'A'))
components.append(RotorFactory("II", 'A'))
components.append(RotorFactory("III", 'A'))
components.append(RotorFactory("IV", 'A'))
components.append(RotorFactory("V", 'A'))
components.append(RotorFactory("VI", 'A'))
components.append(RotorFactory("VII", 'A'))
components.append(RotorFactory("VIII", 'A'))
components.append(ReflectorFactory("B", 'A'))
components.append(ReflectorFactory("C", 'A'))
