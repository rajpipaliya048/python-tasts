# operations list
def menu():
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Power")
    print("6. Remainder")
    print("7. Bitwise Left Shift")
    print("8. Bitwise Right Shift")
    print("9. Bitwise AND")
    print("10. Bitwise OR")
    print("11. Bitwise XOR")
    print("12. Bitwise NOT")
    print("13. Less than")
    print("14. Less than or equal to")
    print("15. Equal to")
    print("16. Not equal to")
    print("17. Greater than")
    print("18. Greater than or equal to")

# calculator class and all operation's functions
class calculator:
    def __init__(self, value1, value2):
        self.value1 = value1
        self.value2 = value2
        
    def addition(self):
        print(self.value1 + self.value2)
        
    def substraction(self):
        print(self.value1 - self.value2)
        
    def multiplication(self):
        print(self.value1 * self.value2)
        
    def division(self):
        if self.value2 != 0:
            print(self.value1 / self.value2)
        else:
            print("division by zero is not allowed")
            
    def power(self):
        print(self.value1 ** self.value2)
        
    def remainder(self):
        if self.value2 != 0:
            print(self.value1 % self.value2)
        else:
            print("division by zero is not allowed")
            
    def bitwise_left_shift(self):
        print(self.value1 << self.value2)
        
    def bitwise_right_shift(self):
        print(self.value1 >> self.value2)
        
    def bitwise_and(self):
        print(self.value1 & self.value2)
        
    def bitwise_or(self):
        print(self.value1 | self.value2)
        
    def bitwise_xor(self):
        print(self.value1 ^ self.value2)
        
    def bitwise_not(self):
        print(~self.value1)
        
    def less_than(self):
        print(self.value1 < self.value2)
        
    def less_than_or_equal_to(self):
        print(self.value1 <= self.value2)
        
    def equal_to(self):
        print(self.value1 == self.value2)
        
    def not_equal_to(self):
        print(self.value1 != self.value2)
        
    def greater_than(self):
        print(self.value1 > self.value2)

    def greater_than_or_equal_to(self):
        print(self.value1 >= self.value2)

# user input values
num1 = int(input("please insert a number: "))
num2 = int(input("please insert a number: "))

menu()

operation = input("please select an operation: ")
result = calculator(num1, num2)

# calling operation methods
if operation == "1":
    result.addition()
elif operation == "2":
    result.subtraction()
elif operation == "3":
    result.multiplication()
elif operation == "4":
    result.division()
elif operation == "5":
    result.power()
elif operation == "6":
    result.remainder()
elif operation == "7":
    result.bitwise_left_shift()
elif operation == "8":
    result.bitwise_right_shift()
elif operation == "9":
    result.bitwise_and()
elif operation == "10":
    result.bitwise_or()
elif operation == "11":
    result.bitwise_xor()
elif operation == "12":
    result.bitwise_not()
elif operation == "13":
    result.less_than()
elif operation == "14":
    result.less_than_or_equal_to()
elif operation == "15":
    result.equal_to()
elif operation == "16":
    result.not_equal_to()
elif operation == "17":
    result.greater_than()
elif operation == "18":
    result.greater_than_or_equal_to()
