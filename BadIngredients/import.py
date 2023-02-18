# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server
import pandas as pd # pip(3) install pandas; clean up the data

# pip(3) list ; show the installed packages

"""
Step 1. Importing dataset from CSV
"""
df = pd.read_csv('BadIngredients/badingredients.csv')
print(df)

"""
Step 2.1 Data clean up
"""
#df['Published Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
#df['Status Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

#df.drop(df.query('Location.isnull() | Status.isnull()').index, inplace=True) # delete bad data 



"""
Step 3.1 Create SQL Servre Connection String
"""
DRIVER = 'ODBC Driver 18 for SQL Server' 
SERVER_NAME = 'mysqlserverefrei.database.windows.net'
DATABASE_NAME = 'efrei'

def connection_string(driver, server_name, database_name):
    conn_string = f"""
        DRIVER={{{driver}}};
        SERVER={server_name};
        DATABASE={database_name};
        Trust_Connection=yes; 
        Uid=azureuser;
        PwD=Efrei2023;
               
    """
    return conn_string

#print(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME)) # to check the definition

""""
#Step 3.2 Create database connection instance
"""
try:
   conn = odbc.connect(connection_string(DRIVER, SERVER_NAME, DATABASE_NAME))
except odbc.DatabaseError as e:
    print('Database Error:')    
    print(str(e.value[1]))
except odbc.Error as e:
    print('Connection Error:')
    print(str(e.value[1]))
# print (conn) - show connnection


