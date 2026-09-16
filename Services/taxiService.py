from Services.adminService import AdminService
class TaxiService:
   taxis =  AdminService.taxis
   taxi_list=[]

   def __init__(self):
      pass
   def MakeTaxiListByLocation(self,location):
      for taxi in self.taxis.values():
         if taxi.get_taxiLocation().lower() == str.lower(location):
            self.taxi_list.append(taxi)
      return self.taxi_list

   def ListOfAllTaxisByLocation(self,location):
      for taxi in self.taxi_list:
         print(f"Taxi Id : {taxi.get_taxiId()} , Taxi Name : {taxi.get_taxiName()}")
   
