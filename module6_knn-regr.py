import numpy as np

# allocate storage
class KNNRegression:
    def __init__(self, n):
        self.n = n
        self.x = np.zeros(n, dtype=float) # pre-sized array to enable vectorized operations
        self.y = np.zeros(n, dtype=float)# pre-sized array to enable vectorized operations
        self.count = 0 #counter

    # add points
    def insert(self, x, y):
        self.x[self.count] = x
        self.y[self.count] = y
        self.count += 1

    #actual knn regression function
    def predict(self, x_query, k):
        if k > self.n:
            return None # exit if not enough neighbours

        distances = np.abs(self.x - x_query) #calc distance
        nearest_indices = np.argpartition(distances, k - 1)[:k] # pick indices of the k smallest distances
        return np.mean(self.y[nearest_indices]) # average the y values of k neighours

# main function to get input from user
def main():
    n = int(input("Enter a positive integer N: "))
    k = int(input("Enter a positive integer k: "))

    model = KNNRegression(n)

    for i in range(n):
        x = float(input(f"Enter x for point {i + 1}: "))
        y = float(input(f"Enter y for point {i + 1}: "))
        model.insert(x, y)

    x_query = float(input("Enter X: "))

    if k > n:
        print("Error: k must be less than or equal to N.")
    else:
        result = model.predict(x_query, k)
        print(result)


if __name__ == "__main__":
    main()
