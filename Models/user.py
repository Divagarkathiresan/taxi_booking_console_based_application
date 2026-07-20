from Utils.userIdGenerator import userIdGenerator
class User:
    def __init__(self,name,age,phoneNumber):
        self.__id=userIdGenerator()
        self.__name=name
        self.__age=age
        self.__phoneNumber=phoneNumber
    def get_name(self):
        return self.__name
    def get_age(self):
        return self.__age
    def get_phoneNumber(self):
        return self.__phoneNumber
    def get_id(self):
        return self.__id
    
    