#Entrar dos numeros de 3 digits i comprovar que tenen tots els digits iguals 

x = eval(input("Primer numero\n")) 
while(x < 100 or x > 999): 
	x = eval(input("El numero ha de tenir 3 digits, torna a entrar-ne un\n"))
	
y = eval(input("Segon numero\n")) 
while(y < 100 or y > 999): 
	y = eval(input("El numero ha de tenir 3 digits, torna a entrar-ne un\n"))

digit = x%10; #Agafem l'ultim digit de x (si x = 658 -> agafem el 8)

sonDigitsIgual = True;#Variable per saber si tots eren iguals 

while(sonDigitsIgual and (x >= 0 or y >= 0)):
	mod_x = None;
	mod_y = None;  

	if(x>9): #Si x te dos digits (i per tant y tambe) 
		mod_x = x%10; #Agafem l'ultim numero de la dreta (ex: 567 --> 7)
		mod_y = y%10; #idem amb la variable y 
		x = int(x/10); #actualitzem la variable x (ex: 567 --> 56)
		y = int(y/10); #idem amb la variable y
	else: # Si x nomes te un digit 
		mod_x = x; #No cal fer el mod, ja que el mateix numero es un digit
		mod_y = y; 
		x = -1; #Indiquem que ja no queden numeros a les variables (ja hem obtingut tots els digits)
		y = -1;
			
	sonDigitsIgual = (mod_x==mod_y and digit == mod_x); #El mod de x i de y son iguals i al mateix temps son iguals al digit inicial

if(sonDigitsIgual): 
	print("Els digits son iguals")
else: 
	print ("Els digits no son iguals")
