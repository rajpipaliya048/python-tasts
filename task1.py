x = input("please enter value: ")
if x.isupper():
    print(x, "is in upper case")
elif x.islower():
    print(x, "is in lower case")
else:
    print(x, "is in camel case")
# - for ASCII value
for elements in x:
    if elements.isupper():
        pass
    else:
        print("The ASCII value of '" + elements + "' is", ord(elements))