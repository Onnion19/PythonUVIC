'''
Que es una cadena? 

Les cadenes son conjunts de caracters dins d'una mateixa variable. Es pot dir que es un vector de caracters: 

Caracter1 = 'h'
Caracter2 = 'o'
Caracter3 = 'l'
Caracter4 = 'a'

Tots aquests caracters formen la cadena "hola", per tant: 

cadena = "hola"
 '''
 
cadena = input("escriu la paraula: patata\n"); #Per exemple l'usuari entra la paraula 'patata'


#Cadena ara te el valor "patata", i esta format pels caracters p a t a t a 

#Podem veure-ho de la seguent manera: 

'''
Podem veure la cadena com un conjunt de "caixes" on a cada una d'elles hi ha un caracter. A mes cada caixa te un index associat: 

  0    1    2    3    4    5
 ---  ---  ---  ---  ---  ---  
| p || a || t || a || t || a |
 ---  ---  ---  ---  ---  ---  
 
 D'aquesta manera podem mirar quin valor te la caixa numero 'x'
 
 cadena[x] ens retornara el valor d'aquella caixa. 
'''

print("La caixa numero 2 te el caracter: ",cadena[2]); 


print("\n\n FUNCIO SPLIT \n");

#La funcio split (Important)

''' 
	La funcio split ens serveix per dividir una cadena en subcadenes en funcio d'un caracter. 
	Per exemple si tenim la seguent cadena: 
		3,71,5,20,-5 
	La podem seprar per comes (ja que tenim els numeros serparats per comes) amb la funcio split(',');
	el resultat sera un vector de cadenes: 
	
	cadena = 
		"3"
		"71"
		"5"
		"20"
		"-5"
		
	VIGILEM!! SEGUEIXEN SENT CARACTERS, SI VOLEM QUE SIGUIN NUMEROS HEM DE FER (INT)
'''

cadena = "3,71,5,20,-5 "
print(f"Cadena original{cadena}"); 
cadenaDividida = cadena.split(',');
print(f"Cadena trencada {cadenaDividida}")
