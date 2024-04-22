import os
from dotenv import load_dotenv
from sqlalchemy import create_engine, inspect
import pandas as pd
from pymongo import MongoClient

# Load environment variables from .env file
load_dotenv()

def load_to_mongodb(df, mongo_db, collection_name, unique_id_field):
    try:
        collection = mongo_db[collection_name]
        existing_ids = set(collection.distinct(unique_id_field))
        
        records_to_insert = []
        for record in df.to_dict(orient='records'):
            if record.get(unique_id_field) not in existing_ids:
                records_to_insert.append(record)

        if records_to_insert:
            collection.insert_many(records_to_insert)
            print(f"Inserted {len(records_to_insert)} new records into {collection_name} collection.")
        else:
            print("No new records to insert.")

    except Exception as e:
        print(f"Error loading data to MongoDB collection {collection_name}: {str(e)}")

def extract_and_load():
    try:
        # Connect to PostgreSQL database
        pg_host = os.getenv('PG_HOST')
        pg_database = os.getenv('PG_DATABASE')
        pg_user = os.getenv('PG_USER')
        pg_password = os.getenv('PG_PASSWORD')
        pg_engine = create_engine(f'postgresql://{pg_user}:{pg_password}@{pg_host}/{pg_database}')
        pg_conn = pg_engine.connect()

        # Connect to MongoDB
        mongo_uri = os.getenv('MONGODB_URI')
        mongo_db_name = os.getenv('MONGODB_DATABASE')
        client = MongoClient(mongo_uri)
        mongo_db = client[mongo_db_name]

        # Define LEGO tables and their unique identifier fields
        lego_tables = {
            'lego_colors': 'id',
            'lego_inventories': 'id',
            'lego_inventory_parts': 'inventory_id',
            'lego_inventory_sets': 'inventory_id',
            'lego_part_categories': 'id',
            'lego_parts': 'part_num',
            'lego_sets': 'set_num',
            'lego_themes': 'id'
        }

        for table_name, unique_id_field in lego_tables.items():
            df = pd.read_sql_table(table_name, pg_conn)
            load_to_mongodb(df, mongo_db, table_name, unique_id_field)

    except Exception as e:
        print("Error during ETL process:", str(e))
    finally:
        pg_conn.close()
        client.close()

# Run the ETL process
if __name__ == "__main__":
    extract_and_load()

