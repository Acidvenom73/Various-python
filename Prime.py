import os
clear = lambda: os.system('cls')
clear()

nstart = int(raw_input("What's the start number from where you want to check?: "))
clear()
nstop = int(raw_input("What's the last number from where you want to check?: "))
clear()

for n in xrange(nstart, nstop):
     for x in xrange(2, n):
         if n % x == 0:
             break
     else:
         print n, "is a prime number"

#  http://stackoverflow.com/questions/4114167/checking-if-a-number-is-a-prime-number-in-python
#  http://stackoverflow.com/questions/18833759/python-prime-number-checker