
from typing import override


class AdminService:
    taxis={}
    def __init__(self):
        pass
    def addTaxi(self,taxi):
        if taxi.get_taxiId() not in self.taxis.keys():
            self.taxis[taxi.get_taxiId()]=taxi
            print("New taxi added by admin")

    @override
    def getProfile(self,admin):
        print(f"Id : {admin.get_id()}")
        print(f"Name : {admin.get_name()}")
        print(f"Phone number : {admin.get_phoneNumber()}")
    
