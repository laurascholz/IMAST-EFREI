import insert

try:
       insert.product_insert(123, 'Lippenstift', 'Lancome', '30.00 €', 'www.sephora.de/lancome/lippenstift', 'www.sehora.de/image/lippenstift')
       print("In datenbank eingespeichert")
except:
       print("Nicht eingespeichert.")
    