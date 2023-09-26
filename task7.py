import csv
# 1
try:
	a = 10/0
	print (a)
except ArithmeticError:
		print ("This statement is raising an arithmetic exception.")

# 2
try:
	a = [1, 2, 3, 4, 5, 6, 7, 8, 9]
	print (a[11])
except LookupError:
	print ("Index out of bound error.")

# 3
try:
    class Attributes(object):
        pass

    object = Attributes()
    print (object.attribute)
except AttributeError:
    print("Attribute not found")
    
# 4
try:
    import math

    print (math.exp(1000))
except OverflowError:
    print ('OverflowError')
    
# 5
try:
    import module_does_not_exist
except ModuleNotFoundError:
    print('Module does not exist.')
    
# 6
try:
    array = { 'a':1, 'b':2 }
    print (array['c'])
except KeyError:
    print ("Key Error")
    
# 7
try:
    print(x)
except NameError:
    print("name error")

# 8
try:
    Arr = [3, 1, 2]
    i=iter(Arr)
    print (i)
    print (i.next())
    print (i.next())
    print (i.next())
except AttributeError:
    print("AttributeError")

# 9
try:
    with open('user_data.txt') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
except FileNotFoundError:
    print("file not found exception")
    
# 10
try:
    def fact(a):
        factors = []
        for i in range(1, a+1):
            if a%i == 0:
                factors.append(i)
        return factors 
    
    num = 600851475143
    print (fact(num))
except KeyboardInterrupt:
    print ('Caught KeyboardInterrupt')
    
#  user defined exceptions

class Error(Exception):
	pass

class zerodivision(Error):
	pass

try:
	num = int(input("Enter a number: "))
	if num == 0:
		raise zerodivision
except zerodivision:
	print("Input value is zero, try again!")
	print()
