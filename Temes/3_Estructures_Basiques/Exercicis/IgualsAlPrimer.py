Cadena = input("Entra una cadena\n"); 

if(len(Cadena) <= 1): 
	print("La cadena es massa curta")
	exit(); 
	
Primer = Cadena[0]; 
iguals = 0; 
for i in range(1,len(Cadena)): 
	if(Cadena[i] == Primer): 
		iguals = iguals +1; 
	elif(Cadena[i] == '*'): 
		break; 

print (f'Nhi ha {iguals} de repetits') 