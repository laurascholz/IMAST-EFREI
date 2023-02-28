import insert

try:
       #insert.product_insert(125, 'Mascara', 'Lancome', '24.00 €', 'www.sephora.de/lancome/mascara', 'www.sehora.de/image/mascara')
       insert.search_product(125)
       print("Produkte gefunden:")
except:
       print("Keine Produkte gefunden.")
    