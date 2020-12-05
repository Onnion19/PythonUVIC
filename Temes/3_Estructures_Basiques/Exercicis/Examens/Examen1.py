'''
Ens entraran dues seqüències de valors separats per espai. La primera conté les bases i
la segona la quantitat que s’ha trobat de cada una d’elles en un tros de DNA avaluat.
Es demana fer un programa en PYTHON que ens retorni quina és la moda de la mostra
i ens digui si és asimètrica a l’esquerra o a la dreta, tenint en compte si hi ha més bases
trobades a l’esquerra o a la dreta de la moda o bé si és simètrica si en té la mateixa
quantitat.
En cas de que hi hagi més d’una base que tingui la mateixa moda, no ha de dir si és
asimètrica o no, sinó que cal que mostri quines són aquestes bases.
Si la quantitat de valors no és igual a les dues seqüències cal que es mostri missatge
d’error.

Exemple1 : 				Exemple2:
Cadena1= A C G T 		Cadena1= A C G T
Cadena2= 18 30 15 30 	cadena2= 10 121 71 100

Resposta: 				Resposta:
Moda: T 				Moda: C
Asimètrica a l’esquerra Asimètrica a la dreta
'''

Cadena1 = "A C G T"
Cadena1.upper(); 
Cadena2 = "10 121 71 121"

Bases = Cadena1.split(); 
Ocurrencies = Cadena2.split();

#Versio exit
if (len(Bases) != len(Ocurrencies)):
	exit("Error"); 
	
#versio if-else
if (len(Bases) != len(Ocurrencies)):
	print ("Error");
	
else:
	index = []; 
	max = 0;

	#Trobem la moda
	for i in range(len(Ocurrencies)): # range [0, ultim)	
		ocurrencia = int(Ocurrencies[i]);
		if( ocurrencia > max): 
			index = [];
			max = ocurrencia; 
			index.append(i);
		elif(ocurrencia == max):
			index.append(i);

	for i in index:
		Moda = Bases[i];
		print(f'La moda es = {Moda}')

	
	if(len(index)==1):
		#Troba si es asimetric:
		  
		if( index[0] >  int(len(Ocurrencies)/2)): 
			print("Es asimetric a la l'esquerra")
		else: 
			print("Es asimetric a dreta ")
			
		#Metode alternatiu de trobar l'asimetria	
		valorsEsquerra = index[0]; 
		valorsDreta = len(Ocurrencies) - index[0] -1;

		if( valorsEsquerra >  valorsDreta): 
			print("Es asimetric a la l'esquerra")
		else: 
			print("Es asimetric a dreta ")


