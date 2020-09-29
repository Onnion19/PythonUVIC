
#Mostrar per pantalla 
""" 

Per mostrar el valor d'una variable o una expressio s'utiltiza la comanda print(). 

"""

print("Soc la comanda print")

#Com mostrar variables 
x = 3 
print(x)

y = True
print(y)

z = "Hola"
print (z)


#Com mostrar una mescla de variables? 
""" 

Per mesclar variables hem de convertir les numeriques en string (usant str() ) i utilitar l'operador de suma

""" 
print("--------------------------------------------") #ignorar aquesta linia


print (str(x) + z); #converteix 3 en "3", aixi que el resultat de la operacio es "3Hola"


#Llegir entrada per teclat 
"""
Podem llegir dades des de fora del programa, que ens entri el usuari.
"""
print("Com et dius?")
nom = input("\t Entra el teu nom:"); 
print("Aixi que et dius " + nom); 

edat = input("\t Quina edat tens?"); #WARNING!" Encara que entrem un numero, es detecta com si fos text.
print("Que gran que ets amb " + edat + " anys"); 


"""
Com podem llegir un numero? i que no es transformi amb text?
""" 
edat = eval(input("Entra la teva edat")); #Utiltizar eval al principi ens retorna el tipus de dada que creu mes convenient. En aquest cas un numero (si li entrem un numero esclar) 
print("Que gran que ets amb " + edat + " anys"); #Ens dona error perque no pot fer la suma de text + numero + text