#!/usr/bin/env python3
import os
import sys

# Tweak lookup path to find students code
sys.path.append(os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), 'src'))

from enigma import prepare

plaintext = prepare("After pruning the Rhubarb Barbara Bar Barbarian Beards, the Rhubarb Barbara Bar Barbarian Beard Barber mostly with the Rhubarb Barbara Bar Barbarians went to the Rhubarb Barbara Bar Barbarian Beard Barber Bier Bar to Rhubarb Barbara Bar Barbarian Beard Barber Bier Bar Barbel in order to take her along to the Rhubarb Barbara Bar in order to eat some of Rhubarb Barbaras superb rhubarb pie and clank together a Rhubarb Barbara Bar Barbarian Beard Barber Beer? Cheers!")
print("Plaintext is :{}:".format(plaintext))

assert plaintext == "AFTERPRUNINGTHERHUBARBBARBARABARBARBARIANBEARDSTHERHUBARBBARBARABARBARBARIANBEARDBARBERMOSTLYWITHTHERHUBARBBARBARABARBARBARIANSWENTTOTHERHUBARBBARBARABARBARBARIANBEARDBARBERBIERBARTORHUBARBBARBARABARBARBARIANBEARDBARBERBIERBARBARBELINORDERTOTAKEHERALONGTOTHERHUBARBBARBARABARINORDERTOEATSOMEOFRHUBARBBARBARASSUPERBRHUBARBPIEANDCLANKTOGETHERARHUBARBBARBARABARBARBARIANBEARDBARBERBEERCHEERS", "Does not match expected plaintext"
