import check

#ingredients_list = ' DIMETHICONE, MICA, POLYMETHYLSILSESQUIOXANE, POLYSORBATE 20, ZINC STEARATE, SYNTHETIC FLUORPHLOGOPITE, DIISOSTEARYL MALATE, CAPRYLYL GLYCOL, PHENOXYETHANOL, SODIUM DEHYDROACETATE, POTASSIUM SORBATE, TIN OXIDE, HEXYLENE GLYCOL, RICINUS COMMUNIS SEED OIL, SODIUM HYALURONATE, HYDROGENATED CASTOR OIL  '
api_id = 504189
product_name = 'Dior Backstage Rosy Glow - Blush-rose à joues universel rehausseur de couleur'


try:
       #if check.select_ingredientsscore(api_id, product_name) == 404:  #if count of harmfull and harmless ingredients dosnt exist in database
          #    check.ingredients_check(api_id, product_name)    
       check.select_explanation(api_id, product_name)

except:
       print("Fehler beim Check.")