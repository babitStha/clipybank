#Utility Functions Needed For Project
import os
from datetime import datetime

def create_account_instance(data,**kwargs):
    list_acct_num = list(data.keys())
    list_acct_num.sort()
    last_acct_num = list_acct_num[-1]
    next_acct_num = format(int(last_acct_num) + 1,'014d')
    validated = False
    user_name = input("Enter username:-")
    first_name = input("Enter First Name:-")
    last_name = input("Enter Last Name:")
    phone_no =input("Enter Phone Number:")
    email = input("Enter your email")
    validated = False
    while not validated:
        date_of_birth = input("Enter Your Date of Birth (DD-MM-YYYY):-")
        if (validateField([],date_of_birth,"date")):
            validated = True
        else:
            validated = False
            print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")

    address = input("Enter Your Address:- ")
    validated = False
    while not validated:
        acct_type = input("Enter Account Type SBA for saving CCA for Current:-").upper()
        if acct_type == "SBA" or acct_type=="CCA":
            validated = True
        else:
            print(f"{acct_type} is not a valid input. Please Enter a valid Input(SBA/CCA)")
            validated = False
    user_inputs = {'username':user_name,'first_name':first_name,'last_name':last_name,'phone_no':phone_no,'email':email,'date_of_birth':date_of_birth,
                   'address':address,'acct_type':acct_type}
    password = generate_password()
    instance = {
    next_acct_num:{
            'auth':{
                'username':user_inputs.get('username',''),
                'password':password,
                'role':kwargs.get('role',''),
            },
            'info':{
                'first_name':user_inputs.get('first_name',''),
                'last_name':user_inputs.get('last_name',''),
                'phone_no':user_inputs.get('phone_no',''),
                'email':user_inputs.get('email',''),
                'date_of_birth':user_inputs.get('date_of_birth',''),
                'address':user_inputs.get('address',''),
                'date_of_register':datetime.now().strftime('%d-%m-%Y'),
            },
            'account':{
              'balance':500,
              'type':user_inputs.get('first_name',''), ##SBA for Saving Account CAA for current account
            },
           'transaction':{
            datetime.now().strftime('%d%m%y%H%M%S'):{
            'amount':500,
            'type':'C',
            'date':datetime.now().strftime('%d-%m-%Y'),
            'remarks':'Account Opening Balance'
        }
    }
        }
    }
    return [instance,next_acct_num,password]



def validateField(validList:list,user_input:str,type:str = "list"):
    if type == "list":
        if user_input in validList:
            return True
        else:
            return False
    elif type == "date":
        date_format = '%d-%m-%Y'
        try:
            user_date = datetime.strptime(user_input, date_format)
            if user_date.strftime(date_format) == user_input:
                return True
            else:
                return False
        except ValueError:
            return False




def greet(username=""):
    if username == "":
        print("#"*7,"Welcome To Bank","#"*7)
    else:
        print("#"*7,f"Hi {username}","#"*7)

def get_username(data,acct_num):
    return data.get(acct_num).get('auth').get('username')

def get_userpassword(data,acct_num):
    return data.get(acct_num).get('auth').get('password')


def get_auth_info(data,acct_num):
    return data[acct_num]['auth']

def get_user_info(data,acct_num):
    return data[acct_num]['auth']

def save_data_in_file(file,data):
    with open(file,'w+') as my_file:
        my_file.write(str(data))
        
def inRange(value,start,end):
    if int(value) in range (int(start),(int(end)+1)):
        return True
    else:
        return False
    

def get_transaction_in_range(data:dict,acct_no,fromDate,toDate):
    transaction_keys =list(data[acct_no].get('transaction'))
    statementList = []
    for key in transaction_keys:
        date_str = str(data[acct_no].get('transaction').get(key).get('date'))
        tran_date = datetime.strptime(date_str,'%d-%m-%Y')
        if(tran_date >= datetime.strptime(fromDate,'%d-%m-%Y')  and tran_date <= datetime.strptime(toDate,'%d-%m-%Y')):
            amount = str(data[acct_no].get('transaction').get(key).get('amount'))
            type = str(data[acct_no].get('transaction').get(key).get('type'))
            type = "Withdrawl" if type == "D" else "Deposit"
            tran_remarks = str(data[acct_no].get('transaction').get(key).get('remarks'))
            statementList.append([key,date_str,type,amount,tran_remarks])
    return statementList
    
