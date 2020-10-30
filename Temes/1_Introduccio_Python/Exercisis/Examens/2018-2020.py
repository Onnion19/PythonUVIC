'''
Es vol fer un anàlisi de aigua respecte a la seva altura. Existeix una relació entre el pH i l’altura:
a mesura que disminueix l’altura augmenta el pH.
Es demana fer un programa on es vagin entrant dades del pH de l’aigua que s’analitza partint
d’una altura de 500 m. i pujant 100 m en cada analítica, ens digui en quina altura s’obté un pH
per sota de 6. Si s’arriba a una altura de 1600m, que es correspon al naixement de la font, indicar
que no s’arriba al pH per sota de 6.
'''

PH = float(input("entra els ph")); 

altura = 500; 

while(PH > 6.0 and altura < 1600): 
	altura = altura +100;
	PH = float(input()); 
	
if(PH < 6.0): 
	print(f'El ph esta per sota 6 a laltura de {altura}m'); 
else: 
	print("El Ph mai esta per sota de 6"); 
	
	
'''
Es demana fer un programa que rebi una seqüència formada per subseqüències de bases
delimitades per * acabada en + i que retorni la posició de la seqüència de bases amb més
percentatge de G.
No cal controlar seqüència buida i les bases que formen les seqüències són les definides (A, T,
G, C) i sempre donades en majúscula.
Per calcular el percentatge: total de G de la seqüència/ total bases seqüència * 100
'''

nucleotid = input("Entra la sequencia caracter a caracter\n"); 
#Dades per la millor sequencia
millorSequencia = -1; 
millorPercentatge = 0; 
#Dades per la sequencia actual
percentatgeSequenciaActual = 0.0
nucleotidsSequenciaActual = 0
G_SequenciaActual = 0
#Dades generals
numSequencies = 1

while(nucleotid != '+'): 
	
	if( nucleotid == '*'): #Nova sequencia
		#si la sequencia actual es millor que la "millor", actualtizar els valors de la millor
		if(percentatgeSequenciaActual > millorPercentatge): 
			millorSequencia = numSequencies; 
			millorPercentatge = percentatgeSequenciaActual; 
		
		#Actualitzem el nombre de sequencies trobades, i comencem a contar de 0
		numSequencies = numSequencies +1; 
		percentatgeSequenciaActual = 0.0;
		G_SequenciaActual = 0;
		nucleotidsSequenciaActual = 0;
		
		
	else: 
		#actualitzem els nucleotids de la sequencia
		nucleotidsSequenciaActual = nucleotidsSequenciaActual +1; 
		
		#Si es una G actualitzem el percentatge de la sequencia
		if( nucleotid == 'G'): 
			G_SequenciaActual = G_SequenciaActual +1; 
			percentatgeSequenciaActual = G_SequenciaActual / nucleotidsSequenciaActual;
			
	nucleotid = input(); 

print(f'La millor sequencia es la {millorSequencia} amb un {millorPercentatge}%');
		
		
		
		