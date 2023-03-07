import insert

try:
       searchstring = 'red'
       api_id = '648810'
       product_name = 'Black Opium Le Parfum - Eau de Parfum Vaporisateur'
       product_brand = 'ARMANI'
       product_price = '123'
       product_link = 'https://www.sephora.fr/p/s%C3%AC-passione.de'
       product_image = 'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/123'
       ingredients_list = ' ALCOHOL , PARFUM / FRAGRANCE , AQUA / WATER , BENZYL SALICYLATE , BENZYL ALCOHOL , LINALOOL , BUTYL METHOXYDIBENZOYLMETHANE , HYDROXYCITRONELLAL , HEXYL CINNAMAL , LIMONENE , COUMARIN , ANISE ALCOHOL , GERANIOL , CITRONELLOL , CINNAMYL ALCOHOL , AMYL CINNAMAL  '
       #if insert.searchstring_select(searchstring) == 404:   #if search string doesnt exist in database
       #      insert.searchstring_insert(searchstring)       # insert in database
       #else: 
         #     insert.searchstring_update(searchstring)       # else update search_date    
       
       #if insert.product_select(api_id, product_name) == 404:   #if product doesnt exist in database
        #      insert.product_insert(searchstring,api_id,product_name,product_brand,product_price,product_link,product_image) # insert in database
       #else: 
          #    insert.product_update(searchstring, api_id, product_name, product_price, product_link,product_image)  # else update product_price, product_link and insert a new relation if neccessary
       if insert.ingredients_select(api_id, product_name) == 404:     # if ingredients doenst exists for product
              insert.ingredients_insert(api_id, product_name, ingredients_list)  # insert ingredientslist in relation to product 
       else:
              insert.ingredients_update(api_id, product_name, ingredients_list) #update ingredientslist of product
except:
       print("Fehler bei Suche.")
    