class AdminService:
    taxis={}
    def __init__(self):
        pass
    def addTaxi(self,taxi):
        if taxi.get_id() not in self.taxis.keys():
            self.taxis[taxi.get_id()]=taxi
            print("New taxi added by admin")
    
