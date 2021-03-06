'''

g. Es demana fer un programa permeti llegir dos fitxers f1.txt i f2.txt que tenen
l’estructura:
f1.txt f2.txt
codi pob 17800 5 7 2 -1 4 -3
17800 Olot 17500 2 3 7 0 -1
08500 Vic 08500 -2 3 5 -2 -3 -1 2
08570 Torelló
17500 Figueres : :
: :
on en f1.txt hi ha la relació entre codi postal de població i el nom de la població,
i en f2.txt per cada línia tenim el codi de la població i un conjunt de
temperatures que s’han mesurat.
Un cop llegits aquests dos fitxers cal que el programa mostri per cada població
el seu nom, els valors positius, els valors negatius, el percentatge de valors
positius sobre el total, el percentatge de valors negatius sobre el total i la
mitjana de temperatures.
Seguint l’exemple dels fitxers, el resultat seria:
Olot
Valors positius 5 7 2 4
Valors negatius -1 -3
Percentatge positius: 66.67%
Percentatge negatius: 33.33%
Mitjana temperatura: 2.33

Figueres
Valors positius 2 3 7
Valors negatius -1
Percentatge positius: 60%
Percentatge negatius: 20%
:
:
'''


##Part 1
'''
a.Es demana fer una funció que rebi com a paràmetre una llista i retorni quantes
vegades ha tingut valors negatius. Aquesta funció s’anomenarà negatiu(l).
exemple llista: [5,4,3,-5,7,-1,0,-4]
'''

def negatiu(llista): 
	contador = 0; 
	for element in llista: 
		if( element < 0): 
			contador = contador + 1;
	
	return contador; 


##Part 2
'''
b. Es demana fer una funció que rebi per paràmetres una llista i un caràcter, i
retorni una llista només amb els valors positius de la primera si el caràcter
rebut és un +, o una llista amb els valors negatius de la primera si el caràcter
rebut és un -. Aquesta funció s’anomenarà tria(l,c).

exemple--> [5,4,3,-5,7,-1,0,-4] , '+' --> [5,4,3,7,0]
'''

def tria(llista,caracter): 
		
	contingut = []
	for element in llista: 
		if(caracter == '+' and element >= 0): 
			contingut.append(element);			
		elif (caracter == '-' and element < 0): 
			contingut.append(element);

	return contingut; 
	
	
##Part3
'''
c. Es demana fer una funció que rebi com a paràmetre el nom d’un fitxer i retorni
una llista amb el seu contingut. Aquesta funció s’anomenarà llegir(nom)
'''

def llegir(nom): 
	contingut = []
	fitxer = None; 
	try: 
		fitxer = open(nom,"r"); 	
	except:  
		print("Nom de fitxer invalid"); 
		return contingut; 
		
	for linia in fitxer: 
		contingut.append(linia);
		
	return contingut; 

##Part4
'''
d. Es demana fer una funció que rebi com a paràmetre una llista i retorni la
mitjana dels seus valors. Aquesta funció s’anomenarà mitjana(l).
exemple llista: [5,4,3,-5,7,-1,0,-4] --> mitjana 
'''

def mitjana(llista): 
	mitjana = 0;
	sumatori = 0;
	for element in llista: 
		sumatori += element; # sumatori = sumatori + element
	
	mitjana = sumatori / len(llista); 
	return mitjana; 
	
##Part 5
'''
e. Es demana fer una funció que rebi com a parametre una llista de valors que no
són numèrics i retorni una llista amb els mateixos valors que la inicial però
passats a real. Aquesta funció s’anomenarà pasreal(l).
exemple = ['6','5','8','-5','5.34'] --> [6,5,8,-5,5.34]
'''
def pasreal(llista): 
	contingut = []
	for element in llista: 
		contingut.append( float(element)); 
	
	return contingut; 
 
 ##Part6
'''
 f. Es demana una funció que rebi com a paràmetre una llista tipus:
[codi pob, codi pob,codi pob,....] i retorni un diccionari on la clau de cada
element sigui el codi i el valor pass¡ociat sigui la població. Aquesta funció
s’anomenarà dicc(l).

exemple -> ["065 Vic" , "493 Barcelona" , ...] -->
			{065 : "Vic" , 493: "Barcelona"}
'''
def dicc(llista): 
	diccionari = {};
	
	for element in llista: ## element -> "065 Vic"
		Parella = element.split(); ##Parella = ["065" , "Vic"]
		clau = int(Parella[0]);##clau = 065
		valor = Parella[1]; ## "Vic"
		diccionari[clau] = valor; ## {065 : "Vic"}
	
	return diccionari; 
 
 ##Part 7
'''
 g. Es demana fer un programa permeti llegir dos fitxers f1.txt i f2.txt que tenen
l’estructura:
f1.txt: 
codi_postal Poblacio

f2.txt 
codi_postal 4 3 2 5 4 2 4 5
on en f1.txt hi ha la relació entre codi postal de població i el nom de la població,
i en f2.txt per cada línia tenim el codi de la població i un conjunt de
temperatures que s’han mesurat.
Un cop llegits aquests dos fitxers cal que el programa mostri per cada població
el seu nom, els valors positius, els valors negatius, el percentatge de valors
positius sobre el total, el percentatge de valors negatius sobre el total i la
mitjana de temperatures.
Seguint l’exemple dels fitxers, el resultat seria:
Olot
Valors positius 5 7 2 4
Valors negatius -1 -3
Percentatge positius: 66.67%
Percentatge negatius: 33.33%
Mitjana temperatura: 2.33

Figueres
Valors positius 2 3 7
Valors negatius -1
Percentatge positius: 60%
Percentatge negatius: 20%
:
:
'''
def CrearDiccionariTemperatures(llista): 
	diccionariTemperatures = {}
	for element in llista: 
		contingut = element.split(); ##["065","4","3","2","-4"]
		clau = int(contingut[0]);
		valor = pasreal(contingut[1:]);
		diccionariTemperatures[clau] = valor; 
		
	return diccionariTemperatures;


##Llegir poblacions i temperatures
##Poblacions: 
llistaPoblacions = llegir("f1.txt"); ##["065 Vic", "493 barcelona" , ...]
diccionariPoblacions = dicc(llistaPoblacions); ##{065: "Vic", 493 :"barcelona"}

##Temperatures
llistaTemperatures = llegir("f2.txt"); ["065 4 3 2 -4", "493 8 19 0 3"]
diccionariTemperatures = CrearDiccionariTemperatures(llistaTemperatures);

for codiPostal, poblacio in diccionariPoblacions.items(): 
	##Mostrar poble o codipostal
	print(f'{poblacio}: {codiPostal}');
	##Agafem els valors temperatures
	llistatValors = diccionariTemperatures[codiPostal];
	
	##Triem els positius
	valorsPositius = tria(llistatValors,'+');
	##Triem els negatius
	valorsNegatius = tria(llistatValors, '-'); 
	##Mostrar temperatures
	print(f'Positius = {valorsPositius}');
	print(f'Negatius = {valorsNegatius}');
	
	##Mostrar Mitjanes 
	PercentatgePositius = 100*len(valorsPositius)/len(llistatValors); 
	PercentatgeNegatius = 100*len(valorsNegatius)/len(llistatValors); 
	print(f'Mitjana Positius = {PercentatgePositius}');
	print(f'Mitjana Negatius = {PercentatgeNegatius}');
	##Calcul de la mitjana
	Mitjana = mitjana(llistatValors); 
	print(f'Mitjana = {Mitjana}');
	print("----");