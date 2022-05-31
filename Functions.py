'''# some more functions
def is_prime(n):
    if n in [2, 3]:
        return True
    if n % 2 == 0:
        return False
    # print()
    r = 3
    while r * r <= n:
        if n % r == 0:
            return False
        r += 2
    # print("\n")
    return True


print(is_prime(78), is_prime(79))'''

# Arguments of a Function

'''def vowel_count(s):
	"""Counts the number of vowels in s and returns the same
	Ignores case of letters"""
	VOWELS = "aeiouAEIOU"
	vc = 0
	for ch in s:
		if ch in VOWELS:
			vc += 1
	return vc
print(vowel_count("GFG is the best platform to learn from."))'''

'''# Types of Arguments


# Python program to demonstrate
# default arguments


def myFun(x, y=50):
	print("x: ", x)
	print("y: ", y)


# Driver code (We call myFun() with only
# argument)
myFun(10)'''

# Variable length non-keywords argument

'''# Python program to illustrate
# *args for variable number of arguments


def myFun(*argv):
	for arg in argv:
		print(arg)


myFun('Hello', 'Welcome', 'to', 'GeeksforGeeks')'''


# Variable length keyword arguments

# Python program to illustrate
# *kwargs for variable number of keyword arguments


def myFun(**kwargs):
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
