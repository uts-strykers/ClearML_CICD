import numpy as np
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score
from clearml import Task


def train_and_evaluate(task):
    X, y = make_classification(
        n_samples=1000, n_features=20, n_informative=2, random_state=42
    )
    X_train, X_test, y_train, y_test = train_test_split(
        X, y, test_size=0.25, random_state=42
    )
    model = RandomForestClassifier(n_estimators=100, random_state=42)
    model.fit(X_train, y_train)
    predictions = model.predict(X_test)
    accuracy = accuracy_score(y_test, predictions)
    task.get_logger().report_scalar("test_accuracy", "accuracy", accuracy, iteration=0)
    print(f"Test Accuracy: {accuracy:.4f}")
    print("Experiment done!")
