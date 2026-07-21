from Services.taxiService import TaxiService
from Models.booking import Booking
class BookingService:
    taxis=TaxiService.taxis
    bookings = {}
    def bookTaxi(self,pickuplocation,droplocation,user,taxiId):
        for taxi in self.taxis.values():
            if taxiId == taxi.get_taxiId():
                booking = Booking(pickuplocation,droplocation,user,taxi)
                self.bookings[booking.get_id()]=booking
                taxi.set_taxiLocation(droplocation)
                print("Taxi Booked !!! ")
