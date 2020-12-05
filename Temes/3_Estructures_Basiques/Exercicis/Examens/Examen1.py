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
Cadena2= 18 10 15 30 	cadena2= 10 121 71 100

Resposta: 				Resposta:
Moda: T 				Moda: C
Asimètrica a l’esquerra Asimètrica a la dreta
'''

Cadena1 = "A C G T"
Cadena1.upper(); 
Cadena2 = "10 121 71 100"

Bases = Cadena1.split(); 
Ocurrencies = Cadena2.split();

index = 0; 
max = 0;

#Trobem la moda
for i in range(len(Ocurrencies)): # range [0, ultim)	
	ocurrencia = int(Ocurrencies[i]);
	if( ocurrencia > max): 
		max = ocurrencia; 
		index = i;

Moda = Bases[index];
print(f'La moda es = {Moda}')

#Troba si es asimetric:
  
if( index >  int(len(Ocurrencies)/2)): 
	print("Es asimetric a la l'esquerra")
else: 
	print("Es asimetric a dreta ")
	
#Metode alternatiu de trobar l'asimetria	
valorsEsquerra = index; 
valorsDreta = len(Ocurrencies) - index -1;

if( valorsEsquerra >  valorsDreta): 
	print("Es asimetric a la l'esquerra")
else: 
	print("Es asimetric a dreta ")


