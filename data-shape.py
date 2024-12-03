import pandas as pd

def load_local_data(file_path):
    try:
        # Load the data into a DataFrame
        data = pd.read_csv(file_path)

        # Print the shape of the data
        print(f"Data Shape: {data.shape}")

        # Print the first few rows of the data
        print("Sample of the data:")
        print(data.head())

        # Return the DataFrame
        return data
    except FileNotFoundError:
        print(f"Error: File not found at path {file_path}")
    except Exception as e:
        print(f"An error occurred while loading the data: {e}")

if __name__ == "__main__":
    # Path to the local CSV file
    csv_file_path = "loan_payments.csv"

    # Load the data
    loan_data = load_local_data(csv_file_path)

    # Perform further analysis or EDA on `loan_data`
    if loan_data is not None:
        print("Columns in the data:")
        print(loan_data.columns)
