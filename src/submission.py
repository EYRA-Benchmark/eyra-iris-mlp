from pathlib import Path
import pickle
import pandas as pd


def my_submission(test_file, out_file):
    df = pd.read_csv(test_file)

    with open(Path('trained_model'), 'rb') as trained_model_file:
        trained_model = pickle.load(trained_model_file)

    results = trained_model.predict(df)
    pd.DataFrame(results).rename(columns={0: 'class'}).to_csv(out_file, header=True, index=False)


if __name__ == "__main__":
    test_file = str(Path('data')/'input'/'test_data')
    out_file = str(Path('data')/'output')

    my_submission(test_file, out_file)
