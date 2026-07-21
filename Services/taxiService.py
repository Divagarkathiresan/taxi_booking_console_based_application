from Services.adminService import AdminService
class TaxiService:
   taxis =  AdminService.taxis

   def __init__(self):
      pass
   def getTaxisByLocation(self,location):
      taxi_list=[]
      for taxi in self.taxis.values():
         if taxi.get_taxiLocation().lower() == str.lower(location):
            taxi_list.append(taxi)
      return taxi_list
