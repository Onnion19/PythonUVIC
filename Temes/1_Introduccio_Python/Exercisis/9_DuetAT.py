'''
Fer un programa que donada una seqüència de nucleòtids acabada en * ens compti
quants n’hi ha abans del duet AT.
'''


#Metode 1
print("Metode 1: Caracter a Caracter\n"); 

num = 0; 
caracter = input("Entra la sequencia caracter a caracter\n");
duetTrobat = False; 
ultimCaracter = '.'


while(caracter != '*' and not duetTrobat): 
	num = num+1; 
	duetTrobat = ultimCaracter == 'A' and caracter == 'T'; 
	
	ultimCaracter = caracter; 
	if(not duetTrobat): 
		caracter = input(); 

	
if(duetTrobat):
	num = num -2; #Recordem que tambe contem el duet AT dins del while, i per tant s'han de restar del comput total

print(f'Hi ha {num} nucleotids'); 


#Metode 2 
print("\n\nMetode 2: Cadenes \n"); 

cadena = input("Entra tota la sequencia"); 
duetTrobat = False; 
index = 0; 
num = 0; 

while(not duetTrobat and index < len(cadena)-1): 
	if(cadena[index] == '*'):
		break; 
		
	duetTrobat = cadena[index] == 'A' and cadena[index +1] == 'T'
	index = index +1; 
	if(not duetTrobat): 
		num = num +1; 
		
print(f'Hi ha {num} nucleotids'); 