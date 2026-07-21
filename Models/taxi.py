from Utils.taxiIdGenerator import taxiIdGenerator 
class Taxi:
    def __init__(self,taxiName,taxiLocation):
        self.__taxiId=taxiIdGenerator()
        self.__taxiName=taxiName
        self.__taxiLocation=taxiLocation
    def get_taxiId(self):
        return self.__taxiId
    def set_taxiId(self,id):
        self.__taxiId=id
    def get_taxiName(self):
        return self.__taxiName
    def set_taxiName(self, taxiName):
        self.__taxiName = taxiName
    def get_taxiLocation(self):
        return self.__taxiLocation
    def set_taxiLocation(self, taxiLocation):
        self.__taxiLocation = taxiLocation