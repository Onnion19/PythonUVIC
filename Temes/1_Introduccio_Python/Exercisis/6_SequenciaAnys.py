'''
Fer un programa que donada una seqüència d’anys acabada en 0 ens digui quants n’hi
ha del segle 20.
'''

any = int(input("Entra any: "));
S20 = 0; 
while (any): 
	if(any > 1900 and any < 2001): 
		S20 = S20 +1; 
		
	any = int(input("Entra any: "));
	
	
print (f'Has entrat {S20} anys dins del segle 20'); 



