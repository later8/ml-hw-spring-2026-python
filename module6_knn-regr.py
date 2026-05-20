import numpy as np
from sklearn.neighbors import KNeighborsRegressor


class KNNRegression:
    def __init__(self, n):
        self.n = n
        self.x = np.zeros(n, dtype=float)
        self.y = np.zeros(n, dtype=float)
        self.count = 0

    def insert(self, x, y):
        self.x[self.count] = x
        self.y[self.count] = y
        self.count += 1

    def label_variance(self):
        return np.var(self.y)

    def predict(self, x_query, k):
        if k > self.n:
            return None

        X_train = self.x.reshape(-1, 1)
        model = KNeighborsRegressor(n_neighbors=k)
        model.fit(X_train, self.y)
        return model.predict(np.array([[x_query]]))[0]


def main():
    n = int(input("Enter a positive integer N: "))
    k = int(input("Enter a positive integer k: "))

    model = KNNRegression(n)

    for i in range(n):
        x = float(input(f"Enter x for point {i + 1}: "))
        y = float(input(f"Enter y for point {i + 1}: "))
        model.insert(x, y)

    x_query = float(input("Enter X: "))

    print(model.label_variance())

    if k > n:
        print("Error: k must be less than or equal to N.")
    else:
        print(model.predict(x_query, k))


if __name__ == "__main__":
    main()
