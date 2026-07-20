class ChoiceException(Exception):
    def __init__(self,message="Enter the numbers from 1 to 3"):
        self.message=message
        super().__init__(self.message)
    def __str__(self):
        return self.message