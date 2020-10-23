'''
Fer un programa que donades 10 mesures fetes a laboratori ens digui quantes n’hi ha
que estiguin entre l’ interval 0.9 i 1
'''


#Metode 1
print("Metode 1: doble iteracio\n"); 
list = []
for i in range(0,10): 
	list.append( float(input("Entra una nova mesura:\t"))); 
	
dinsRang = 0; 
for mesura in list: 
	if(mesura >= 0.9 and mesura <=1): 
		dinsRang = dinsRang+1; 

print(f'Hi ha {dinsRang} mesures dins del rang'); 



#Metode 2
print("\n\nMetode 2: Una sola iteracio \n"); 
dinsRang = 0; 
for i in range(0,10): 
	mesura = float(input("Entra una nova mesura:\t")); 
	if(mesura >= 0.9 and mesura <=1): 
		dinsRang = dinsRang+1; 

print(f'Hi ha {dinsRang} mesures dins del rang'); 

