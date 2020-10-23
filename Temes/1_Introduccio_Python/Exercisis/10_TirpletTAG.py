'''
Fer un programa que donada una seqüència de 30 nucleòtids ens compti quantes
vegades apareix la tripleta TAG.
'''

#Metode 1
print("\n\nMetode 1: split \n"); 

Cadena = input("Entra la cadena de nucleotids").split('T'); 
tripletsTrobats = 0; 
for sub in Cadena: 
	if(len(sub)>= 2): 
		if(sub[0] == 'A' and sub[1] == 'G'): 
			tripletsTrobats = tripletsTrobats +1;
			
print(f'Hi ha {tripletsTrobats} TAG'); 


#Metode 2
print("\n\nMetode 2: Caracter a caracter \n"); 

tripletsTrobats = 0; 
coincidencia = 0; 
for i in range(30): 
	caracter = input(); 
	
	if(caracter == 'T'): 
		coincidencia = 1; 
	elif(caracter == 'A' and coincidencia == 1): 
		coincidencia = 2; 
	elif(caracter == 'G' and coincidencia == 2): 
		coincidencia = 0; 
		tripletsTrobats = tripletsTrobats +1; 
	else: 
		coincidencia = 0; 

		
print(f'Hi ha {tripletsTrobats} TAG'); 
		
	
	
