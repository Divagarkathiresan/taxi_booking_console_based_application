from Utils.bookingIdGenerator import bookingIdGenerator
class Booking:
    def __init__(self,pickUp,drop,user,taxi):
        self.__id=bookingIdGenerator()
        self.__pickUp=pickUp
        self.__drop=drop
        self.__user=user
        self.__taxi=taxi

    # Getter for id
    def get_id(self):
        return self.__id

    # Getter for pickUp
    def get_pickUp(self):
        return self.__pickUp

    # Setter for pickUp
    def set_pickUp(self, pickUp):
        self.__pickUp = pickUp

    # Getter for drop
    def get_drop(self):
        return self.__drop

    # Setter for drop
    def set_drop(self, drop):
        self.__drop = drop

    # Getter for user
    def get_user(self):
        return self.__user

    # Setter for user
    def set_user(self, user):
        self.__user = user

    # Getter for taxi
    def get_taxi(self):
        return self.__taxi

    # Setter for taxi
    def set_taxi(self, taxi):
        self.__taxi = taxi