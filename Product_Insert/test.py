import insert

try:
       searchstring = 'Boss'
       #insert.searchstring_insert('Blush')
       if insert.searchstring_select(searchstring) == 404:   #if search string doesnt exist in database
              insert.searchstring_insert(searchstring)       # insert in database
       else: 
              insert.searchstring_update(searchstring)       # else update search_date    
       
       #insert.searchstring_update('Mascara')
       #insert.product_insert('Chanel',139, 'Mascara', 'Chanel', '24.00 €', 'www.sephora.de/chanel/mascara', 'www.sehora.de/image/mascara')
       #insert.search_product(126, 'Mascara')
       #insert.searchstring_insert('Lancome')

       #insert.ingredients_insert(517720, 'Lip + Cheek - Blush Crème', 'WATER/AQUA/EAU, COPERNICIA CERIFERA (CARNAUBA) WAX/CERA CARNAUBA/CIRE DE CARNAUBA, GLYCERYL STEARATE')
       
except:
       print("Fehler bei Suche.")
    