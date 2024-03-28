import polars as pl

VISIT_DATA_PATH = "../data/visits.csv"

data_visits = pl.read_csv(VISIT_DATA_PATH)

print(data_visits.shape)

print(data_visits.head())