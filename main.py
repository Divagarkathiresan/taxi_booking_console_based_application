import sys
import Models.user as UserModel
from Models.taxi import Taxi
from Services.bookingService import BookingService
from Services.taxiService import TaxiService
from Services.userService import UserService
from Services.adminService import AdminService
from Exceptions.ChoiceException import ChoiceException
from Models.admin import Admin
def main():
    userServiceObject=UserService()
    adminServiceObject=AdminService()
    admin=Admin("Admin",20,"1234","admin1@gmail.com","admin")
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
    TaxiServiceObject=TaxiService()
    while True:
        print("1. Search Taxi")
        print("2. Profile")
        print("3. Logout")

        choice=int(input("Enter the choice : "))
        match choice:
            case 1:
                pickUpLocation=input("Enter the pick-up location : ")
                dropLocation=input("Enter the drop location : ")
                TaxiServiceObject.MakeTaxiListByLocation(pickUpLocation)
                bookingOperations(LoggedUser,pickUpLocation,dropLocation,TaxiServiceObject)
            case 2:
                userServiceObject.getProfile(LoggedUser)
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
                        userServiceObject.getProfile(admin)
                    case 4:
                        return
            else:
                raise ChoiceException("Enter the numbers from 1 to 4")
        except ValueError:
            print("Enter only the numbers")
        except ChoiceException as e:
            print(e)

def bookingOperations(user,pickUpLocation,dropLocation,taxiServiceObject):
    BookingServiceObject=BookingService()
    while True:
        print("1. Show all taxies")
        print("2. Go back")

        choice=int(input("Enter the choice : "))
        match choice:
            case 1:
                #Show all taxies by location
                taxiServiceObject.ListOfAllTaxisByLocation(pickUpLocation)
                print("1. Start booking")
                print("2. Cancel and go back")

                number = int(input("Enter the number : "))
                match number:
                    case 1:
                        taxiId=int(input("Enter the taxi Id : "))
                        BookingServiceObject.bookTaxi(pickUpLocation,dropLocation,user,taxiId)
                        return
                    case 2:
                        return
                    
            case 2:
                return

if __name__=="__main__":
    main()