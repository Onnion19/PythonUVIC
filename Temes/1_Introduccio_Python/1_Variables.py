
#Tipus de variables (basiques): 
"""
 Numèriques: 
 	- Enters (int)egers
 	- Decimals (float)ing point 
 	- lògiques (bool)ean  [0-1]
Text:
	- Caràcters: 'a' '2'  '^' etcetera  Nomes pot ser 1 lletra / simbol / digit
	- Text: 'Hola que tal' , 'Text es multiples caracters'  Poden ser multiples lletres / simbols / digits
"""


#Declaracio d'una variable: 
"""
NomVariable = valor
"""
x = 2 # la variable x te com a valor 2 (enter)
y = 2.0 # la varaible y te com a valor 2.0 (decimal)
z = True # la variable z te com a valor 1 o True (Booleana)
w = False # la varialbe w te com a valor 0 o False (booleana)

a = '$' # la variable a te com a valor el CARACTER $ 
b = "soc un text" #la variable b te com a valor ( soc un text )
c = '0' # la variable c te com a valor el CARACTER 0 (no es un numero, es un simbol!!!!!!!)



#Operacions 
""" 
Per norma general no es poden barrejar operacions entre variables numeriques i de text: 

	Python en principi no sap com fer la seguent operacio: 2 + "hola que tal"

	Tampoc sap fer la seguent: 2 + "0"


	Una altre excepcio son les variables booleanes que tene tot un altre algebra apart, 
	veure la seguent seccio per mes info. 



Aixi doncs dincs de les variables numeriques podem fer les operacions de: 
Suma (+) / Resta (-) / Multiplicacio (*) / Divisio (/)

Entra les variables de text nomes podem fer l'operacio de suma (+)
"""
x = x+y; # x = 2 + 2.0 = 4 o 4.0? 
print(x) #Mostra per pantalla el valor de x


a = a+b; # a = '$' + "soc un text" = "$soc un text"
print(a) #Mostra per pantalla el valor de a 


#Operacions booleanes 
"""
Les operacions booleanes tenen un altre alegebra, i se'n diuen operacions logiques, seguint l'algebra de Boole. 
Bàsicament poden fer les seguents operacions bàsiques: 

	AND: Comprova que dos valors siguin True
	OR: Comprova que un dels dos valors sigui True 
	NOT: Nega el valor. 
"""

a = True 
b = False 
c = True

d = a and b # d = true and false = false 
e = a and c # e = true and true = true 

f = a or b # f = true or false = true 

g = not a # g = not true = false 
h = not b #h = not false = true
