import insert

try:
       searchstring = 'red'
       api_id = '533212'
       product_name = 'Le Baume Miracle - CBD + Pro-collagène'
       product_brand = 'ARMANI'
       product_price = '123'
       product_link = 'https://www.sephora.fr/p/s%C3%AC-passione.de'
       product_image = 'https://www.sephora.fr/dw/image/v2/BCVW_PRD/on/demandware.static/123'
       ingredients_list = 'Helianthus Annuus Seed Oil, Coco-caprylate/Caprate, Microcrystalline Cellulose, C15-19 Alkane, Behenyl Alcohol, Stearic Acid, Butyrospermum Parkii Butter, Cetearyl Alcohol, Cannabis Sativa Seed Oil(1), Cannabis Sativa Seed Extract(1), Parfum, Cannabidiol, Caprylic/Capric Triglyceride, Cylindrotheca Fusiformis Extract, Tocopherol, Glycine Soja Oil, Linalool, Limonene, Coumarin, Eugenol, Citral '
       #if insert.searchstring_select(searchstring) == 404:   #if search string doesnt exist in database
       #      insert.searchstring_insert(searchstring)       # insert in database
       #else: 
         #     insert.searchstring_update(searchstring)       # else update search_date    
       
       #if insert.product_select(api_id, product_name) == 404:   #if product doesnt exist in database
        #      insert.product_insert(searchstring,api_id,product_name,product_brand,product_price,product_link,product_image) # insert in database
       #else: 
          #    insert.product_update(searchstring, api_id, product_name, product_price, product_link,product_image)  # else update product_price, product_link and insert a new relation if neccessary
       
       insert.ingredients_insert(api_id, product_name, ingredients_list)
       
except:
       print("Fehler bei Suche.")
    