'''
1.	Cada 5 minuts ens passen la concentració d’organismes d’un cultiu que està en creixement. 
Es demana fer un programa que ens digui en quin moment deixa de créixer la concentració, 
quina és la concentració màxima i quina és la velocitat de creixement.
'''

#Mesura actual i mesura anterior
mesura = float(input("Entra la mesura\n"));
mesuraAnterior = mesura -1; 

#Mesura Inicial i final: 
mesuraInicial = mesura; 
mesuraFinal = mesura; 

#Contador de mesures
numMesures = 1 #Comença a 1 perque ja hem llegit una mesura al principi de tot

while(mesura > mesuraAnterior): 

	mesuraFinal = mesura; 
	mesuraAnterior = mesura;
	mesura = float(input("Entra la mesura\n"));
	
	#Si la mesura es valida, augmentem el comtpador de mesures. (no ens interesa sumar una mesura no valida)
	if(mesura > mesuraAnterior):
		numMesures = numMesures +1;
	
	



velocitatCreixement = (mesuraFinal - mesuraInicial) / (numMesures * 5); 
print(f'Sestabilitza al minut {numMesures *5}');
print(f'La concentracio maxima es {mesuraFinal}');
print(f'La velocitat es de {velocitatCreixement}');



'''

2.	Per tal de poder dur a terme una reacció és necessita un mínim de temperatura. 

Es demana fer un programa que permeti entrar una temperatura mínima llindar,
després  una sèrie de temperatures acabada en -1 i 
ens digui quin és el valor més gran de totes les que estiguin per sota del llindar.


Se'ns assegura que la seqüència no és buida i que el primer valor és menor que el llindar.

'''


#Variables de control
llindar = int(input("Entra el llindar \n")); 
mesura = int(input("Entra les mesures\n")); 

#Variable mes propera al llindar
mesuraPropera = 0; 

while(mesura != -1): 
	
	if(mesura < llindar): 
		#Calculem la diferencia entre el llindar i les mesures (Aka delta)
		DeltaMillor = llindar - mesuraPropera; 
		DeltaActual = llindar - mesura; 
		#Si la mesura actual es millor que la "millor" actualitzem les dades
		if( DeltaActual < DeltaMillor): 
			mesuraPropera = mesura; 
			
	#Llegim la seguent mesura		
	mesura = int(input()); 
	
print(f'La mesura mes propera es {mesuraPropera}'); 












