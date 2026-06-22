from sqlalchemy import create_engine
import pandas as pd

# Paste your Neon connection string here
DATABASE_URL = "postgresql://neondb_owner:npg_YU0cyIex2TGg@ep-snowy-hill-ajo07lqo-pooler.c-3.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"

engine = create_engine(DATABASE_URL)

print("Loading CSV...")

df = pd.read_csv("data/cleaned_retail_sales.csv")

# Clean column names
df.columns = (
    df.columns
      .str.strip()
      .str.replace(" ", "_")
      .str.lower()
)

print(df.columns.tolist())

df.to_sql(
    "retail_sales",
    engine,
    if_exists="replace",
    index=False,
    chunksize=10000
)

print("✅ Data uploaded successfully!")