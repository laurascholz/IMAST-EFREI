import pypyodbc as odbc # pip(3) install pypyodbc;  use libary to connect to MS SQL Server

def select_ingredientsscore(api_id, product_name): #Method to get the count of harmful and harmless ingredients
    
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
    #Step 1.3 Create a cursor connection and search if ingredients consits of bad ingredients then harmful and harmless ingredients
    """

    
    sql_select_ingredientslist_id = '''
         SELECT ingredientslist_id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_ingredients = '''
         SELECT ingredientslist_harmful, ingredientslist_harmless FROM ingredientslist
            WHERE id = ? AND ingredientslist_name = ?
     '''

       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_ingredientslist_id,(api_id, product_name))    # select ingredientslist id
        ingredientslist = cursor.fetchone()
        #cursor.commit()  
        if ingredientslist == None:     # check if ingredientslist not exist for product
            #print('404: ID found in Database')
            return 404
            
        else:
            ingredientslist_id = ingredientslist[0]
            #print(ingredientslist_id)              
            cursor.execute(sql_select_ingredients,(ingredientslist_id,product_name)) #select count from harmful and harmless ingredients of ingredientslist
            ingredientscheck = cursor.fetchone()
            cursor.commit()
            #print(ingredientscheck)
            
            for i in ingredientscheck: # to check if to values were found
                if i == None:
                    #print('404: Count found in Database')
                    return 404
                else:
                    print(i)
            harmful = ingredientscheck[0] #first value is count harmful
            harmless = ingredientscheck[1] #second value is count harmless
            #print(harmful)
            #print(harmless)
            return harmful,harmless

            
       
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Ingredients Score displayed.')
        cursor.close()
        conn.close() 
         



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
    #Step 1.3 Create a cursor connection and search if ingredients consits of bad ingredients then harmful and harmless ingredients
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
         INSERT INTO ingredientscheck(ingredientslist_id,badingredients_id, product_name) 
             VALUES (?,?,?)
     '''
     
    sql_update_ingredients = '''
         UPDATE ingredientslist
            SET ingredientslist_harmful = ?, ingredientslist_harmless = ?
             WHERE id = ? AND ingredientslist_name = ?
     '''
    
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_ingredientslist_id,(api_id, product_name)) #select ingredientslist_id of ingredientslist
        ingredientslist = cursor.fetchone()
        ingredientslist_id = ingredientslist[0]
        #print(ingredientslist_id)
        cursor.commit()  
        if ingredientslist_id == None:     # check if ingredientslist not exist for product
            #print('404: Not found in Database')
            return 404
            
        else:              
            cursor.execute(sql_select_ingredients,(ingredientslist_id,product_name)) #select ingredientslist string
            ingredientslist = cursor.fetchone()
            #print(ingredientslist)
            #print(type(ingredientslist))
           
            for  i in ingredientslist: 
                 #print(i)
                 ingredients = str(i)  #change the format to string for ingredientslist string
                 #print(ingredients)

            ingredient = ingredients.split(',') #split the string after ,
            #print(ingredient)
            counter_harmful = 0 #set counter_harmful = 0
            counter_harmless = 0 #set counter_harmless = 0
            for i in ingredient:  #for every singe ingredient in ingredientslist string
                #print(i)
                remove = i.strip()    #Whitespeace removed at the beginning and end of string
                insert = "%" + remove + "%"  # add % at the front and end to get better results by comparision with bad ingredients
                #print(insert)
                cursor.execute(sql_select_badingredient_id,(insert,insert)) #select id from bad ingredients if comparision with the ingredient is sucessful
                badingredient = cursor.fetchone()  
                #print(badingredient)s
                
                if badingredient == None:     # check if ingredient is not found in table bad ingredient
                          #print('404: Not found in Database')
                          counter_harmless += 1 #set counter harmless +=1
                          
                else: 
                       #print("Bad ingredient found") 
                        counter_harmful +=1 #set counter harmful +=1
                        badingredient_id = badingredient[0] #get bad ingredient id
                        #print(badingredient_id)
                        cursor.execute(sql_insert_ingredientscheck,(ingredientslist_id,badingredient_id, product_name)) # insert match in ingredientscheck 
                        cursor.commit() 

        #print(counter_harmful)
        #print(counter_harmless)   
        cursor.execute(sql_update_ingredients,(counter_harmful,counter_harmless,ingredientslist_id,product_name)) #update counter_harmless and counter_harmful in database
        cursor.commit()  
        
        return counter_harmful,counter_harmless 
       
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Ingredients check completed.')
        cursor.close()
        conn.close() 


def select_explanation(api_id, product_name): #Method to get the explanation of bad ingredients 
    
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
    #Step 1.3 Create a cursor connection and search if ingredients consits of bad ingredients then harmful and harmless ingredients
    """

    
    sql_select_ingredientslist_id = '''
         SELECT ingredientslist_id FROM product
            WHERE api_id = ? AND product_name = ?
     '''
    
    sql_select_badingredients = '''
         SELECT badingredients_id FROM ingredientscheck
            WHERE ingredientslist_id = ? AND product_name = ?
     '''
    sql_select_explanation = '''
         SELECT explanation FROM badingredients
            WHERE id = ? AND (explanation = ? OR explanation = ? OR explanation = ? OR explanation = ?)
     '''
       
    try:
        cursor = conn.cursor()
        cursor.execute(sql_select_ingredientslist_id,(api_id, product_name)) # select ingredientslist_id
        ingredientslist = cursor.fetchone()
        #cursor.commit()  
        counter_colorant = 0  #set counter_colorant = 0
        counter_restricted = 0 #set counter_restricted = 0
        counter_preservatives = 0 #set counter_preservatives = 0
        counter_uvfilter = 0 ##set counter_uvfilter = 0
        if ingredientslist == None:     # check if ingredientslist not exists for product
            #print('404: ID found in Database')
            return 404
            
        else:
            ingredientslist_id = ingredientslist[0] #get ingredientslist_id
            #print(ingredientslist_id)              
            cursor.execute(sql_select_badingredients,(ingredientslist_id,product_name)) #select badingredients which are connected with the ingredientslist
            badingredients = cursor.fetchall()
            cursor.commit() 
            #print(badingredients)
            #return 
            for [i] in badingredients:  #for every badingredients
                #print(i)
                cursor.execute(sql_select_explanation,(i,'Colorant','Restricted','Preservatives','UV Filter')) #select the explanation
                explanation = cursor.fetchone()
                cursor.commit()
                #print(explanation)
                #set counter according to explanation of bad ingredients
                if explanation == ('Colorant',):
                    counter_colorant += 1 
                if explanation == ('Restricted',):
                    counter_restricted += 1
                if explanation == ('Preservatives',):
                    counter_preservatives +=1
                if explanation == ('UV Filter',):
                    counter_uvfilter += 1
                    
            #print(counter_colorant, counter_restricted, counter_preservatives, counter_uvfilter)  
            return counter_colorant,counter_restricted,counter_preservatives,counter_uvfilter 
                    
                
            
    except Exception as e:
        cursor.rollback()
        print(str(e))
    finally:
        print('Explanation for bad ingredients delivered.')
        cursor.close()
        conn.close()          