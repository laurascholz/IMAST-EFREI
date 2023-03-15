# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server
import pandas as pd # pip(3) install pandas; clean up the data


# pip(3) list ; show the installed packages

"""
Step 1. Importing dataset from CSV
"""
df = pd.read_csv('BadIngredients/ingredients_uvfilters.csv') #uvfilter ingredients
# print(df) control if csv will be read

"""
Step 2.1 Data clean up
"""


try:
   df = df.dropna(subset=['Name of Common Ingredients Glossary']) #drop rows where common ingredient name doesnt exist 
except AttributeError as e:
    print('Dataset is correct.')    
    

"""
Step 2.2 Specify columns we want to import
"""

columns = ['Chemical name / INN / XAN', 'Name of Common Ingredients Glossary']

df_data = df[columns]
#print(df_data)

records = df_data.values.tolist()  
#print(records) # to control if the right columns were selected


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

# print(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME)) # to check the definition

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
# print (conn) #- show connnection

"""
#Step 3.3 Create a cursor connection and insert records
"""

sql_insert = '''
    INSERT INTO badingredients(chemical_name,ingredient_name,explanation,source) 
        VALUES (?,?,'UV Filter', 'https://ec.europa.eu/growth/tools-databases/cosing/pdf/COSING_Annex%20VI_v2.csv')
'''

try:
    cursor = conn.cursor()
    for i in records:
                print(i)
                cursor.execute(sql_insert,(i))
                cursor.commit();    
except Exception as e:
    cursor.rollback()
    print(str(e))
finally:
    print('Task is complete.')
    cursor.close()
    conn.close()