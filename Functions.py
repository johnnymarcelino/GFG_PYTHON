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


"""def myFun(**kwargs):
	'''
	-> FUNCTION to print key arguments and values arguments
	:param kwargs: There is not anyone
	:return: without
	'''
	for key, value in kwargs.items():
		print("%s == %s" % (key, value))


# Driver code
myFun(first='Geeks', mid='for', last='Geeks')
print(myFun.__doc__)"""


# Instrução de retorno de função Python

'''def square_value(num):
	"""This function returns the square
	value of the entered number"""
	return num**2


print(square_value(5))
print(square_value(-9))'''


'''def swap(x, y):
	temp = x
	x = y
	y = temp
	return x, y

# Driver code
x = 2
y = 3
swap(x, y)
# print(x)
# print(y)'''

# def myFun(new, **various):
# 	# print("after argument one: ", various)
# 	print("First argument: ", new)
# 	for key, value in various.items():
# 		print(key, value, end=" ")
#
# myFun("Alright", Suadações = "hello", name = "Johnny", lastname = "Marcelino", cumprimentos = "Welcome Back")


'''def myNewFun(*b, **a):
	# print("arg1:", b[len(b)-1])
	# print("arg2:", b[len(b)-2])
	# print("arg3:", b[len(b)-3])
	# print(len(b))
	# for key, value in a.items():
	# 	print(f"This {value} is the valent!")

n = ("Johnny", "Marcelino", "Name")
myNewFun(*n)
#
# def myFun(**datas):
# 	print(datas)
# 	for key, arg in datas.items():
# 		print(f"This {key} represent -> {arg}")

varioN = {"first_name": "johnny", "Last_Name": "Marcelino", "Age": 26, "Birthday": 1995}
myNewFun(*n, **varioN)'''


# Global Keyword / Palavra-chave global

# This function modifies the global variable
def f():
    global s
    s += " All Languages is greater!"
    print("Inside of function", s)
    s = "Except Python!"
    print(s)


s = "Python is greater!"
f()
print("Outside of function", s)