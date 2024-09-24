import psycopg2
import pandas as pd
from azure.storage.blob import BlobServiceClient
from config import DB_HOST, DB_NAME, DB_USER, DB_PASS, AZURE_STORAGE_CONNECTION_STRING, CONTAINER_NAME

def rxtract_data_from_postgres(query):
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD
        )
        df = pd.read_sql_query(query, conn)
        conn.close()
        return df
    except Exception as e:
        raise Exception(f"Error extracting data from PostgreSQL: {e}")
    
def upload_to_azure(dataframe, file_name):
    try:
        blob_service_client = BlobServiceClient.from_connection_string(AZURE_STORAGE_CONNECTION_STRING)
        container_client = blob_service_client.get_container_client(CONTAINER_NAME)
        csv_data = dataframe.to_csv(index=False)
        
        blob_client = container_client.get_blob_client(file_name)
        blob_client.upload_blob(csv_data, overwrite=True)
        print(f"File {file_name} uploaded successfully.")
    except Exception as e:
        raise Exception("Error uploading to Azure Data Lake.")
def migrate_data():
    try:
        customers_df = extract_data_from_postgres("SELECT * FROM customers;")
        payment_methods_df = extract_data_from_postgres("SELECT * FROM payment_methods;")
        payments_df = extract_data_from_postgres("SELECT * FROM payments;")
        
        
        upload_to_azure(customers_df, "customers.csv")
        upload_to_azure(payment_methods_df, "payment_methods.csv")
        upload_to_azure(payments_df, "payments.csv")
        
        print("Data migration completed successfully.")
    except Exception as e:
        raise Exception(f"Error during migration: {e}")