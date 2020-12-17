import re
password_input= input("Input your password: ")
boolean = True
while boolean:  
    if (len(password_input)<6 or len(password_input)>16):
        break
    elif not re.search("[a-z]",password_input):
        break
    elif not re.search("[0-9]",password_input):
        break
    elif not re.search("[A-Z]",password_input):
        break
    elif not re.search("[$#@]",password_input):
        break
    elif re.search(r"\s",password_input):
        break
    else:
        print("Valid Password")
        boolean=False
        break

if boolean:
    print("Not a Valid Password")