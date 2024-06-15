#THIEN WEI JIAN
#TP065231
#TAN WEI HUP
#TP065176


from THIENWEIJIAN_TP065231_validations import *
import datetime

# Getting super admin and admin
def get_user():
    with open("userCredentials.txt", "r") as readFile:      
        for index, data in enumerate(readFile, 1):
            username, password, userType = data.strip('\n').split(', ')
            yield username, password, userType

#sign up for super admin
def signUpSuperAdmin():
    name = input('Enter Name:')
    password = input('Enter password: ')

    with open('userCredentials.txt', 'a') as writeFile:
        #write the name input and password input and s input into writeFile
        writeFile.write(name + ', ' + password + ', s\n')

#sign up for admin
def signUpAdmin():
    name = input('Enter Name:')
    password = input('Enter password: ')

    with open('userCredentials.txt', 'a') as writeFile:
        #write the name input and password input and a input into writeFile
        writeFile.write(name + ', ' + password + ', a\n')

#check is user exist or not
def user_exists(username, password):
    #convert get_user function into user and check is the user equals to the user credentials file
    return any(user == (username, password, 's') or user == (username, password, 'a') for user in get_user())

#use to print text if the input is match to the user credentials file
def loginUserType(username, password):
    superAdminFlag = 's'
    adminFlag = 'a'
    for user in get_user():
        if (username, password, 's') == user:       #if the user is equals to username, password and s then print the text
            print('Welcome Back, Super Admin ' + username)
            return superAdminFlag
        elif (username, password, 'a') == user:     #if the user is equals to username, password and a then print the text
            print('Welcome Back, Admin ' + username)
            return adminFlag

#check whether the username and password is exist inside the user credentials file or not
def login():
    while True:
        username = input('Enter Your Username: ')
        password = input('Enter Your Password: ')
        if not user_exists(username, password):         #if the username and password is not exist inside the user credentials file
            print('INVALID USERNAME OR PASSWORD')
            continue    
        else:
            currentDT = datetime.datetime.now()
            currentDT = currentDT.strftime("%Y-%m-%d %H:%M:%S")
            currentDT = str(currentDT)
            writeAuditLog('[' + currentDT + '] ' + username + " Logged In ")
            return username, password

def loginPeriod():
    currentDT = datetime.datetime.now()

    if currentDT.hour >= 21 or currentDT.hour < 8:
        print('Working Hour is over, Please Login At 8am.')
        return False

    return True