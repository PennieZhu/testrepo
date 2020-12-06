def add(a, b):
    print("adding %d + %d" % (a, b))
    return a + b

def subtract(a, b):
    print("subtracting %d - %d" % (a, b))
    return a - b

def multiply(a, b):
    print("multiplying %d　* %d " % (a, b))
    return a*b

def divide(a, b):
    print("dividing %d / %d" % (a, b))
    return a/b

print("Let's do some math with just functions!")
print("how old are you?")
age1 = float(input())
print("How old is your mother?")
age2 = float(input())

difference = subtract(age2, age1)
print("so your mother is %d years older than you.\n" % difference)
