#Object oriented programming

#def a container to store and operate on data
class NumberStorage:
    def __init__(self):
        self.numbers = [] #define a list
    def insert(self, number): 
        self.numbers.append(number) #add to the list

    def search(self, x):
        for index, number in enumerate(self.numbers, start=1): #search for the number requested
            if number == x: #condition
                return index
        return -1


def main():
    n = int(input("Enter N: "))

    storage = NumberStorage() #call on the class defined above to store number from user

    for i in range(n):
        number = int(input(f"Enter number {i + 1}: ")) #loop to collect input from user
        storage.insert(number)

    x = int(input("Enter X: "))

    print(storage.search(x))


if __name__ == "__main__":
    main()