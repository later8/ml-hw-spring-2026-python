#Input N (positive int)
N = int(input("Enter a positive integer N: "))

numbers = []

#Get all the numbers from user
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

#get the int that user is looking for
X = int(input("Enter the number to search for (X): "))

#Search for X
if X in numbers:
    #Return index+1, since this is 0-based
    print(numbers.index(X) + 1)
else:
    print(-1) #Returned if the int user is looking for is not in provided set