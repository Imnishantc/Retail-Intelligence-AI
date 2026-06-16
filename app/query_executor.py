from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://postgres:1234@localhost:5432/retaildb"
)

def execute_query(sql_query):

    df = pd.read_sql(
        sql_query,
        engine
    )

    return df