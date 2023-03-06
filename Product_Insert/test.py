import insert

try:
       searchstring = 'red'
       api_id = '123'
       product_name = 'Sì Passione - Coffret Eau de Parfum'
       product_brand = 'ARMANI'
       product_price = '123'
       product_link = 'https://www.sephora.fr/p/s%C3%AC-passione.de'
       product_image = 'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/123'
       
       #if insert.searchstring_select(searchstring) == 404:   #if search string doesnt exist in database
       #      insert.searchstring_insert(searchstring)       # insert in database
       #else: 
         #     insert.searchstring_update(searchstring)       # else update search_date    
       
       if insert.product_select(api_id, product_name) == 404:   #if product doesnt exist in database
              insert.product_insert(searchstring,api_id,product_name,product_brand,product_price,product_link,product_image) # insert in database
       else: 
              insert.product_update(searchstring, api_id, product_name, product_price, product_link,product_image)  # else update product_price, product_link and insert a new relation if neccessary
       
       #insert.product_insert('Chanel',139, 'Mascara', 'Chanel', '24.00 €', 'www.sephora.de/chanel/mascara', 'www.sehora.de/image/mascara')
       #insert.search_product(126, 'Mascara')

       #insert.ingredients_insert(517720, 'Lip + Cheek - Blush Crème', 'WATER/AQUA/EAU, COPERNICIA CERIFERA (CARNAUBA) WAX/CERA CARNAUBA/CIRE DE CARNAUBA, GLYCERYL STEARATE')
       
except:
       print("Fehler bei Suche.")
    