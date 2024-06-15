#THIEN WEI JIAN
#TP065231
#TAN WEI HUP
#TP065176


from THIENWEIJIAN_TP065231_options import *
from THIENWEIJIAN_TP065231_login import *


# the main menu
def starting_program():
    try:
        while True:
            print("\n" + '=' * 30)
            print('1. LOG IN\n'
                  '2. Exit Program')
            choices = int(input('Do you want to Log In or Exit?: '))
            if choices == 1:
                username, password = login()
                flag = loginUserType(username, password)
                if flag == 's':
                    super_admin_menu()
                    return True
                elif flag == 'a':
                    admin_menu()
                    return True
            elif choices == 2:
                choice = input('Do you want to exit the system?[y/n]: ')
                if choice in ['Y', 'y']:
                    writeAuditLog('=' * 15 + ' Exited Program ' + '=' * 15)
                    quit()
                elif choice in ['N', 'n']:
                    return starting_program()
    except ValueError:
        print('Enter only numbers..')
        return starting_program()



def super_admin_menu():
    print('=' * 15 + ' Welcome To Super Admin Main Menu ' + '=' * 15)

    supAdmin_menu_list = [
        ("Insert New Data", insertMenu),
        ("View Data", viewMenu),
        ("Modify Existing Data", modifyMenu),
        ("Delete Data", deleteMenu),
        ("Create New Super Admin", signUpSuperAdmin),
        ("Create New Admin", signUpAdmin),
        ("View Audit Log", viewAuditLog),
        ("Log Out", logOut)
    ]

    while True:
        menu_list, index = printMenu(supAdmin_menu_list)
        choice = input('What would you like to do? : ')
        choice = menu_choiceValidate(choice, index, super_admin_menu)
        choice -= 1
        runFunc(menu_list, choice)


def admin_menu():
    print('=' * 15 + ' Welcome To Admin Main Menu ' + '=' * 15)

    admin_menu_list = [
        ("Insert New Data", insertMenu),
        ("View Data", viewMenu),
        ("Modify Existing Data", modifyMenu),
        ("Delete Data", deleteMenu),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(admin_menu_list)
        choice = input('What would you like to do? Choose a number: ')
        choice = menu_choiceValidate(choice, index, admin_menu)
        choice -= 1
        runFunc(menu_list, choice)


def insertMenu():

    insert_menu_list = [
        ("Insert Tenant's details", writeTenant),
        ("Insert Apartment Data", writeApartment),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(insert_menu_list)
        choice = input('What would you like to Insert? Enter [X] to previous menu: ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, insertMenu)
        choice -= 1
        runFunc(menu_list, choice)

def viewMenu():
    print('=' * 15 + ' Welcome To View Main Menu ' + '=' * 15)

    view_menu_list = [
        ("View Tenant Record", view_searchCurrentTenantMenu),
        ("View Apartment Record", viewAndSearchApartmentMenu),
        ("View Past Tenant Record", viewAndSearchPastTenantMenu),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(view_menu_list)
        choice = input('What would you like to View? Enter [X] to previous menu: ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, viewMenu)
        choice -= 1
        runFunc(menu_list, choice)



def view_searchCurrentTenantMenu():
    print('=' * 15 + ' Welcome To View and Search Menu ' + '=' * 15)
    viewTenantList = [
        ("View All Current Tenant", viewAllTenant),
        ("Search Tenant", searchTenant),
        ("Log Out", logOut)
    ]

    while True:
        menu_list, index = printMenu(viewTenantList)
        choice = input('Choose your Action. Enter [X] to previous menu : ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, view_searchCurrentTenantMenu)
        choice -= 1
        runFunc(menu_list, choice)
        choice += 1

def viewAndSearchApartmentMenu():
    viewApList = [
        ("View All Apartment", viewAllApartment),
        ("Search Apartment", searchApartment),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(viewApList)
        choice = input('Choose your Action. Enter [X] to previous menu : ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, viewAndSearchApartmentMenu)
        choice -= 1
        runFunc(menu_list, choice)
        choice += 1

def viewAndSearchPastTenantMenu():
    viewPastTenList = [
        ("View All Past Tenant", viewPastTenant),
        ("Search Past Tenant", searchPastTenant),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(viewPastTenList)
        choice = input('Choose your Action. Enter [X] to previous menu : ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, viewAndSearchPastTenantMenu)
        choice -= 1
        runFunc(menu_list, choice)
        choice += 1
def modifyMenu():
    modify_menu_list = [
        ("Modify Tenant Record", modifyTenant),
        ("Modify Apartment Record", modifyApartment),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(modify_menu_list)
        choice = input('What would you like to Modify? Enter [X] to previous menu: ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, modifyMenu)
        choice -= 1
        runFunc(menu_list, choice)


def deleteMenu():
    delete_menu_list = [
        ("Delete Tenant Record", deleteTenant),
        ("Log Out", logOut)
    ]
    while True:
        menu_list, index = printMenu(delete_menu_list)
        choice = input('Choose your Action. Enter [X] to previous menu : ')
        if choice in ['X', 'x']:
            return False
        choice = menu_choiceValidate(choice, index, deleteMenu)
        choice -= 1
        runFunc(menu_list, choice)
        choice += 1

def backtoPrev():
    return False


def get_menus(menu_list):
    for index, menu in enumerate(menu_list, 1):
        menus, func = menu
        yield menus, func

def runFunc(menu_list, choice):
    for menus, func in get_menus(menu_list):
        if menu_list[choice] == (menus, func):
            return func()

def printMenu(menu_list):
    countIndex = 0
    for index, menu in enumerate(menu_list, 1):
        menus, func = menu
        print(f'{index}. {menus}')
        countIndex += 1
    return menu_list, countIndex

def logOut():
    writeAuditLog('-' * 15 + ' Logged Out ' + '-' * 15)
    return starting_program()

starting_program()
