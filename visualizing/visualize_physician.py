import polars as pl

PHYSICIAN_DATA_PATH = "../data/physicians.csv"

data_physicians = pl.read_csv(PHYSICIAN_DATA_PATH)

print(data_physicians.shape)

print(data_physicians.head())