def AmmountOf( DinersInicials,  DividitPer, Text): 
	dividend =  int(DinersInicials/DividitPer); 
	print(f'{Text} {DividitPer}:{dividend}')
	return DinersInicials - int(dividend * DividitPer); 

Diners = int(eval(input("Entra un valor de diners\n")))
DividirPer = [500,200,100,50,20,10,5,2,1]

for valor in DividirPer: 
	Diners = AmmountOf(Diners, valor, "\tBittlets de ");