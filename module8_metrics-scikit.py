#Program calculating precision and recall based on user inputs

import numpy as np
from sklearn.metrics import precision_score, recall_score


class ClassificationResults:
    def __init__(self):
        #Store points as array with shape (N, 2), each row is [true_label, predicted_label]
        self.data = np.empty((0, 2), dtype=int)

    #add new point
    def insert_point(self, x, y):
        new_point = np.array([[x, y]], dtype=int) 
        self.data = np.vstack((self.data, new_point))

    def get_true_labels(self):
        return self.data[:, 0]

    def get_predicted_labels(self):
        return self.data[:, 1]


#Get N number of points
def read_positive_integer(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value <= 0: #make sure it's positive
                print("Please enter a positive integer.")
            else:
                return value
        except ValueError:
            print("Invalid input. Please enter a positive integer.")

# Get ground truth label and predicted class
def read_binary_value(prompt):
    while True:
        try:
            value = int(input(prompt))
            if value == 0 or value == 1:
                return value
            else:
                print("Invalid input. Please enter either 0 or 1.")
        except ValueError:
            print("Invalid input. Please enter either 0 or 1.")


def main():
    results = ClassificationResults()

    n = read_positive_integer("Enter N, the number of points: ")

    #gather input
    for i in range(n):
        print(f"\nPoint {i + 1}:")
        x = read_binary_value("Enter x value, the true class label, 0 or 1: ")
        y = read_binary_value("Enter y value, the predicted class, 0 or 1: ")
        results.insert_point(x, y)

    y_true = results.get_true_labels()
    y_pred = results.get_predicted_labels()

    #calc the metrics
    precision = precision_score(y_true, y_pred, zero_division=0)
    recall = recall_score(y_true, y_pred, zero_division=0)

    #print results
    print("\nResults:")
    print(f"Precision: {precision}")
    print(f"Recall: {recall}")


if __name__ == "__main__":
    main()