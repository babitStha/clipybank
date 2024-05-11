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
        },
        'account':{
          'balance':0,
          'type':'SBA', ##SBA for Saving Account CAA for current account
        },
        'transaction':{
            'amount':0,
            'type':'D',
            'date':''
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

list_acct_num = list(data.keys())
list_acct_num.sort()
last_acct_num = list_acct_num[-1]
print(last_acct_num)

run = True
#os.system('cls')
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
        os.system('cls')
        print(f"{login} is not a valid input")
        continue

    #Loop For Logging in User
    run_Login_loop = True
    
    while run_Login_loop:
        os.system('cls')
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
            is_logged_in = False

        if is_logged_in:
            greet(logged_in_user_name)
        #os.system('cls')

#LOGIN COMPLETE
        if(login_role == "SUPERUSER"):
            while is_logged_in:
                print("is_logged_in Loop")
                #os.system('cls')
                print("1.Create Staff Account")
                print("0.Go Back")
                staff_action = input()
                validInputs = ["1","0"]
                if staff_action == "0":
                    is_logged_in = False
                    continue
                elif validateField(validInputs,staff_action):
                    is_logged_in = True
                else:
                    print("Invalid Input")
                    is_logged_in = False
                
                print(is_logged_in)
                if (staff_action == "1"):
                    data = create_account_instance(data,role="STAFF")
                    print(data)
                    
                    




        






"""
print("Utils Function")
data['01200300040000']['auth']['username'] = "Babeet"
print(get_username(data,"01200300040000"))
print(get_userpassword(data,"01200300040000"))
print(get_auth_info(data,'01200300040000').get('username'))
print(get_user_info(data,'01200300040000'))

save_data_in_file(data_file,data)
"""