#es fehlt die Einbindung der Datenbanken, deshalb hier erstmal nur die Logik

ing_list= ["Hallo", "Wasser", "Niacinamid", "Luft", "BHA", "Tea Tree Extract", "AHA", "Glycerin"]  # List of ingredients of cosmetic product
bad = ["Niacinamid", "Luft", "Erde", "AHA"]                                # List of bad ingredients


counter = 0             #counter of bad ingredients found
j = 0  
k = 0
ing_number = len(ing_list)     #number of ingredients in ing_Liste
while  len(bad)  > j:                        #as long as there are ingredients in the bad List left,...
    while ing_number > k:                   #the ingredients list of the product is checked for the bad ingredient
        if bad[j] in ing_list[k]:
            counter += 1                #the number of bad ingredients is counted, the bad ingredient is printed
            print(bad[j])
        k +=1
    j +=1
    k = 0   
    
    #print(j + counter)

score = counter / ing_number              #a score is calculated
print(score)