def print_table(data):
    if(data != []):
        col_size = 20
        header = ['Transaction ID', 'Transaction Date', 'Transaction Type', 'Transaction Amount','Transaction Remarks']
        x = [x+ " "*(col_size - len(x)) for x in header]
        formatted_header = "|".join(x)
        print(formatted_header)
        print("*"*len(formatted_header))
        for row in data:
            formatted_data = "|".join([str(data)+ " "*(col_size - len(str(data))) for data in row])
            print(formatted_data)
    else:
        print("\n\nTransaction Not Found Between Entered Date\n\n")
        return


def update_account_details(data,acct_num):
    display_option = True
    while display_option:
        print("1    Change Username :")
        print("2    Change First Name :")
        print("3    Change Last Name :")
        print("4    Change Phone No :")
        print("5    Change Email :")
        print("6    Change Date of Birth :")
        print("7    Change Address :")
        print("8    Change password :")
        print("0    Save and Exit :")
        user_input =input()
        if user_input == "1":
            print(f"Current Username {data[acct_num]['auth']['username']}")
            username = input("Enter New Username :")
            data[acct_num]['auth']['username'] = username
        
        elif user_input == "2":
            print(f"Current First Name {data[acct_num]['info']['first_name']}")
            firstName = input("Enter First Name :")
            data[acct_num]['info']['first_name'] = firstName
        elif user_input == "3":
            print(f"Current Last Name {data[acct_num]['info']['last_name']}")
            lastName = input("Enter Last Name :")
            data[acct_num]['info']['last_name'] = lastName
        elif user_input == "4":
            print(f"Current Phone No {data[acct_num]['info']['phone_no']}")
            phoneNo = input("Enter Phone No :")
            data[acct_num]['info']['phone_no'] = phoneNo
        elif user_input == "5":
            print(f"Current Change Email {data[acct_num]['info']['email']}")
            email = input("Enter New Email :")
            data[acct_num]['info']['email'] = email
        elif user_input == "6":
            print(f"Current Date of Birth  {data[acct_num]['info']['date_of_birth']}")
            dob = input("Enter New Date of Birth (DD-MM-YYYY) :")
            validated = False
            while not validated:
                if (validateField([],dob,"date")):
                    validated = True
                else:
                    validated = False
                    print("Invalid Date Format. Please Enter Date in DD-MM-YYYY format")
            data[acct_num]['info']['date_of_birth'] = dob
        elif user_input == "7":
            print(f"Current Address {data[acct_num]['info']['address']}")
            address = input("Enter New Address :")
            data[acct_num]['info']['address'] = address
        elif user_input == "8":
            #print(f"Current Address {data[acct_num]['info']['address']}")
            password = input("Enter New Password :")
            data[acct_num]['auth']['password'] = password
        elif user_input == "0":
            save_data_in_file('./data.txt',data)
            print("Changes Saved. Exiting .... ")
            display_option = False
            continue
        else:
            print("INvalid Input")
        input("Press Any Key To Continue")

def generate_password(length=8):
    random_bytes = os.urandom(length)
    hex_string = random_bytes.hex()[:length]
    return hex_string

def create_transaction(data,acct_num):
    print("CCREATE TRANSACTION")
    while True:
        avaliableBal = data[acct_num]['account'].get('balance','0')
        print("You have $ ",avaliableBal)
        print("1.Withdraw Balance")
        print("2.Deposit Balance")
        print("0.Go Back")
        choice = input("Enter Your Choice :- ")
        print(choice)
        if choice == "1" or choice =="2":
            try:
                tranAmt = int(input(f"Enter a Amount to {"Withdraw" if choice=="1" else "Deposit"}:- "))
                remarks = input("Enter Transaction Remarks:- ")
            except ValueError:
                print("Incorrect Amount Format.Couldnt Create Transaction")
                break
            if int(tranAmt)> avaliableBal and choice == "1":
                print("You Dont Have Sufficent Balance. Couldnt Create Transaction")
                break
            tranId = str(datetime.now().strftime('%d%m%y%H%M%S'))
            data[acct_num]['transaction'][tranId] ={
                    'amount':tranAmt,
                'type':'D' if choice =="1" else "C",
                'date':datetime.now().strftime('%d-%m-%Y'),
                'remarks':remarks
                }
            data[acct_num]['account']['balance']  = int(avaliableBal) - tranAmt if choice =="1" else int(avaliableBal) + tranAmt
            save_data_in_file('./data.txt',data)
            print("Transaction Created Suesfully")
            print("Your New Available Balance is",data[acct_num]['account'].get('balance','0'))
            input("Press Any Key To Continue")
            break





    
    
    
    
    
 
