#Utility Functions Needed For Project
import os

def create_account_instance(data,**kwargs):
    list_acct_num = list(data.keys())
    list_acct_num.sort()
    last_acct_num = list_acct_num[-1]
    next_acct_num = format(int(last_acct_num) + 1,'014d')
    print(last_acct_num)
    print(next_acct_num)
    password = ""
    user_name = input("Enter username:-")
    first_name = input("Enter First Name:-")
    last_name = input("Enter Last Name:")
    phone_no =input("Enter Phone Number:")
    email = input("Enter your email")
    date_of_birth = input("Enter Your Date of Birth (DD-MM-YYYY):-")
    address = input("Enter Your Address:- ")
    acct_type = input("Enter Account Type SBA for saving CCA for Saving:-")
    user_inputs = {'username':user_name,'first_name':first_name,'last_name':last_name,'phone_no':phone_no,'email':email,'date_of_birth':date_of_birth,
                   'address':address,'acct_type':acct_type}
    data[next_acct_num]={
            'auth':{
                'username':user_inputs.get('username',''),
                'password':user_inputs.get('password',''), # need to call fxn to generateRandom pass
                'role':kwargs.get('role',''),
            },
            'info':{
                'first_name':kwargs.get('first_name',''),
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
    save_data_in_file('./data.txt',data)
    return data



def validateField(validList:list,field:str):
    if field in validList:
        return True
    else:
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