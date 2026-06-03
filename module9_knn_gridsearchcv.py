# module6_knn-classification-best-k.py

import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


class Dataset:
    def __init__(self):
        # Store pairs as NumPy array with shape (N, 2)
        # Each row is [x, y]
        # x = input feature
        # y = class label
        self.data = np.empty((0, 2), dtype=float)

    #add pairs
    def insert_pair(self, x, y):
        new_pair = np.array([[x, y]], dtype=float)
        self.data = np.vstack((self.data, new_pair))

    #get x value
    def get_x_values(self):
        # Scikit-learn expects input features to be 2D: [[x1], [x2], ...]
        return self.data[:, 0].reshape(-1, 1)

    #get y value
    def get_y_values(self):
        # Class labels should be integers
        return self.data[:, 1].astype(int)


#next 3 functions are preventing incorrect input
def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0:
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")


def read_non_negative_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value < 0:
                print("Please enter a non-negative integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a non-negative integer.")


def read_float(prompt):
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a real number.")


def read_dataset(dataset_name):
    dataset = Dataset()

    n = read_positive_integer(f"Enter the number of pairs for {dataset_name}: ")

    for i in range(n):
        print(f"\n{dataset_name} pair {i + 1}:")
        x = read_float("Enter x value, the input feature: ")
        y = read_non_negative_integer("Enter y value, the class label: ")
        dataset.insert_pair(x, y)

    return dataset


def find_best_k(train_dataset, test_dataset):
    x_train = train_dataset.get_x_values()
    y_train = train_dataset.get_y_values()

    x_test = test_dataset.get_x_values()
    y_test = test_dataset.get_y_values()

    best_k = None
    best_accuracy = -1

    # k cannot be larger than the number of training samples
    max_k = min(10, len(x_train))

    for k in range(1, max_k + 1):
        classifier = KNeighborsClassifier(n_neighbors=k)

        classifier.fit(x_train, y_train)

        y_pred = classifier.predict(x_test)

        accuracy = accuracy_score(y_test, y_pred)

        print(f"k = {k}, accuracy = {accuracy}")

        if accuracy > best_accuracy:
            best_accuracy = accuracy
            best_k = k

    return best_k, best_accuracy


def main():
    print("Training set input")
    train_dataset = read_dataset("TrainS")

    print("\nTest set input")
    test_dataset = read_dataset("TestS")

    best_k, best_accuracy = find_best_k(train_dataset, test_dataset)

    print("\nFinal result:")
    print(f"Best k: {best_k}")
    print(f"Corresponding test accuracy: {best_accuracy}")


if __name__ == "__main__":
    main()