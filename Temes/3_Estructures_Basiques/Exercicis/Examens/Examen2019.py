'''


4. (0.75 punts)
Fer una funció anomenada codons(c) que rebi per paràmetre una cadena de bases
c, i retorni una llista amb els codons que es formen amb ella.

6. ( 1 punt)
Fer una funció anomenada pos(c1,c2) que rebi per paràmetre dues cadenes c1 i
c2, i retorni una llista amb les posicions on els valors de les dues cadenes no
coincideixen.
7. ( 4 punts)
Es demana fer un programa que usant les funcions anteriors permeti:
a. Rebre el nom de 3 fitxers :
i. El primer, un fitxer fasta, corresponent a un tros DNA d’un individu
concret d’una espècie.
ii. El segon, un fitxer fasta, corresponent a la traducció a aminoàcid del
mateix tros de DNA anterior, però de l’espècie en general.

iii. El tercer fitxer, un fitxer que té una línia de capçalera i la resta
contenen el símbol d’un aminoàcid i el codó que el codifica.

b. Com a resulta retorni:
i. Individu sense mutació, si la traducció del tros de DNA de l’individu
concret es correspon a la cadena d’aminoàcids de l’espècie.
ii. O bé, individu amb mutació en cas contrari. Llavors si es dóna aquesta
situació cal saber en quina posició es troben els aminoàcids que no es
corresponen als de l’espècie en general.

Exemple:
Fitxer1.fasta Fitxer2.fasta
&gt;Individus345324 HomoSapiens &gt;HomoSapiens code EN245COD1231
AUGAUGCAGGAAUCUGCGACAGAGA MMQESATETISNSSMN
CAAUAAGCAACAGUUCAAUGAAU

Fitxer3.txt
AMINO CODO
A GCU
A GCC
A GCA
R CGU
R CGC
N AAU
D GAU
:
:

En aquest cas la resposta seria Individu sense mutació perquè la
traducció del fitxer1.fasta a aminoàcids és idéntica a la de l’espècie.
'''


##Part 1: 
'''
(1 punt)
Fer una funció anomenada llegir() que demani el nom del fitxer que es vol llegir i
retorni una llista amb totes les línies del fitxer menys la primera.
'''

def llegir(): 
	nomFitxer = input("Entra el nom del fitxer\n"); 
	llista = []
	
	fitxer = open(nomFitxer , "r"); 
	fitxer.readline(); ## Eliminar la primera linia 
	
	for linia in fitxer: 
		llista.append(linia); 
		
	return llista; 


##Part 2
'''
2. (1 punt)
Fer una funció anomenada dic_codo(l) que rebi per paràmetre una llista l, on
cada element es una parella de valors amino codó, i retorni un diccionari amb clau
codó i valor amino.
'''

def dic_codo(llista): 
	diccionari = {}; 
	
	for element in llista: ## Elements = [A GCU, R CAU]
		contingut = element.split(); ##["A",GCU]
		valor = contingut[0]; 
		clau = contingut[1];
		diccionari[clau] = valor; 
		
	return diccionari; 


'''
3. ( 0.75 punts)
Fer una funció anomenada l_cad(l) que rebi per paràmetre una llista l, on cada
element de la llista és una cadena acabada amb \n, i retorni una cadena que es
correspongui a la unió de totes les cadenes de la llista inicial havent eliminat \n
'''
##Metode 1
def l_cad(llista): 
	cadena = ""; 
	for element in llista: #element = "sdiofjuewioafoafi\n" --> "sdiofjuewioafoafi"
		contingut = element[:len(element)-1]; ## "a" --> Len = 1 //"sdoifaj\n" --> Len 8 -1
		cadena = cadena + contingut; 

	return cadena; 

##Metode 2
def l_cad2(llista):
	cadena = ""; 
	for element in llista: #element = "sdiofjuewioafoafi\n" --> "sdiofjuewioafoafi"
		contingut = element.split('\n'); ## ["sdiofjuewioafoafi"]
		cadena = cadena + contingut[0]; 
		
	return cadena; 
 


'''
5. (1.5 punts)
Fer una funció anomenada trad_a(l,d), que rebi per paràmetre una llista l i un
diccionari d, on els elements d’l són codons i d es correspon a un diccionari amb clau
codó i valor aminoàcid, retorni una cadena corresponent a la traducció dels codons a
aminoàcids.
'''
## Llista --> ["GCU , "CAU" , GAU"...]
## Diccionari --> { GCU: A, CAU: T, ... }

def trad_a(llista,diccionari):
	cadena = "";
	for element in llista:
		aminoacid = diccionari[element]; ##diccionari[element] diferencia si clau no existeix
		cadena = cadena + aminoacid; 

	return cadena; 
	
	
l = ["GCU", "CAU", "GAU"]; 
d = {"CAU": "B"  , "GCU": "A", "GAU":"C"}; 
