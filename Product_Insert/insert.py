# first created venv for PythonProject
# python(3) -m venv venv
# source venv/bin/activate

import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server
from datetime import datetime

# pip(3) list ; show the installed packages

"""
    Methods for search string
"""

def searchstring_insert(search_string): #method to save search string in database

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

def searchstring_select(search_string): 

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
    #Step 1.3 Create a cursor connection and select data if searchstring exists, else return 404
    """
    
    sql_select_searchstring = '''
         SELECT search_string, search_date, website_name FROM searchstring
            WHERE search_string = ? AND website_name = ?
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_searchstring,(search_string, 'Sephora'))
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
        print('Searchstring search completed.')
        cursor.close()
        conn.close()

def searchstring_update(search_string): 

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
    #Step 1.3 Create a cursor connection and update search_date from searchstring
    """
    
    sql_update_searchstring = '''
            UPDATE searchstring 
             SET search_date = ?
                WHERE search_string = ? AND website_name = ?
     '''
    
    # datetime object containing current date and time
    now = datetime.now()
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_update_searchstring,(now,search_string, 'Sephora'))
        cursor.commit();    
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Search String updated successfully.')
        cursor.close()
        conn.close()


"""
    Methods for product
"""


def product_insert(search_string, api_id, product_name, product_brand, product_price, product_link, product_image): #method to save product in database with relation to search string

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
        cursor.commit(); 
        # productsearch (Relation Product_Searchstring) inserted
        
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Product saved in Database.')
        cursor.close()
        conn.close()        

def product_select(api_id, product_name): 

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
        if data_list == []:     # check if product exists in database
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
        

def product_update(search_string, api_id, product_name, product_price, product_link, product_image): #method to save update product and add a relation to search string if doesnt exist

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
    
    sql_update_product = '''
         UPDATE product
            SET product_price = ?, product_link = ?, product_image = ?
             WHERE api_id = ? AND product_name = ? 
     '''
    
    sql_select_product_id = '''
         SELECT id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_searchstring_id = '''
         SELECT id FROM searchstring
            WHERE search_string = ? AND website_name = ?
     '''       
    
    sql_select_productsearch = '''
         SELECT * FROM productsearch
            WHERE product_id = ? AND searchstring_id = ?
     '''  
     
    sql_insert_productsearch = '''
         INSERT INTO productsearch(product_id,searchstring_id) 
             VALUES (?,?)
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_update_product,(product_price,product_link,product_image,api_id,product_name))
        cursor.commit()
        print('Product updatded')
        # product updated with price, link and image 
        
        cursor.execute(sql_select_product_id,(api_id,product_name))
        product = cursor.fetchone()
        if product == []:   
            print('404: Product not found in Database')
            return 404
        else:  
            product_id = product[0]
            print(product_id)
        #cursor.commit()      
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
        
        cursor.execute(sql_select_productsearch,(product_id,searchstring_id))   
        productsearch = cursor.fetchone()
        # print(productsearch)
        if productsearch == None:   #check if relation doesnt exists
            cursor.execute(sql_insert_productsearch,(product_id,searchstring_id)) #insert new relation
            cursor.commit(); 
            print('Relation Product-Searchstring added')
            # productsearch inserted
        else:
            print("Relation Searchstring to Product already exists")
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Product and Relation to searchstring updated.')
        cursor.close()
        conn.close()        
        

def ingredients_insert(api_id, product_name, ingredients_list): #method to save ingredients in database with relation to product

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
    #Step 1.3 Create a cursor connection and insert ingredients as well as insert ingredient_id in tabel product
    """
    
    sql_insert_ingredients = '''
         INSERT INTO ingredientslist(ingredientslist_name,ingredientslist_string) 
             VALUES (?,?)
     '''
    
    sql_select_product_id = '''
         SELECT id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_ingredientslist_id = '''
         SELECT id FROM ingredientslist
            WHERE ingredientslist_name = ? AND ingredientslist_string = ? 
     '''       
    
    sql_update_product = '''
         UPDATE product 
             SET ingredientslist_id = ?
                WHERE id = ? 
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_insert_ingredients, (product_name, ingredients_list))
        cursor.commit(); 
        # ingredients saved
        
        cursor.execute(sql_select_product_id,(api_id,product_name))
        product = cursor.fetchone()
        if product == []:   
            print('404: Product not found in Database')
            return 404
        else:  
            product_id = product[0]
            print(product_id)
        cursor.commit();      
        # product_id searched
        
        cursor.execute(sql_select_ingredientslist_id,(product_name,ingredients_list))
        ingredientslist = cursor.fetchone()
        if ingredientslist == []:
            print('404: Search String not found in Database')
            return 404
        else: 
            ingredientslist_id = ingredientslist[0]
            print(ingredientslist_id)
        cursor.commit(); 
        # ingredientslist_id searched   
        
        cursor.execute(sql_update_product(ingredientslist_id,product_id))
        cursor.commit(); 
        # ingredientlist_id added to table product
        
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Ingredients saved in Database.')
        cursor.close()
        conn.close()

 