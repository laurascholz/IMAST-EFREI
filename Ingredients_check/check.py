import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server

def ingredients_check(api_id, product_name): #Method to check if a ingredientslist contains bad ingredients

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
    #Step 1.3 Create a cursor connection and search if ingredients consits of bad ingredients then harmfull and harmless ingredients
    """

    
    sql_select_ingredientslist_id = '''
         SELECT ingredientslist_id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_ingredients = '''
         SELECT ingredientslist_string FROM ingredientslist
            WHERE id = ? AND ingredientslist_name = ?
     '''
     
    sql_insert_ingredientscheck = '''
         INSERT INTO ingredientscheck(ingredientslist_id,badingredients_id) 
             VALUES (?,?)
     '''
     
    sql_update_ingredients = '''
         UPDATE ingredientslist
            SET ingredientslist_harmfull = ? AND ingredientslist_harmless
             WHERE id = ? AND ingredientslist_name = ?
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_ingredientslist_id,(api_id, product_name))
        ingredientslist = cursor.fetchone()
        ingredientslist_id = ingredientslist[0]
        print(ingredientslist_id)
        cursor.commit()  
        if ingredientslist_id == None:     # check if ingredientslist exists for product
            print('404: Not found in Database')
            return 404
            
        else:              
            cursor.execute(sql_select_ingredients,(ingredientslist_id,product_name)) 
            ingredientslist = cursor.fetchone()
            #print(ingredientslist)
            #print(type(ingredientslist))
           
            for  i in ingredientslist:
                 #print(i)
                 ingredients = str(i)
                 print(ingredients)

            ingredient = ingredients.split(',')
            #print(ingredient)
            for i in ingredient:
               print(i)
             
           
            #return ingredients
       
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Ingredients check completed.')
        cursor.close()
        conn.close() 
        