def is_prime(x):
    if x < 2:
        print "Invalid number, please enter a number over 1."
    for n in range(2, x - 1):
        if x % n == 0:
            return False
    else:
        return True
        
def is_prime_r(z):
    z = int(raw_input("Please enter a number: "))
    if is_prime(z) == True:
        return True
    else:
        return False


#x = 0
#if x == 0:
#    print "x = 0"
#else:
#    print "x != 0"
        


        
#is_prime(5)
# For each number (n) from 2 to (x - 1):
# Check if x divides evenly by n
# If yes, return False
# If no, return True
# x % n == 0
# Define n? In a for loop?: for n in x ?
# Convert x to list with all numbers before x as the content?
# n = 2, 3, 4, 5,  up to (x - 1)
# range (2, x - 1) ?
# 0 and 1 fails..