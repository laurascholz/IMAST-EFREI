pip install pypyodb
pip install pandas 

import pypyodbc as odbc # pip install pypyodbc; use libary to connect to MS SQL Server
import pandas as pd # pip install pandas; clean up the data

# Step 1. Importing dataset from CSV

df = pd.read_csv('badingredients.csv')

# Step 2. Data cleanup



# database connection
DRIVER = 'SQL Server' # or mysqlserverefrei or MSQL Server
SERVER_NAME = 'mysqlserverefrei.database.windows.net'
DATABASE_NAME = 'efrei'