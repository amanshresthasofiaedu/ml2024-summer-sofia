import numpy as np
from sklearn.neighbors import KNeighborsClassifier
from sklearn.model_selection import GridSearchCV, KFold 
from sklearn.metrics import accuracy_score

def main():
    N = int(input("Enter the number of training data points (N): "))

    X_train = np.zeros(N, dtype=float)
    y_train = np.zeros(N, dtype=int)

    print("Enter the training data points (x, y) one by one:")
    for i in range(N):
        X_train[i] = float(input(f"x{i+1}: "))
        y_train[i] = int(input(f"y{i+1}: "))

    M = int(input("Enter the number of test data points (M): "))

    X_test = np.zeros(M, dtype=float)
    y_test = np.zeros(M, dtype=int)

    print("Enter the test data points (x, y) one by one:")
    for i in range(M):
        X_test[i] = float(input(f"x{i+1}: "))
        y_test[i] = int(input(f"y{i+1}: "))

    X_train = X_train.reshape(-1, 1)
    X_test = X_test.reshape(-1, 1)

    knn = KNeighborsClassifier()

    max_k = min(10, N - 1)  
    param_grid = {'n_neighbors': range(1, max_k + 1)}
    n_splits = min(5, N)  
    cv = KFold(n_splits=n_splits, shuffle=True, random_state=42)


    grid_search = GridSearchCV(knn, param_grid, cv=cv, scoring='accuracy')
    grid_search.fit(X_train, y_train)

    best_k = grid_search.best_params_['n_neighbors']
    best_estimator = grid_search.best_estimator_
    y_pred = best_estimator.predict(X_test)
    test_accuracy = accuracy_score(y_test, y_pred)

    print(f"Best k: {best_k}")
    print(f"Corresponding test accuracy: {test_accuracy}")

if __name__ == "__main__":
    main()