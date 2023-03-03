# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server

# pip(3) list ; show the installed packages

def searchstring_insert(search_string):

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
    #Step 1.3 Create a cursor connection and insert search string
    """
    #search_date will insert automatically
    sql_insert_searchstring = '''
         INSERT INTO searchstring(search_string,website_name) 
             VALUES (?,?)
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_searchstring,(search_string, 'Sephora')) #currently we only search on Sephora
        cursor.commit();    
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Search String saved in Database.')
        cursor.close()
        conn.close() 


def product_insert(search_string, api_id, product_name, product_brand, product_price, product_link, product_image):

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
    #Step 1.3 Create a cursor connection and insert product as well as insert product_id and searchstring_id in tabel productsearch
    """
    
    sql_insert_product = '''
         INSERT INTO product(api_id, product_name, product_brand, product_price, product_link, product_image) 
             VALUES (?,?,?,?,?,?)
     '''
    
    sql_select_product_id = '''
         SELECT id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_searchstring_id = '''
         SELECT id FROM searchstring
            WHERE search_string = ? AND website_name = ?
     '''       
    
    sql_insert_productsearch = '''
         INSERT INTO productsearch(product_id,searchstring_id) 
             VALUES (?,?)
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_product,(api_id,product_name,product_brand,product_price,product_link,product_image))
        cursor.commit(); 
        # product saved
        
        cursor.execute(sql_select_product_id,(api_id,product_name))
        product = cursor.fetchone()
        if product == []:   
            print('404: Product not found in Database')
            return 404
        else:  
            product_id = product[0]
            print(product_id)
        #cursor.commit();      
        # product_id searched
        
        cursor.execute(sql_select_searchstring_id,(search_string,'Sephora'))
        searchstring = cursor.fetchone()
        if searchstring == []:
            print('404: Search String not found in Database')
            return 404
        else: 
            searchstring_id = searchstring[0]
            print(searchstring_id)
        #cursor.commit(); 
        # searchstring_id searched   
        
        cursor.execute(sql_insert_productsearch,(product_id,searchstring_id))
        # productsearch inserted
        cursor.commit(); 
        
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Product saved in Database.')
        cursor.close()
        conn.close()        

def search_product(api_id, product_name):

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
    #Step 1.3 Create a cursor connection and insert records if product not exists in database
    """
    
    sql_select = '''
         SELECT product_name,product_brand,product_price,product_link,product_image FROM product
            WHERE api_id = ? AND product_name = ?
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select,(api_id, product_name))
        data_list = cursor.fetchall()
        if data_list == []:
            print('404: Not found in Database')
            return 404
            
        else: 
            for row in data_list:
                print(data_list)
                return data_list
                       
        cursor.commit();    
       
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Product search completed.')
        cursor.close()
        conn.close()  