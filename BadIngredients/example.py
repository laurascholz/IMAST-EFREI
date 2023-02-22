import pypyodbc as odbc # pip install pypyodbc
import pandas as pd # pip install pandas

"""
Step 1. Importing dataset from CSV
"""
df = pd.read_csv('BadIngredients/Real-Time_Traffic_Incident_Reports.csv')

"""
Step 2.1 Data clean up
"""
df['Published Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')
df['Status Date'] = pd.to_datetime(df['Published Date']).dt.strftime('%Y-%m-%d %H:%M:%S')

# delete bad data 
df.drop(df.query('Location.isnull() | Status.isnull()').index, inplace=True)


"""
Step 2.2 Specify columns we want to import
"""
columns = [ 'Issue Reported', 'Status' ]

df_data = df[columns]
records = df_data.values.tolist()



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

print(connection_string(DRIVER,SERVER_NAME,DATABASE_NAME)) # to check the definition

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
 # print (conn) # show connnection


"""
#Step 3.3 Create a cursor connection and insert records
"""

sql_insert = '''
    INSERT INTO ingredientslist(ingredientslist_name, ingredientslist_string) 
    VALUES (?, ?)
'''

try:
    cursor = conn.cursor()
    cursor.executemany(sql_insert, records)
    cursor.commit();    
except Exception as e:
    cursor.rollback()
    print(str(e[1]))
finally:
    print('Task is complete.')
    cursor.close()
    conn.close()