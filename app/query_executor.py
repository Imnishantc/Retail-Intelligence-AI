from sqlalchemy import create_engine
import pandas as pd

engine = create_engine(
    "postgresql://neondb_owner:npg_YU0cyIex2TGg@ep-snowy-hill-ajo07lqo-pooler.c-3.us-east-2.aws.neon.tech/neondb?sslmode=require&channel_binding=require"
)

def execute_query(sql_query):

    df = pd.read_sql(
        sql_query,
        engine
    )

    return df