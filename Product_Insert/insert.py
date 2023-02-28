# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server

# pip(3) list ; show the installed packages

def product_insert(api_id, product_name, product_brand, product_price, product_link, product_image):

    """
    Step 1.1 Create SQL Server Connection String
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
    #Step 1.2 Create database connection instance
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
    #Step 1.3 Create a cursor connection and check if results are already in Database
    """
    #try:
    sql_select = '''
          SELECT product_name, product_brand, product_price, product_link, product_image FROM product
               where api_id = ? 
        '''
       
    try:
            cursor = conn.cursor()
            cursor.execute(sql_select,(api_id))
            cursor.commit();    
    except Exception as e:
            cursor.rollback()
            print(str(e))
    finally:
            print('Task is complete.')
            cursor.close()
            conn.close()
    #except:
       # """
        #Step 1.4 Create a cursor connection and insert records if product not exists in database
       # """
    
        #sql_insert = '''
           # INSERT INTO product(api_id, product_name, product_brand, product_price, product_link, product_image) 
           #     VALUES (?,?,?,?,?,?)
       # '''
       
       # try:
          #  cursor = conn.cursor()
           # cursor.execute(sql_insert,(api_id,product_name,product_brand,product_price,product_link,product_image))
           # cursor.commit();    
        #except Exception as e:
          # cursor.rollback()
          # print(str(e))
        #finally:
          #  print('Task is complete.')
           # cursor.close()
           # conn.close()
