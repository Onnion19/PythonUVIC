'''
Donada una cadena de bases (A, T, C, G), calcular el percentatge de T que es troben
després d’una A i el percentatge de G que es troben després d’una C .
Exemple: ATTCGCGAGCTATACCCTGCGA
% de T després d’A : 40
% de G després de C : 60
'''


cadena = input("Entra la cadena\n");

cadena.upper();

CadenaA = cadena.split('A'); #Aqui tenim totes les subcadenes que comencen per A
CadenaC = cadena.split('C'); #Aqui tenim totes les subcadenes que comencen per C
CadenaT = cadena.split('T'); #Aqui tenim totes les subcadenes que comencen per T
CadenaG = cadena.split('G'); #Aqui tenim totes les subcadenes que comencen per G

numT = len(CadenaT) -1
numG = len(CadenaG) -1

numAT = 0
numCG = 0

for subcadena in CadenaA:	
	if(len(subcadena)>0 and subcadena[0] == 'T'):
		numAT = numAT +1;
		
		
for subcadena in CadenaC:	
	if(len(subcadena)>0 and subcadena[0] == 'G'):
		numCG = numCG +1;	
	
print(f"%T= {numAT/numT} %G= {numCG/numG}\n=======\n");

'''
Ens donaran una cadena. En aquesta cadena hi trobarem cadenes de bases separades
per *. Es demana un algorisme que ens digui quantes cadenes hi ha que comencin i
acabin per les mateixes bases que l’última.
Exemple:
ATTAG*ATTGCT*ATTTCGCG*TTATT*GATTG*CTTAA*AG*ACGTG* 
'''
print("\n\nExercici 2\n\n");

#Versio llistes (pop?)

cadena = "*ATTAG*ATTGCT*ATTTCGCG*TTATT*GATTG*CTTAA*AG*ACGTG*"
subcadenes = cadena.split('*');

UltimaCadena = subcadenes.pop();
UltimaCadena = subcadenes.pop();

PrimeraLletra = UltimaCadena[0]; 
UltimaLletra = UltimaCadena[len(UltimaCadena)-1]; #'CGG' llargada=4 pos max = 3

numTrobats = 0
for subcadena in subcadenes: 
	if(len(subcadena)>1):
		if(subcadena[0]==PrimeraLletra   and subcadena[len(subcadena) -1] == UltimaLletra):
			numTrobats= numTrobats +1;

print(f'El nombre de trobats es = {numTrobats}');




