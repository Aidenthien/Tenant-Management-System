# THIEN WEI JIAN
# TP065231
# TAN WEI HUP
# TP065176


def isAddIDValid(id):
    if len(id) < 1:
        print('Empty Input is not Allowed... ')
        return False
    elif len(id) < 3:
        print('Invalid ID')
        return False
    elif not alphaValid(id) and digitValid(id):
        return False
    elif (id[0], id[1]) != ('T', 'N') and (id[0], id[1]) != ('A', 'P'):
        print('Invalid ID')
        return False

    with open('tenant_info.txt', 'r') as rFile:
        idList = []
        for records in rFile:
            records = records.strip().split(',')
            idList.append(records[0])

        if id in idList:
            return False

    with open('apartment_info.txt', 'r') as rFile:
        idList = []
        for records in rFile:
            records = records.strip().split(',')
            idList.append(records[0])

        if id in idList:
            return False

    return True

def isIDValid(id):
    if len(id) < 1:                                 #if the id is less than 1
        print('Empty Input is not Allowed... ')
        return False
    elif len(id) < 3:                               #if the id is less than 3
        print('Invalid ID')
        return False
    elif not digitandnumberValid(id):               #call the function to check is it valid
        return False
    return True

#this function can check ID and AP unit validation is it in the right format
def digitandnumberValid(info):
    if not any(char.isdigit() for char in info):        #check the character is it digit or not, if no digit then print the text
        print('At least One number is required...')
        return False
    elif not any(char.isalpha() for char in info):      #check the character is it alphabet or not, if no alphabet then print the text
        print('At least one Alphabet is required...')
        return False
    return True

def checkIDexist(id):
    while True:
        with open('tenant_info.txt', 'r') as rFile:
            idList = []
            for records in rFile:
                records = records.strip().split(',')
                idList.append(records[0])

            if id not in idList:
                print('Invalid ID')
                break

        return True

def alphaValid(data):
    if not any(char.isalpha() for char in data):
        print('At least one Alphabet is required...')
        return False
    return True


def digitValid(data):
    if not any(char.isdigit() for char in data):
        print('At least One number is required...')
        return False
    return True

# check is the apartment unit is valid or not
def isAPUnitValid(apUnit):
    if len(apUnit) < 1:  # if  the apartment unit less than 1
        print('Empty Input is not Allowed... ')
        return False
    elif len(apUnit) < 5:  # if  the apartment unit less than 5
        print('Invalid apartment Unit..')
        return False
    elif not alphaValid(apUnit) and digitValid(apUnit):  # call the function to check is it valid
        return False
    return True


# check is the name valid or not
def isNameValid(name):
    name = name.strip()  # remove the spaces at the begin and end of the string

    # check the character if it not alphabet or is less than 6 then print the text
    if not any(characters.isalpha() for characters in name) or len(name) < 6:
        print('Name must follow IC.')
        return False

    # check the character is it digit or not, if got digit then print the text
    elif any(characters.isdigit() for characters in name):
        print('Name cannot contain numbers.')
        return False

    return True


# check whether the IC is correct or not
def isIcValid(ic):
    if len(ic) < 12 or len(ic) > 12:  # the length must be in 12
        return False
    if not ic.isdigit():  # if ic is not digits
        return False

    return True


# check whether the phone is correct or not
def isPhoneValid(phone):
    phone = phone.replace('-', '').replace(' ','')  # replace the string from - to empty and remove spaces if found the input
    if len(phone) < 11 or len(phone) > 12:  # length must not more than 12 and less than 11
        return False
    if not phone.isdigit():  # if phone is not digits
        return False

    return True


# check is the date of birth correct or not
def isDobValid(date_of_birth):
    if len(date_of_birth) < 10 or len(date_of_birth) > 10:  # the length cannot more than 10 or less than 10
        return False

    return True


# check whether is there a digit inside the city of birth
def isCoBValid(cityOfBirth):
    for character in cityOfBirth:  # convert cityOfBirth into character
        if character.isdigit():  # the character cannot have digit inside
            return False
        elif not character.isalpha():  # the character must be in alphabet input
            return False
    return True


# check whether is there a digit inside the work history
def isWorkHistoryValid(workHistory):
    for character in workHistory:  # convert workHistory into character
        if character.isdigit():  # cannot input digit
            return False
        if character == '':  # not everyone have work history so if they dont have work history means empty input
            return 'None'

    return True


# check whether is there a digit inside the current work
def isCurrentWorkValid(currentWork):
    for character in currentWork:  # convert currentWork into character
        if character.isdigit():  # cannot have digit inside the input
            return False

    return True


# check is date of acquisition in correct input or no
def isDoAValid(dateOfAcquisition):
    if len(dateOfAcquisition) < 10 or len(dateOfAcquisition) > 10:  # the length cannot more than 10 or less than 10
        return False

    return True


# check is sq foot correct input or no
def isSqFootValid(sqFoot):
    sqFoot = sqFoot.strip('  sf').strip()  # remove the spaces at the begin of sf and remove spaces again
    if len(str(sqFoot)) < 3:  # length cannot less than 3
        return False
    if len(str(sqFoot)) > 250:  # length cannot more than 250
        return False
    for characters in sqFoot:  # convert sqFoot into character
        if not characters.isdigit():  # character must in digit input
            return False

    return True


# check is the rent input correct or not
def isRentValid(rent):
    if len(rent) <= 3:  # length of rent cannot less than or equals to 3
        print('Minimum 1k is required...')
        return False
    elif not any(char.isdigit() for char in rent):  # convert rent into char and char must be in digit input
        print('Only Numbers...')
        return False
    return True


def textInput(prompt, dataValidation):
    try:
        value = input(prompt)
        if not dataValidation(value):
            return textInput(prompt, dataValidation)
        return value

    except ValueError:
        print("Error")
        return ValueError


def menu_choiceValidate(choice, menuIndex, function):
    try:
        choice = int(choice)
        if choice > menuIndex or choice <= 0:
            print('Invalid Option')
            return function()
    except ValueError:
        print('Empty Input is Not Allowed')
        return function()

    return choice

def writeAuditLog(text):
    data = text
    with open('audit_log.txt', 'a') as wFile:
        wFile.write(data + '\n')

    return

def isEmpty(data):
    if data == '':
        return False
    return True