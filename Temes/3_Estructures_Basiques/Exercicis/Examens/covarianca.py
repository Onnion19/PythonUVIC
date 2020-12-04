'''
Fer un programa que permeti entrar dues cadenes: una cadena de valors
numèrics corresponents a dies de pluja a la ciutat de Vic i una altra amb la
quantitat de contaminació associada a cadascun dels dies.
Un cop entrada aquesta informació es vol que mostri el resultat que permet
veure la relació entre aquests valors i que es correspon a la covariança
'''


'''
Metode 1
'''

cadenaA = input("EntraCadena A\n").split(); 
cadenaB = input("EntraCadena B\n").split(); 

#Calcular el sumatori
Sumatori = 0; 
for i in range(len(cadenaA)): 
	Sumatori = Sumatori + int(cadenaA[i]) * int(cadenaB[i]);

Sumatori = float(Sumatori) / len(cadenaA); 	

#Calcular la mitjana
mitjanaA = 0
mitjanaB = 0
for i in range(len(cadenaA)): 
	mitjanaA = mitjanaA + int(cadenaA[i])
	mitjanaB = mitjanaB + int(cadenaB[i])
	
mitjanaA = float(mitjanaA)/len(cadenaA)
mitjanaB = float(mitjanaB) / len(cadenaB)

covarianca = Sumatori - mitjanaA*mitjanaB; 


print(f'Covariansa = {covarianca}');


'''
Metode 2 Nomes un loop
'''
cadenaA = input("EntraCadena A\n").split(); 
cadenaB = input("EntraCadena B\n").split(); 

Sumatori = 0; 
mitjanaA = 0
mitjanaB = 0
for i in range(len(cadenaA)): 
	Sumatori = Sumatori + int(cadenaA[i]) * int(cadenaB[i]);
	mitjanaA = mitjanaA + int(cadenaA[i]);
	mitjanaB = mitjanaB + int(cadenaB[i]);

Sumatori = float(Sumatori) / len(cadenaA); 	
mitjanaA = float(mitjanaA)/len(cadenaA);
mitjanaB = float(mitjanaB) / len(cadenaB);

covarianca = Sumatori - mitjanaA*mitjanaB; 


print(f'Covariansa = {covarianca}');