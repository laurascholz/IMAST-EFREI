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
    
    sql_select_badingredient_id = '''
         SELECT id FROM badingredients
            WHERE chemical_name LIKE CONVERT(NVARCHAR(MAX),?) OR ingredient_name LIKE CONVERT(NVARCHAR(MAX),?)    
     '''
     
    sql_insert_ingredientscheck = '''
         INSERT INTO ingredientscheck(ingredientslist_id,badingredients_id) 
             VALUES (?,?)
     '''
     
    sql_update_ingredients = '''
         UPDATE ingredientslist
            SET ingredientslist_harmfull = ?, ingredientslist_harmless = ?
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
                 #print(ingredients)

            ingredient = ingredients.split(',') #', '
            print(ingredient)
            counter_harmfull = 0
            counter_harmless = 0
            for i in ingredient:
                print(i)
                remove = i.strip()    #Whitespeace removed at the beginning and end of string
                insert = "%" + remove + "%"  #search for word in a string 
                #print(insert)
                cursor.execute(sql_select_badingredient_id,(insert,insert))
                badingredient = cursor.fetchone()  
                #print(badingredient)s
                
                if badingredient == None:     # check if ingredientslist exists for product
                          print('404: Not found in Database')
                          counter_harmless += 1
                          
                else: 
                       #print("Bad ingredient found") 
                        counter_harmfull +=1
                        badingredient_id = badingredient[0]
                        print(badingredient_id)
                        cursor.execute(sql_insert_ingredientscheck,(ingredientslist_id,badingredient_id))
                        cursor.commit()  
                                
        print(counter_harmfull)
        print(counter_harmless)   
        cursor.execute(sql_update_ingredients,(counter_harmfull,counter_harmless,ingredientslist_id,product_name))
        cursor.commit()    
       
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Ingredients check completed.')
        cursor.close()
        conn.close() 
        