'''
Donat un valor enter positiu que representa una quantitat de segons, fer un
programa que calculi l’equivalent expressat en dies, hores, minuts i segons.
'''

segons = int(input("Entra els segons\n")); 


#calcular minuts
#1. Trobar el nombre de minuts que hi ha: 
minuts = int(segons/60); 
#2. Restar aquests minuts dels "segons" 
segons = segons%60; 

#Calcular hores: 
#1. Trobar el nombre d'hores que hi ha segons els minuts: 
hores = int(minuts/60); 
#2. Restar aquestes hores dels "minuts" 
minuts = minuts%60; 

#Calcular dies: 
#1. Trobar el nombre de dies que hi ha segons les hores: 
dies = int(hores/24); 
#2. Restar els dies de les hores
hores = hores%24; 

print(f'{dies} dies, {hores} hores , {minuts} minuts  i {segons} segons'); 



'''
Donat un número enter positiu es demana fer un programa que digui si és
màgic. Un número és màgic si la suma des de 1 fins a la meitat del número dóna el
número.
'''

numero = int(input("Entra un numero")); 
sumatori = 0;
index= 0;

while(index <= numero/2): 
	sumatori = sumatori + index; 
	index = index +1; 
	
if(sumatori == numero): 
	print(f'{numero} es magic'); 
else: 
	print(f'{numero} no es magic'); 
	

'''
Donada una seqüència de valors enter positius acabada en -1 formada per
subseqüències delimitades per 0, fer un programa que ens digui quina posició ocupa la
subseqüència que té més valors parells (cal controlar la seqüència buida).
'''

numero = int(input("Entra els numeros d'un en un\n")); 
sequenciesTrobades = 1; 
#Necessitem guardar la millor de totes
millorSequencia = -1; 
numParellsMillorSequencia = -1; 
#I tambe l'actual
numParellsSequenciaActual = 0; 

while(numero != -1): 

	if(numero == 0): #Cas que trobem un 0 aka el final d'una sequencia
		if(numParellsSequenciaActual > numParellsMillorSequencia): #Si la sequencia acabada té mes parells que la "millor"
			millorSequencia = sequenciesTrobades; #La millor sequencia ara es la que estavem processant
			numParellsMillorSequencia = numParellsSequenciaActual; #El maxim nombre de parells son els de la sequencia actual
			
		sequenciesTrobades = sequenciesTrobades +1; 
		numParellsSequenciaActual = 0; 
	elif(numero %2 == 0): #Si el numero es parell
		numParellsSequenciaActual = numParellsSequenciaActual+1; 
	
	numero = int(input()); 

print(f'La sequencia {millorSequencia} conte {numParellsMillorSequencia} parells'); 
		











	