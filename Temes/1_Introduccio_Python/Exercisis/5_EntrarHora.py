'''
Fer un programa que donada una hora, un minuts i uns segons, li sumi un segon i
retorni el resultat en format horari correcte.
'''

''' 
CODI ALTERNATIU: 
hora = int(input("entra hora: "))
minuts = int(input("entra minuts: "))
segons = int(input("entra segons": ))
'''  

#Entrada de dades
hora , minuts, segons = input("Entra una hora en el format hh:mm:ss\n").split(":"); 

#Convertir a enters
hora = int(hora); 
minuts = int(minuts); 
segons = int(segons); 


#Sumar un segon
segons = segons +1; 

#Normalitzar la hora (si el segons > 100, min +1. si min > 60 , hora +1) 

#1. Comprovar si ens passem del limit amb la divisio entera
minuts = minuts + int(segons/100); 
hora = hora + int(minuts/60); 

#2. Arrodonir el valor entre 0 -  99 i 59 pels segons i minuts. 
segons = segons%100; 
minuts = minuts%60; 


print(f'La nova hora es: {hora}:{minuts}:{segons}'); 




