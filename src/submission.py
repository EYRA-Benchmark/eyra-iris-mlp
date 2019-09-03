from pathlib import Path
import pickle
import pandas as pd


def my_submission(test_file, out_file):
    df = pd.read_csv(test_file)

    with open(Path('trained_model'), 'rb') as trained_model_file:
        trained_model = pickle.load(trained_model_file)

    results = trained_model.predict(df)
    data = pd.DataFrame(results).to_csv(None, header=False, index=False)
    open(out_file, 'w').write(data[:-1])


if __name__ == "__main__":
    test_file = str(Path('data')/'input'/'test_data')
    out_file = str(Path('data')/'output')

    my_submission(test_file, out_file)
