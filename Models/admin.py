from Models.user import User

class Admin(User):
    def __init__(self,name,age,phoneNumber,email,role):
        super().__init__(name,age,phoneNumber)
        self.__email=email
        self.__role=role
    def get_email(self):
        return self.__email
    def get_role(self):
        return self.__role