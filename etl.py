import pandas as pd
from sqlalchemy import create_engine

# Replace with your PostgreSQL connection details
db_connection = {
    'host': 'localhost',
    'database': 'ETL',
    'user': 'postgres',
    'password': 'sql'
}

# Replace with the correct path to your Excel file
excel_file_path = r'E:\Phython\etl.csv'
df = pd.read_csv(excel_file_path)

# Transform data if needed
# (perform any necessary cleaning or formatting)

# Load data into PostgreSQL
engine = create_engine(f'postgresql://{db_connection["user"]}:{db_connection["password"]}@{db_connection["host"]}/{db_connection["database"]}')
df.to_sql('movies', engine, index=False, if_exists='replace')

print("Data loaded successfully!")
