import polars as pl

REVIEW_DATA_PATH = "../data/reviews.csv"

data_reviews = pl.read_csv(REVIEW_DATA_PATH)

print(data_reviews.shape)

print(data_reviews.head())