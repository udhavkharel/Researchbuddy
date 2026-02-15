import pandas as pd
import sqlite3

DB="memory.db"
CSV="dataset.csv"

df = pd.read_csv(CSV)

conn=sqlite3.connect(DB)

df.to_sql(
    "knowledge",
    conn,
    if_exists="replace",
    index=False
)

conn.close()

print("CSV imported into database.")
