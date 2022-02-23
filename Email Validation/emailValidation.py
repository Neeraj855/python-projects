import re
email_condition = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
user_email = input('Eneter your email : ')

if re.search(email_condition,user_email):
    print("Your email is correct")
else:
    print("Wrong Email")