'''

Disposem de tres fitxers:
El primer (fitxercodificacio.txt) conté una codificació d’aminoàcids amb el següent format:
A GCU GCC GCA GCG
D GAU GAC
Q CAA CAG
N AAU AAC
R CGU CGC CGA CGG AGA AGG
...

El segon és un fitxer amb format FASTA que conté un una primera línia amb la descripció de la
codificació seguida per una seqüència de línies que contenen una seqüència d’ARN.
Exemple: (fitxerbases.fasta)
>ENSG00000128573|ENST00000393495
AUG AUG CAG GAA UCU GCG ACA GAG ACA AUA AGC AAC AGU UCA AUG AAU CAA AAU GGA AUG 
AGCACUCUAAGCAGCCAAUUAGAUGCUGGCAGCAGAGAUGGAAGAUCAAGUGGUGACACC
AGCUCUGAAGUAAGCACAGUAGAACUGCUGCAUCUGCAACAACAGCAGCAGCAGCAGCAG
CAGCAGCAGCAACAGCAAUUGGCAGCCCAGCAGCUUGUCUUCCAGCAGCAGCUUCUCCAG
AUGCAACAACUCCAGCAGCAGCAGCAUCUGCUCAGCCUUCAGCGUCAGGGACUCAUCUCC
AUUCCACCUGGCCAGGCAGCACUUCCUGUCCAAUCGCUGCCUCAAGCUGGCUUAAGUCCU
GCUGAGAUUCAGCAGUUAUGGAAAGAAGUGACUGGAGUUCACAGUAUGGAAGACAAUGGC
AUUAAACAUGGAGGGCUAGACCUCACUACUAACAAUUCCUCCUCGACUACCUCCUCCAAC
ACU UCC AAA GCA UCA CCA CCA AUA ACU CAU C

Es demana fer un programa usant funcions en PYTHON on es calculi el biaix de codó:
Per cada aminoàcid donar el percentatge d’utilització de cada codó en la codificació i quantes
vegades apareix.
Exemple:
A : GCU – 3 - 33,33%
GCC – 1 - 11,11%
GCA – 4 - 44,44%
GCG – 1 - 11,11%
D : GAU – 2 - 40%
GAC – 3 - 60%
Q : CAA – 10 – 27,77%
CAG – 26 – 72,22%
'''


#Aquesta practica estarà dividida en 3 parts: 
# 	1- Crear un diccionari amb els codols 
#	2- Carrergar el fitxer a descodificar i preparar-lo 
#	3- Comprovar els codols que hi ha dins el fitxer descodificat. 


#Funcions

## Llegeix una linia del fitxer de codols i l'afegeix al diccionari indicat. 
def LLegirCodol_AfegirDiccionari(linia, diccionari): 

	aux = linia.split(); 
	if(len(aux) >= 2): 
		clau = aux[0]; 
		valor = aux[1:]; 
		
		diccionari.update({clau : valor}); 
		
	return diccionari; 

## Mostra el contingut d'un diccionari de forma llegible 
def MostrarDiccionari(diccionari): 
	for x,y in diccionari.items(): 
		print(f'{x} --> {y}');
		

##Donat un codol busca al diccionari de codols quin aminoacid li correspon		
def TrobarAminoacid(diccionari, codol): 

	aminoacid = None; 
	for clau,valor in diccionari.items(): 
		if codol in valor: 
			aminoacid = clau; 	
		
	return aminoacid; 
	
##Actualitza el diccionari d'aminoacids incrementant en 1 la ocurrencia. 	
def ActualitzarAminoacid(diccionari, aminoacid, codol): 
	if not aminoacid in diccionari: 
		diccionari[aminoacid] = {}; 
	
	if codol in diccionari[aminoacid]: 
		diccionari[aminoacid][codol] += 1; 
	else: 
		diccionari[aminoacid][codol] = 1

def CalcularPercentatges(diccionari): 
	for aminoacid , codols in diccionari.items(): 
		total = 0
		for codol , ocurrencia in codols.items(): 
			total += ocurrencia; 
		print(f'Aminoacid: {aminoacid}');	
		for codol , ocurrencia in codols.items():
			percentatge = ocurrencia*100.0/total;
			print(f'\t {codol}--> {ocurrencia} = {round(percentatge,2)} %');

#Part 1: 
FitxerCodols = open("fitxercodificacio","r"); 
dicCodols = {}
for linia in FitxerCodols:
	LLegirCodol_AfegirDiccionari(linia,dicCodols); 
FitxerCodols.close(); 
	
#MostrarDiccionari(dicCodols);
 
	
#Part 2: 
FitxerSequencia = open("fitxerbases.fasta","r"); 
FitxerSequencia.readline(); 
dicAminoacids = {}

for line in FitxerSequencia: 
	for index in range(0,len(line)-2,3): #Recordar que les cadenes tenen 1 caracter extra (\n)
		Codol = line[index:index+3]
		aminoacid = TrobarAminoacid(dicCodols,Codol);
		if(aminoacid!= None): 
			ActualitzarAminoacid(dicAminoacids, aminoacid,Codol); 

#Part3:
#MostrarDiccionari(dicAminoacids);

CalcularPercentatges(dicAminoacids);
















