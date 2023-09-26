conditions = [
    ("Username should have at least one '.'", lambda username: '.' in username),
    ("Username should have at least one '_'", lambda username: '_' in username),
    ("Username should be at least 8 characters long", lambda username: len(username) >= 8),
    ("Password should have at least one of '@', '#', '$', '%'", lambda password: any(char in password for char in ['@', '#', '$', '%'])),
    ("Password should have at least one uppercase letter", lambda password: any(char.isupper() for char in password)),
    ("Password should have at least one lowercase letter", lambda password: any(char.islower() for char in password)),
    ("Password should have at least one digit from 0-9", lambda password: any(char.isdigit() for char in password)),
]

username = input("Enter a username: ")
username_errors = [condition for condition, check in conditions[:3] if not check(username)]
 
for error in username_errors:
    print(error)
    username = input("Enter a username: ")
    if len(username_errors) == '0':
        break
    
password = input("Enter a password: ")
password_errors = [condition for condition, check in conditions[3:] if not check(password)]

for error in password_errors:
    print(error)
    password = input("Enter a password: ")
    if len(password_errors) == '0':
        break
print()
print("Username is: %s" %username)
print("Password is: %s" %password)