# Loan Payments Exploratory Data Analysis

## Table of Contents
- [Description](#description)
- [Installation](#installation)
- [Usage](#usage)
  - [Step 1: Create Database Connection](#step-1-create-database-connection)
  - [Step 2: Load Data from Local Storage](#step-2-load-data-from-local-storage)
  - [Step 3: Explore Data](#step-3-explore-data)
- [Features](#features)
- [File Structure](#file-structure)
- [License](#license)

---

## Description
This project focuses on performing **Exploratory Data Analysis (EDA)** on loan payment data extracted from an AWS RDS database. The analysis aims to provide insights into borrower behavior, loan performance, and financial trends.

Key Tasks Completed:
1. Establishing a secure connection to the AWS RDS database.
2. Extracting data from the database into a Pandas DataFrame.
3. Saving the data locally for efficient access during analysis.
4. Loading the local data into Pandas and inspecting its structure.

The data contains detailed information about loans, including borrower profiles, payment plans, and loan statuses.

---

## Installation

### Requirements:
- Python 3.x
- Libraries: `pandas`, `sqlalchemy`, `pyyaml`

### Setup:
1. Clone the repository:
   ```bash
   git clone https://github.com/lunandromeda/loan-eda.git
   ```
2. Navigate to the project directory:
   ```bash
   cd loan-eda
   ```
3. Install the required dependencies
4. Create a `credentials.yaml` file in the project root

## Usage
### Step 1: Create Database Connection 
1. Load database credentials securely from the credentials.yaml file.
2. Establish a connection to the AWS RDS database using SQLAlchemy.
3. Extract data from the loan_payments table into a Pandas DataFrame.

    ```python
    from db_utils import RDSDatabaseConnector

    # Initialise connection
    connector = RDSDatabaseConnector(load_credentials("credentials.yaml"))
    connector.init_engine()

    # Fetch data
    data = connector.fetch_data("loan_payments")

    # Save locally
    connector.save_to_csv(data, "loan_payments.csv")
    ```

### Step 2: Load Data from the Local Storage 
1. Used the saved CSV file to load up the data into Pandas.
2. Inspect the data to understand its size and structure.

### Example

    ```python
    from local_utils import load_local_data

    df = load_local_data("loan_payments.csv")
    print(df.info())
    print(df.head())
    ```

## Step 3: Explore Data
1. View cokumn names, data dtypes, and descriptive statistics.
2. Prepare the data for further analysis by handling missing values, renaming columns, or filtering specific attributes.

## Features
- Secure conenction to the AWS RDS Database
- Flexible extraction of data into Pandas for analysis 
- Local data storage for faster subsequent analysis
- Detailed data dict for understanding the dataset

## File Structure 

loan-eda/
├── db_utils.py          # Handles database connections and data extraction
├── local_utils.py       # Handles loading data from local storage
├── credentials.yaml     # Stores database credentials (not tracked by Git)
├── README.md            # Project documentation
└── loan_payments.csv    # Local copy of the extracted data

## License
This project is licensed under the MIT License. See the License [LICENSE] file for more details.