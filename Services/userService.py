from abc import ABC, abstractmethod
from Interfaces.UserOperationInterface import UserOperationInterface
class UserService(UserOperationInterface):
    users={}
    def __init__(self):
        pass
    def register(self,user):
        if user.get_id() not in self.users.keys():
            self.users[user.get_id()]=user
            print("Registration successfull !!!")

    def login(self,phoneNumber):
        flag=False
        Loggeduser=None
        for user in self.users.values():
            if phoneNumber == user.get_phoneNumber():
                flag=True
                Loggeduser=user
                break
        if flag:
            print("Login Successfull ")
            return Loggeduser
        else:
            print("User not found")

    def getProfile(self,Loggeduser):
        for user in self.users.values():
            if user.get_id() == Loggeduser.get_id():
                return user

    def allUsers(self):
        for user in self.users.values():
            print(f"{user.get_id()} {user.get_name()} ")