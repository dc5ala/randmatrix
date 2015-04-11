#!/usr/bin/env python

"""randmatrix.py: Generates a square matrix with random numbers."""

__license__     = "GPL"
__author__      = "Andre Lohan"
__email__       = "31loan1bif@hft-stuttgart.de"

import sys
from random import randint

if (len(sys.argv) < 2):
    sys.stdout.write("Usage: " + sys.argv[0] + " <size>\n")
    sys.stdout.write("For example " + sys.argv[0] + " 8 will create a 8x8 matrix\n")
    sys.exit()
    
# square matrix
size = int(sys.argv[1])
# range for random numbers
lower_bound = -100
upper_bound = 100

sys.stdout.write('# Number of rows\n')
sys.stdout.write(str(size) + '\n')
sys.stdout.write('# Number of columns\n')
sys.stdout.write(str(size) + '\n')

sys.stdout.write('# matrix\n')
for row in range(0, size):
    for col in range(0, size):
        number = randint(-10, 10)
        if (col > 0):
            sys.stdout.write(', ')
        sys.stdout.write(str(number))
    sys.stdout.write('\n')


sys.stdout.write('# solution vector\n')
for row in range(0, size):
    number = randint(-10, 10)
    sys.stdout.write(str(number))
    sys.stdout.write('\n')

