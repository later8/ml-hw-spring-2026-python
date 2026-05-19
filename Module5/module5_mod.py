#Modular design

class NumberStorage:
    def __init__(self):
        self.numbers = [] #create a list

    def insert(self, number):
        self.numbers.append(number) #add inputs to the list

    def search(self, x):
        for index, number in enumerate(self.numbers, start=1): #loop checking the condition and returning final value
            if number == x:
                return index
        return -1