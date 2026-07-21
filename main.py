import sys
import Models.user as UserModel
from Models.taxi import Taxi
from Services.userService import UserService
from Services.adminService import AdminService
from Exceptions.ChoiceException import ChoiceException
from Models.admin import Admin
def main():
    userServiceObject=UserService()
    adminServiceObject=AdminService()
    admin=Admin("Admin",20,"1234567890","admin1@gmail.com","admin")
    userServiceObject.register(admin)
    
    while True:
        print("1. Login")
        print("2. Register")
        print("3. Exit")
        try:
            choice=int(input("Enter your choice : "))
            if 1<=choice<=3:
                match choice:
                    case 1:
                        #login
                        phoneNumber=input("Enter your phoneNumber : ")
                        if phoneNumber==admin.get_phoneNumber():
                            adminOperations(admin,userServiceObject,adminServiceObject)
                        else:
                            LoggedUser=userServiceObject.login(phoneNumber)
                            if LoggedUser != None :
                                userOperations(LoggedUser,userServiceObject)
                    case 2:
                        #register
                        name=input("Enter your name : ")
                        age=int(input("Enter your age : "))
                        phoneNumber=input("Enter your phoneNumber : ")
                        new_user=UserModel.User(name,age,phoneNumber)
                        userServiceObject.register(new_user)
                    case 3:
                        sys.exit("Exiting...")
            else:
                raise ChoiceException
        except ValueError:
            print("Enter only the numbers")
        except ChoiceException as e:
            print(e)

def userOperations(LoggedUser,userServiceObject):
    while True:
        print("1. Search Taxi")
        print("2. Profile")
        print("3. Logout")

        choice=int(input("Enter the choice : "))
        match choice:
            case 1:
                pass
            case 2:
                user = userServiceObject.getProfile(LoggedUser)
                print(f"Id : {user.get_id()}")
                print(f"Name : {user.get_name()}")
                print(f"Phone number : {user.get_phoneNumber()}")
            case 3:
                return

def adminOperations(admin,userServiceObject,adminServiceObject):
    while True:
        print("1. Add taxi")
        print("2. Remove taxi")
        print("3. Profile")
        print("4. Logout")
        try:
            choice=int(input("Enter the choice : "))
            if 1<=choice<=4:
                match choice:
                    case 1:
                        name=input("Enter the taxi name : ")
                        location=input("Enter the current taxi location : ")
                        taxi=Taxi(name,location)
                        adminServiceObject.addTaxi(taxi)
                    case 3:
                        user = userServiceObject.getProfile(admin)
                        print(f"Id : {user.get_id()}")
                        print(f"Name : {user.get_name()}")
                        print(f"Phone number : {user.get_phoneNumber()}")
                    case 4:
                        return
            else:
                raise ChoiceException("Enter the numbers from 1 to 4")
        except ValueError:
            print("Enter only the numbers")
        except ChoiceException as e:
            print(e)

if __name__=="__main__":
    main()