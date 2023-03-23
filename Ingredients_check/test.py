import check

#ingredients_list = ' DIMETHICONE, MICA, POLYMETHYLSILSESQUIOXANE, POLYSORBATE 20, ZINC STEARATE, SYNTHETIC FLUORPHLOGOPITE, DIISOSTEARYL MALATE, CAPRYLYL GLYCOL, PHENOXYETHANOL, SODIUM DEHYDROACETATE, POTASSIUM SORBATE, TIN OXIDE, HEXYLENE GLYCOL, RICINUS COMMUNIS SEED OIL, SODIUM HYALURONATE, HYDROGENATED CASTOR OIL  '
api_id = 473723
product_name = 'Caviar Stick Eye Colour - Fard à Paupières En Crayon'


try:
       if check.select_ingredientsscore(api_id, product_name) == 404:  #if count of harmfull and harmless ingredients dosnt exist in database
              check.ingredients_check(api_id, product_name)    
       

except:
       print("Fehler beim Check.")