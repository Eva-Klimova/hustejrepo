"""
program.py
vypíše náhodné číslo od 1 do 100
"""

import random
import sys

interval = int(sys.argv[1])

cislo = random.randint(0,interval)
print(cislo)

