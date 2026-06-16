import pandas as pd
from sqlalchemy import create_engine

engine = create_engine(
    "postgresql://postgres:1234@localhost:5432/retaildb"
)

df = pd.read_csv("data/cleaned_retail_sales.csv")

df.columns = [
    "invoice",
    "stockcode",
    "description",
    "quantity",
    "invoicedate",
    "price",
    "customer_id",
    "country",
    "revenue"
]

df.to_sql(
    "retail_sales",
    engine,
    if_exists="append",
    index=False
)

print("Data Imported Successfully!")