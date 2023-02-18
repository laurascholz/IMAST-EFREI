# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pyodbc  # pip(3) install pypyodbc;  use libary to connect to MS SQL Server
import pandas  # pip(3) install pandas; clean up the data

# pip(3) list ; show the installed packages

# Step 1. Importing dataset from CSV

#df = pd.read_csv('badingredients.csv')

# Step 2. Data cleanup

# df['']

# database connection
DRIVER = 'SQL Server' # or mysqlserverefrei or MSQL Server
SERVER_NAME = 'mysqlserverefrei.database.windows.net'
DATABASE_NAME = 'efrei'
Uid = 'azureuser'
Pwd = 'Efrei2023'
Trusted_Connection='yes'
