from abc import ABC, abstractmethod

class UserOperationInterface(ABC):
    @abstractmethod
    def login(self,phoneNumber):
        pass