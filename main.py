import os
import datetime
from helperFxn import *

#Default SuperUser Account
data = {
    '01200300040000':{
        'auth':{
            'username':'username',
            'password':'aaaaaa',
            'role':'SUPERUSER',
        },
        'info':{
            'first_name':'SuperUser',
            'last_name':'',
            'phone_no':'',
            'email':'',
            'date_of_birth':'',
            'address':'',
            'date_of_register':'',
            'balance':0,
        }
    }
}

#read and store file content in dict if exixts else create file with default
data_file = "./data.txt"
if os.path.exists(data_file):
    with open(data_file,'r') as my_file:
        data = eval(my_file.read())
        #print(data)
else:
    with open(data_file,'w+') as my_file:
        my_file.write(str(data))

run = True
last_acct_num = list(data.keys())[-1]
next_acct_num = format(int(last_acct_num) + 1,'014d')
print(last_acct_num)
print(next_acct_num)

greet()
while run:
#Choose Role to Login
    print("1. Login as SuperUser")
    print("2. Login as Staff")
    print("3. Login as Customer")
    print("4. Exit")
    login = input("Please Choose an Option:- ")
    login_role = ""

    if login =="1":
        login_role = "SUPERUSER"
    elif login == "2":
        login_role = "STAFF"
    elif login == "3":
        login_role = "CUSTOMER"
    elif login == "4":
        run = False
        continue  #Exits if user enters 4
    else:
        print(f"{login} is not a valid input")

    #Loop For Logging in User
    run_Login_loop = True
    while run_Login_loop:
        #Default Variable Initialize for Login
        is_acct_num_valid = False
        is_password_valid = False
        is_logged_in = False
        account = input("Enter Your Account Number or 0 to go back:- ")
        if account == "0":
            run_Login_loop = False
            continue
        password = input("Enter Your Account Password or 0 to go back:-")
        if password == "0":
            run_Login_loop = False
            continue
        is_acct_num_valid = account in list(data.keys())
        if is_acct_num_valid:
            is_password_valid = password == get_userpassword(data,account)
            is_role_valid = login_role == get_auth_info(data,account).get('role')
        
        if is_acct_num_valid and is_password_valid and is_role_valid:
            is_logged_in = True
            logged_in_user_name = get_username(data,account)
        else:
            print(f"Invalid Credintials For {login_role} login. Please Try again with correct credentials")

        if is_logged_in:
            greet(logged_in_user_name)

#LOGIN COMPLETE
        while is_logged_in:
            if(login_role == "SUPERUSER"):
                print("Logged In as SuperUser")


        






"""
print("Utils Function")
data['01200300040000']['auth']['username'] = "Babeet"
print(get_username(data,"01200300040000"))
print(get_userpassword(data,"01200300040000"))
print(get_auth_info(data,'01200300040000').get('username'))
print(get_user_info(data,'01200300040000'))

save_data_in_file(data_file,data)
"""