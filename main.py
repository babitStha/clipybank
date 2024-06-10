import os
from datetime import datetime
from helperFxn import *
current_date = datetime.now().strftime('%d-%m-%Y')
print("Current date:", current_date)
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
          'balance':510,
          'type':'SBA', ##SBA for Saving Account CAA for current account
        },
        'transaction':{
            datetime.now().strftime('%d%m%y%H%M%S'):{
            'amount':500,
            'type':'C',
            'date':datetime.now().strftime('%d-%m-%Y'),
            'remarks':'Account Opening Balance'
        },
        '150524172326':{
            'amount':10,
            'type':'C',
            'date':datetime.now().strftime('%d-%m-%Y'),
            'remarks':'Account Opening Balance'
        }
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


# create_transaction(data,"01200300040000")
# transaction_keys =list(data['01200300040000'].get('transaction'))
# print(transaction_keys)

# for key in transaction_keys:
#     print(data['01200300040000'].get('transaction').get(key))



# list_acct_num = list(data.keys())
# list_acct_num.sort()
# last_acct_num = list_acct_num[-1]
# print(last_acct_num)


#os.system('cls')
total_col = 50
left_space = 10
projectDetails = [" BANKING SYSTEM PROJECT  "," Team Members    "," A.Shahnawaj Hussain (Leader)    "," B.Babit Shrestha    "]
print("#"*total_col)
for heading in projectDetails:
    row = "*"*left_space + heading + "*"*(total_col-left_space-len(heading))
    print(row)
print("#"*total_col)
input("Press Any Key To Start")

os.system('cls')

greet()
run = True
while run:
#Choose Role to Login
    print("Login Menu")
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
    os.system('cls')
    attempt = 3
    while run_Login_loop:
        #os.system('cls')
        #Default Variable Initialize for Login
        print("YOu have",attempt,"attempt left")
        if(attempt<=0):
            print("You have reached your Maximum attempt exiting..")
            run = False
            break
        is_acct_num_valid = False
        is_password_valid = False
        is_logged_in = False
        account = input("Enter Your Account Number or 0 to go back:- ")
        if account == "0":
            run_Login_loop = False
            continue
        password = input("Enter Your Account Password or 0 to go back:-")
        if password == "0":
            continue
        is_acct_num_valid = account in list(data.keys())
        if is_acct_num_valid:
            is_password_valid = password == get_userpassword(data,account)
            is_role_valid = login_role == get_auth_info(data,account).get('role')
        
        if is_acct_num_valid and is_password_valid and is_role_valid:
            is_logged_in = True
            logged_in_user_name = get_username(data,account)
            logged_in_account = account
            is_logged_in=True
        else:
            print(f"Invalid Credintials For {login_role} login. Please Try again with correct credentials")
            is_logged_in = False
            attempt-=1
            continue

        if is_logged_in:
            greet(logged_in_user_name)
        #os.system('cls')

#LOGIN COMPLETE
        if(login_role == "SUPERUSER"):
            os.system('cls')
            while is_logged_in:
                print("1.Create Staff Account")
                print("0.Go Back")
                user_action = input()
                validInputs = ["1","0"]
                if user_action == "0":
                    is_logged_in = False
                    run_Login_loop = False
                    continue
                elif validateField(validInputs,user_action):
                    is_logged_in = True
                    run_Login_loop = False
                else:
                    print("Invalid Input")
                    is_logged_in = False
                    run_Login_loop = False
                
                if (user_action == "1"):
                    [instance,created_acct,default_password] = create_account_instance(data,role="STAFF")
                    data[created_acct] = instance[created_acct]
                    print(f"Staff Account Created.\n Account Number :{created_acct} \n password :{default_password}")
                    save_data_in_file('./data.txt',data)
                    input("Press Any Key To Continue")
        #STAFF LOGIN
        elif(login_role == "STAFF"):
            os.system('cls')
            while is_logged_in:
                #os.system('cls')
                print("1.   Create Create Customer Account :")
                print("2.   Print Acount Statement :")
                print("3.   Maintain Account Details :")
                print("0.Go Back")
                
                user_action = input("Please Choose An Option :")
                validInputs = ["1","0","2","3"]
                if user_action == "0":
                    is_logged_in = False
                    run_Login_loop = False
                    continue
                elif validateField(validInputs,user_action):
                    is_logged_in = True
                else:
                    print("Invalid Input")
                    continue
                
                if (user_action == "1"):
                    [instance,created_acct,default_password] = create_account_instance(data,role="CUSTOMER")
                    data[created_acct] = instance[created_acct]
                    print(f"Customer Account Created.\n Account Number :{created_acct} \n password :{default_password}")
                    save_data_in_file('./data.txt',data)
                    input("Press Any Key To Continue")
                elif(user_action == "2"):
                    validated = False
                    while not validated:
                        acct_no = input("Enter Account Number to Print Statement:")
                        if acct_no in list(data.keys()):
                            validated = True
                        else:
                            validated = False
                            print(f"{acct_no} does not Exist. ")
                    validated = False
                    while not validated:
                        from_date = input("Enter From Date (DD-MM-YYYY):-")
                        if (validateField([],from_date,"date")):
                            validated = True
                        else:
                            validated = False
                            print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")
                    validated = False
                    while not validated:
                        to_date = input("Enter To Date (DD-MM-YYYY):-")
                        if (validateField([],to_date,"date")):
                            validated = True
                        else:
                            validated = False
                            print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")
                    statementList = get_transaction_in_range(data,acct_no,from_date,to_date)
                    os.system("cls")
                    print_table(statementList)
                    print("\n\n")
                    input("Press Any Key To Return") 
                elif(user_action == "3"):
                    print("Maintain User Account")
                    validated = False
                    while not validated:
                        acct_no = input("Enter Account Number to Maintain:")
                        if acct_no in list(data.keys()):
                            validated = True
                        else:
                            validated = False
                            print(f"{acct_no} does not Exist. ")
                    if acct_no and acct_no != "":
                        update_account_details(data,acct_no)
                        acct_no = ""
        elif(login_role == "CUSTOMER"):
            os.system('cls')
            while is_logged_in:
                print("is_logged_in Loop")
                #os.system('cls')
                print("1.   Create a Transaction :")
                print("2.   Print Acount Statement :")
                print("3.   Maintain Account Details :")
                print("0.Go Back")
                
                user_action = input("Please Choose An Option :")
                validInputs = ["1","0","2","3"]
                if user_action == "0":
                    is_logged_in = False
                    run_Login_loop = False
                    continue
                elif validateField(validInputs,user_action):
                    is_logged_in = True
                else:
                    print("Invalid Input")
                    continue
                
                if (user_action == "1"):
                    #Create a Transaction
                    create_transaction(data,logged_in_account)
                    
                elif(user_action == "2"):
                    validated = False
                    while not validated:
                        from_date = input("Enter From Date (DD-MM-YYYY):-")
                        if (validateField([],from_date,"date")):
                            validated = True
                        else:
                            validated = False
                            print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")
                    validated = False
                    while not validated:
                        to_date = input("Enter To Date (DD-MM-YYYY):-")
                        if (validateField([],to_date,"date")):
                            validated = True
                        else:
                            validated = False
                            print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")
                    statementList = get_transaction_in_range(data,logged_in_account,from_date,to_date)
                    print(statementList)
                    print_table(statementList)
                    print("\n\n")
                    input("Press Any Key To Return") 
                elif(user_action == "3"):
                    print("Maintain User Account")
                    acct_no = logged_in_account
                    if acct_no and acct_no != "":
                        update_account_details(data,acct_no)
                        acct_no = ""
                        