import pickle
import numpy as np
import os
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression


def create_model():

    data = load_iris()
    X = data["data"]
    y = data["target"]

    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.33, random_state=42
    )
    clf = LogisticRegression(random_state=0).fit(X_train, y_train)

    return clf


def save_model(savePath, model):
    with open(savePath, "wb") as file:
        pickle.dump(model, file)
        print(f"Model saved in {savePath}")


if __name__ == "__main__":
    savePath = os.path.join(
        "/Users/yenchenchou/Documents/GitHub/Career_Learning_Path/demo",
        "irismodel.pkl",
    )
    label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    model = create_model()
    save_model(savePath, model)
