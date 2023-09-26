import re

# username check
username = ""
while True:
    username = input("please enter username: ")
    if len(username) < 9:
        print("username is too short")
        continue
    if  username.find(".") == -1:
        print("username should have atleast one '.'")
        continue
    if username.find("_") == -1:
        print("username should have atleast one '_'")
        continue
    if (len(username) > 8 and username.find(".") != -1 and username.find("_") != -1):
        break
    
# password check
password = ""
pwdpattern = r"(?=.*[@#$%])(?=.*[A-Z])(?=.*[a-z])(?=.*\d)"
while True:
    password = input("please enter password: ")
    if re.match(pwdpattern, password):
        break
    else:
        if not re.search(r"[@#$%]", password):
            print("Password should have at least one of '@', '#', '$', or '%'")
            continue
        if not re.search(r"[A-Z]", password):
            print("Password should have at least one uppercase letter")
            continue
        if not re.search(r"[a-z]", password):
            print("Password should have at least one lowercase letter")
            continue
        if not re.search(r"\d", password):
            print("Password should have at least one digit")
            continue

print("\nUsername:", username,"\nPassword:", password )