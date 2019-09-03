import pickle
import pandas as pd
from pathlib import Path
from sklearn.neural_network import MLPClassifier

if __name__ == '__main__':
    df = pd.read_csv(Path('../data/training_data'))
    X = df.drop(["class"], axis='columns')
    Y = df["class"]

    clf = MLPClassifier(
        solver='lbfgs',
        alpha=1e-5,
        hidden_layer_sizes=(10, 10),
        random_state=1
    )

    clf.fit(X, Y)

    f = pickle.dumps(clf)

    with open(Path('./trained_model'), 'wb') as trained_model_file:
        trained_model_file.write(f)
