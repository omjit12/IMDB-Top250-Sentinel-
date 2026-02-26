import pandas as pd
from sqlalchemy import create_engine

df = pd.read_csv("imdb_clean.csv")

# Rename rank → movie_rank (SQL expects this)
df.rename(columns={"rank": "movie_rank"}, inplace=True)

engine = create_engine(
    "mysql+pymysql://root:Om*748908@localhost/imdb_db"
)

df.to_sql(
    "imdb_top250",
    con=engine,
    if_exists="append",
    index=False
)

print("Data inserted into MySQL ✅")