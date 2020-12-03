'''
Fer un programa que donada una seqüència de 30 nucleòtids ens compti quantes
vegades apareix la tripleta TAG. 
'''

comptador = 0;
nucleotidAnterior = '7'
nucleotidReAnterior = '7'

for i in range(30):
	nucleotid = input("entra nucleotid") 

	if (nucleotidReAnterior == 'T' and nucleotidAnterior == 'A' and nucleotid == 'G'): 
		comptador = comptador +1; 
	
	
	nucleotidReAnterior = nucleotidAnterior; 
	nucleotidAnterior = nucleotid;
	
print (f'Trobats {comptador}');