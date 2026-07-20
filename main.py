import sys
import Models.user as UserModel
import Services.userService as userService
from Exceptions.ChoiceException import ChoiceException
from Models.admin import Admin
def main():
    userServiceObject=userService.UserService()
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
                            print("Admin Logged In")
                        else:
                            LoggedUser=userServiceObject.login(phoneNumber)
                            if LoggedUser != None :
                                userOperations(LoggedUser)
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

def userOperations(LoggedUser):
    while True:
        print("1. Search Taxi")
        print("2. Profile")
        print("3. Logout")

        choice=int(input("Enter the choice : "))
        match choice:
            case 1:
                pass
            case 2:
                pass
            case 3:
                break
    
if __name__=="__main__":
    main()