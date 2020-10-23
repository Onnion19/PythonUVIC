'''
Fer un programa que donada una seqüència de nucleòtids acabada en * ens compti
quants n’hi ha de Timina.
'''


#Metode 1
print("Metode 1: Funcions de string\n"); 
sequencia = input("Entra la sequencia\n"); 
num_T = sequencia.split('T'); 
print(f'Hi ha {len(num_T)-1} Timina'); 




print("\n\nMetode 2: Iteracio de cadenes\n"); 
#Metode 2
sequencia = input("Entra la sequencia\n"); 
num_t = 0; 
for i in sequencia: 
	if(i == 'T' or i == 't'): 
		num_t = num_t +1; 
		
print(f'Hi ha {num_t} Timina'); 



print("\n\nMetode 3: Caracter a caracter \n"); 
#Metode 3
print("Entra caracter a caracter la sequencia\n"); 
caracter = input(); 
num_t = 0; 
while(caracter != '*'): 
	if(caracter == 'T' or caracter == 't'): 
		num_t = num_t +1; 
	caracter = input();

print(f'Hi ha {num_t} Timina'); 

