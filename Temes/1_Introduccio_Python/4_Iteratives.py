"""
Les estructures iteratives repeteixien un conjunt d'instruccions fins que es dona una certa condicio
""" 

""" 
La mes senzilla d'entendre és l'estructura: 
 while ( condicio ):
	fer ... 
	
Amb aquesta estructura, mentre la condicio sigui certa anira repetint les mateixes instruccions. 
""" 
#Exemple 1
print("Exemple 1:");
x = 0; 
while(x < 10): #Mentre x sigui menor que 0
	print(x); #Mostra el valor de la x
	x = x+1; 
	

#Exemple 2
print ("\nExemple 2")

x = 0; 

while(x != 4): 
	x = eval( input ("Entra un numero del 1 al 10\n")); 

print("\n Numero correcte"); 


"""
L'estructura FOR es fa servir per repetir les instruccions un numero concret de vegades
""" 
print("----- FOR ----"); 
#Exemple 1
print("Exemple 1:");

for i in range(4): #el valor i anirà de 0 a 3 (en total 4 iteracions)
	print(i)
	
#Exemple 2
print ("\nExemple 2")
for i in range (10 , 15): #El valor i anirà de 10 a 14(en total 4 iteracions)
	print (i) 
		
#Exemple 3
print ("\nExemple 3")
for i in range (0 , 20 , 5): #El valor i anirà de 0 a 15 de 5 en 5. (en total 4 iteracions) 
	print (i) 
	

""" 
	Hi ha altres operacions per fer amb el for, pero es veurant amb les llistes i diccionaris
"""