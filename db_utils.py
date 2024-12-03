import yaml
from sqlalchemy import create_engine
import pandas as pd

# Function to load credentials from the credentials.yaml file
def load_credentials(file_path):
    with open(file_path, 'r') as file:
        credentials = yaml.safe_load(file)
    return credentials


# Class to handle the RDS database operations
class RDSDatabaseConnector:
    def __init__(self, credentials):
        self.host = credentials['RDS_HOST']
        self.user = credentials['RDS_USER']
        self.password = credentials['RDS_PASSWORD']
        self.database = credentials['RDS_DATABASE']
        self.port = credentials['RDS_PORT']
        self.engine = None

    def init_engine(self):
        try:
            self.engine = create_engine(
                f"postgresql://{self.user}:{self.password}@{self.host}:{self.port}/{self.database}"
            )
            print("SQLAlchemy engine successfully initialised.")
        except Exception as e:
            print(f"Error initialising engine: {e}")

    def fetch_data(self, table_name):
        if not self.engine:
            print("Engine is not initialisd. Use the `init_engine` method first.")
            return None

        try:
            query = f"SELECT * FROM {table_name}"
            df = pd.read_sql(query, self.engine)
            print(f"Data fetched successfully from table: {table_name}")
            return df
        except Exception as e:
            print(f"Error fetching data: {e}")
            return None

    def save_to_csv(self, df, file_name):
        try:
            df.to_csv(file_name, index=False)
            print(f"Data saved successfully to {file_name}")
        except Exception as e:
            print(f"Error saving data: {e}")


# Main script <3
if __name__ == "__main__":
    # Step 1: Loads credentials from the YAML file
    credentials = load_credentials("credentials.yaml")

    # Step 2: Initialises the RDSDatabaseConnector
    connector = RDSDatabaseConnector(credentials)

    # Step 3: Initialises the SQLAlchemy engine
    connector.init_engine()

    # Step 4: Fetch data from the loan_payments table
    data = connector.fetch_data("loan_payments")

    # Step 5: Save the data to a CSV file
    if data is not None:
        connector.save_to_csv(data, "loan_payments.csv")
