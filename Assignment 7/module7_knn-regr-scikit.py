import numpy as np
from sklearn.neighbors import KNeighborsRegressor

class KNNRegressor:
    def __init__(self,N, k):
        self.k = k
        self.N = N
        self.X = np.zeros(N)  
        self.y = np.zeros(N)
        self.current_index = 0  


    def add_data_point(self, x, y):
        if self.current_index < self.N:
            self.X[self.current_index] = x  
            self.y[self.current_index] = y
            self.current_index += 1
        else:
            raise IndexError("Trying to add more data points than initially specified.") 


    def predict(self, X_new):

        X = self.X.reshape(-1, 1)
        X_new = np.array([X_new]).reshape(-1, 1)

        knn = KNeighborsRegressor(n_neighbors=self.k)
        knn.fit(X, self.y)
        prediction = knn.predict(X_new)[0] 
        return prediction

    def variance(self):
      return np.var(self.y)

def main():
    N = int(input("Enter the number of data points (N): "))
    k = int(input("Enter the value of k: "))

    if k > N:
        print("Error: k cannot be greater than N.")
        return

    regressor = KNNRegressor(N,k)

    print("Enter the data points (x, y) one by one:")

    for i in range(N):
        x = float(input(f"x{i+1}: "))
        y = float(input(f"y{i+1}: "))
        regressor.add_data_point(x, y)

    X_new = float(input("Enter the value of X for prediction: "))

    try:  
      result = regressor.predict(X_new)
      print("The predited value of Y is:", result)
      print(f"The Variance is {regressor.variance()}")
    except ValueError as e:
      print("Error is:", e)

main()