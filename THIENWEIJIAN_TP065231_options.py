#THIEN WEI JIAN
#TP065231
#TAN WEI HUP
#TP065176


from THIENWEIJIAN_TP065231_validations import *

def writeTenant():
    masterList = []

    name = "Enter name: "
    ic = "Enter the identity card no (without the -): "
    phoneNum = "Enter the phone number (start with 60 and without the - and spaces): "
    dob = "Enter date of birth (must with -): "
    cob = "Enter city of birth: "
    workHistory = "Enter work history: "
    currentWork = "Enter current employer: "

    while True:
        tenantID = textInput('Enter Tenant ID: ', isAddIDValid)
        name = textInput(name, isNameValid)
        ic = textInput(ic, isIcValid)
        phoneNum = textInput(phoneNum, isPhoneValid)
        dob = textInput(dob, isDobValid)
        cob = textInput(cob, isCoBValid)
        workHistory = textInput(workHistory, isWorkHistoryValid)
        currentWork = textInput(currentWork, isCurrentWorkValid)
        record = [tenantID, name, ic, phoneNum, dob, cob, workHistory, currentWork]
        masterList.append(record)

        with open("tenant_info.txt", "a") as fhand:
            for record in masterList:
                for item in record:
                    fhand.write(item)
                    fhand.write(",")
                fhand.write("\n")

        print(masterList)
        print('Data successfully inserted!!')
        writeAuditLog('Added Tenant Details')
        break
        

def writeApartment():
    mList=[]
    while True:
        apartmentID = textInput('Enter Apartment ID: ', isAddIDValid)
        apartmentUnit = textInput('Enter apartment unit number: ', isAPUnitValid)
        doA = textInput("Enter the date of acquisition (must with -): ", isDoAValid)
        sqFoot = textInput("Enter the square footage: ", isSqFootValid)
        expectRent = textInput("Enter the expected rent: ", isRentValid)
        rentalHistory = textInput("Enter rental History: ", isRentValid)

        record = [apartmentID, apartmentUnit, doA, sqFoot + 'sf', expectRent, rentalHistory]
        mList.append(record)

                #make the apartment data in a write mode
        with open("apartment_info.txt", "a") as fhand:
            for record in mList:
                for item in record:
                    fhand.write(item)
                    fhand.write(",")
                fhand.write("\n")

            print(mList)
        print('Apartment Data successfully inserted!!')
        writeAuditLog('Added Apartment Details')
        return
    

# view all the data
def viewAllTenant():
    with open("tenant_info.txt", "r") as fhand:
        for record in fhand:
            print(record.rstrip().rstrip(","))
    return


def getTenantColumn(file_path, name):
    for column in file_path:
        if name == column[0]:
            printTenant(column)
            return column

def printTenant(information):
    tenantsDetails = [
        'ID',
        'Name',
        'IC',
        'Pnumber',
        'DOB',
        'COB',
        'WorkHistory',
        'Emplyer'
    ]

    count = 0
    for index, details in enumerate(tenantsDetails):
        count += 1
        print(f"{count}. Tenant's {details}: {information[index]}")
    print('\n')


def searchTenant():
    tenantName = textInput("Enter Tenant ID: ", isIDValid)
    tenantList = readTenantFile()
    getTenantColumn(tenantList, tenantName)

def readTenantFile():
    tenantList = []
    with open('tenant_info.txt', 'r') as data:
        for tenant in data:
            tenant = tenant.strip().strip(',').split(',')
            tenantList.append(tenant)
    return tenantList


def readAPFile():
    apartmentList = []
    with open('apartment_info.txt', 'r') as data:
        for ap in data:
            ap = ap.strip().strip(',').split(',')
            apartmentList.append(ap)
    return apartmentList

def getApColumn(file_path, name):
    for column in file_path:
        if name == column[0]:
            printAp(column)
            return column

