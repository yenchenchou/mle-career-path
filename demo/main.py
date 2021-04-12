import pickle
import numpy as np
import os
import argparse
# import uvicorn

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

from fastapi import FastAPI

app = FastAPI()

def load_model(modelPath):
    try:
        with open(modelPath, "rb") as file:
            model = pickle.load(file)
    except OSError:
        raise ("Wrong path")
    return model


def model_predict(model, X_test):
    return model.predict(X_test)


@app.get("/")
def read_root():
    return {"Hello": "World YC"}


@app.put("/predict")
def read_item(a: float, b: float, c: float, d: float):
    savePath = "irismodel.pkl"
    label_map = {0: "setosa", 1: "versicolor", 2: "virginica"}
    X_test = np.array([a, b, c, d]).reshape(1, -1)
    model = load_model(savePath)
    pred = label_map[model_predict(model, X_test)[0]]
    return pred


# if __name__ == "__main__":
#     uvicorn.run(app, host="0.0.0.0", port=8000)
