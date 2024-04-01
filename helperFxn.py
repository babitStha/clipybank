#Utility Functions Needed For Project
import os
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