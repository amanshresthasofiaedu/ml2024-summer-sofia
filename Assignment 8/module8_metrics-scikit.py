import numpy as np
from sklearn.metrics import precision_score, recall_score

def main():
    N = int(input("Enter the number of data points (N): "))

    X = np.zeros(N, dtype=int)
    Y = np.zeros(N, dtype=int)

    print("Enter the data points (x, y) one by one (0 or 1 for both):")
    for i in range(N):
        while True:
            x = int(input(f"x{i+1}: "))
            if x in (0, 1):
                break
            else:
                print("Invalid input. x must be 0 or 1.")
        while True:
            y = int(input(f"y{i+1}: "))
            if y in (0, 1):
                break
            else:
                print("Invalid input. y must be 0 or 1.")


        X[i] = x
        Y[i] = y

    precision = precision_score(X, Y)
    recall = recall_score(X, Y)

    print(f"Precision: {precision}")
    print(f"Recall: {recall}")

if __name__ == "__main__":
    main()