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
# print(df) control if csv will be read

"""
Step 2.1 Data clean up
"""
try:
   df.drop(df.query('Chemical name / INN'.isnull()).index, inplace=True) # delete data where chemical name is NULL
except AttributeError as e:
    print('Dataset is complete:')    
    print(str(e))


"""
Step 2.2 Specify columns we want to import
"""
columns = ['Chemical name / INN', 'Name of Common Ingredients Glossary', 
           'Product Type, body parts']

df_data = df[columns]
records = df_data.values.tolist()

# print(records) # to control if the right columns were selected


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

"""
#Step 3.3 Create a cursor connection and insert records
"""

#sql_insert = '''
 #   INSERT INTO Austin_Traffic_Incident 
  #  VALUES (?, ?, ?, ?, ?, ?, ?, GETDATE())
#'''

#try:
 #   cursor = conn.cursor()
  #  cursor.executemany(sql_insert, records)
   # cursor.commit();    
#except Exception as e:
 #   cursor.rollback()
  #  print(str(e[1]))
#finally:
 #   print('Task is complete.')
  #  cursor.close()
   # conn.close()
