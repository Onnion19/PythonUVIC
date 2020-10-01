"""
Els condicinals permeten modificar el flux d'execució del programa en funció d'una o més condicions. 

En python s'utilirza el " if (condicio)" per executar
"""

if(True): 
	#Codi quan la condició es certa 
	print("La condicio es certa")
elif(2 < 1):
	#Si la primera condicio no era certa, evalua la que es troba dins del elif
	print("La condicio del elif es certa"); 
elif(0 > 1): 
	#Podem encadenar tants elif com volguem 
	print("El segon elif era cert"); 
else: 
	#Codi quan totes les condicions previes no s'han complert 
	print("No hi ha hagut cap condicio previa valida")
	
"""
Com a condicions podem fer servir variables / funcions o expressions, en el cas anterior hem utilitzat: 
	- Dos comparacions numeriques < / > (mes petit que / mes gran que) 
	- Un valor constant: True 
""" 
x = True; 
if(x): 
	print("la variable x es true"); 

#No tenim perque posar un else o un elif si no volem 

if(not x): 
	print("L'expressio (not x) s'evalua a cert"); 

y = 2; 
z = 2; 
if(y == z): 
	print("Y i Z tenen el mateix valor")
	
a = 1; 
b = 1.0

if(a == b): 
	print("A i B tenen el mateix valor")
	
	
	