def printAp(information):
    tenantsDetails = [
        'ID',
        'Unit',
        'Date of Acquisition',
        'Square Foot',
        'Expected Rent',
        'Rental History'
    ]

    count = 0
    for index, details in enumerate(tenantsDetails):
        count += 1
        print(f"{count}. Apartment's {details}: {information[index]}")
    print('\n')

def viewAllApartment():
    with open("apartment_info.txt", "r") as rFile:
        for record in rFile:
            print(record.rstrip().rstrip(","))
    return

def searchApartment():
    apID = textInput("Enter Apartment ID: ", isIDValid)
    apartmentList = readAPFile()
    getApColumn(apartmentList, apID)


def readPastTenantFile():
    pastTenantList = []
    with open('past_tenant.txt', 'r') as data:
        for tenant in data:
            tenant = tenant.strip().strip(',').split(',')
            pastTenantList.append(tenant)
    return pastTenantList


def getPastTenantColumn(file_path, name):
    for column in file_path:
        if name == column[0]:
            printTenant(column)
            return column

def viewPastTenant():
    with open("past_tenant.txt", "r") as rFile:
        for record in rFile:
            print(record.rstrip().rstrip(","))
    return


def searchPastTenant():
    pastTenantName = textInput("Enter Past Tenant ID: ", isIDValid)
    pastTenantList = readPastTenantFile()
    getPastTenantColumn(pastTenantList, pastTenantName)


def modifyTenant():
        tenantList = readTenantFile()
        name = textInput('Enter TenantID: ',isIDValid)
        column = getTenantColumn(readTenantFile(), name)
        option = int(input('Choose which part to change: '))
        newData = input("Enter your new data: ")

        option -= 1
        for index, data in enumerate(tenantList):
            if data == column:
                data[option] = newData
                tenantList[index] = data

        overWriteTenant(tenantList)
        writeAuditLog(f'Modified Tenant Details')
        return


def overWriteTenant(tenantList):
    with open('tenant_info.txt', 'w') as writeFile:
        for newData in tenantList:
            newData = ",".join(newData)
            writeFile.write(newData)
            writeFile.write('\n')

    print('TENANT DATA SUCCESSFULLY CHANGED!!')
    
    
    

def modifyApartment():
    apartmentList = readAPFile()
    apID = textInput('Enter Apartment ID to choose apartment: ', isIDValid)
    column = getApColumn(readAPFile(), apID)
    option = int(input('Choose which part to change: '))
    newData = input("Enter your new data: ")

    option -= 1
    for index, data in enumerate(apartmentList):
        if data == column:
            data[option] = newData
            apartmentList[index] = data
    overWriteApartment(apartmentList)
    writeAuditLog(f'Modified Apartment {apID} Details')

def overWriteApartment(apartmentList):
    with open('apartment_info.txt', 'w') as writeFile:
        for newData in apartmentList:
            newData = ",".join(newData)
            writeFile.write(newData)
            writeFile.write('\n')

    print('APARTMENT DATA SUCCESSFULLY CHANGED!!')
    

def deleteTenant():
    while True:
        tenantList = readTenantFile()
        name = textInput('Enter TenantID to delete: ',isIDValid)
        column = getTenantColumn(tenantList, name)
        deletedData = column

        for index, data in enumerate(tenantList):
            if name == data[0]:
                tenantList.remove(data)

        overWriteTenant(tenantList)
        writePastTenant(deletedData)
        writeAuditLog(f'Deleted Tenant Details')
        return


def writePastTenant(deletedData):
    with open('past_tenant.txt', 'a') as writeFile:
        deletedData = ",".join(deletedData)
        writeFile.write(deletedData)
        writeFile.write('\n')
        print('DATA ADD TO PAST TENANT!!')
        writeAuditLog('Past Tenant is Added')


def viewAuditLog():
    with open('audit_log.txt', 'r') as rFile:
        for record in rFile:
            print(record.strip())
    return

