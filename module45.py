# module4.py

# Step 1: Read N
N = int(input("Enter a positive integer N: "))

numbers = []

# Step 2: Read N numbers one by one
for i in range(N):
    num = int(input(f"Enter number {i+1}: "))
    numbers.append(num)

# Step 3: Read X
X = int(input("Enter the number to search for (X): "))

# Step 4: Search for X and output result
if X in numbers:
    # index() gives 0-based index, so add 1
    print(numbers.index(X) + 1)
else:
    print(-1)