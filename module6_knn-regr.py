import numpy as np

class KNNRegressor:
    def __init__(self, k):
        self.k = k
        self.X = np.array([])  
        self.y = np.array([])  

    def add_data_point(self, x, y):
        self.X = np.append(self.X, x)
        self.y = np.append(self.y, y)

    def predict(self, X_new):
        X = self.X.reshape(-1, 1) 
        distances = np.abs(X - X_new)

        # Using argsort here to get the indices that would sort distances
        sorted_distances = np.argsort(distances, axis = 0)
        # Getting the top k indices that are closest
        top_k = sorted_distances[:self.k]
        # Using those indices to get the k nearest values
        k_nearest_y = self.y[top_k]
        prediction = np.mean(k_nearest_y)
        return prediction


def main():
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    regressor = KNNRegressor(k)

    print("Enter the data points (x, y) one by one:")
    for i in range(N):
        x = float(input(f"x{i+1}: "))
        y = float(input(f"y{i+1}: "))
        regressor.add_data_point(x, y)

    X_new = float(input("Enter the value of X for prediction: "))

    result = regressor.predict(X_new)

    print("The predicted value of Y is:", result)


main()