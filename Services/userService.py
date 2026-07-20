class UserService:
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
        if flag:
            print("Login Successfull ")
            return Loggeduser
        else:
            print("User not found")

    def allUsers(self):
        for user in self.users.values():
            print(f"{user.get_id()} {user.get_name()} ")