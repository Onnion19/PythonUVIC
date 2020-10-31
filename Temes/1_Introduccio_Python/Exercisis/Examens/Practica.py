'''
El programa ha de calcular quina és la població que la mitjana de les mesures és la
millor (inferior) i quina és la pitjor (superior). Per fer aquest càlcul es descartaran les
poblacions que en alguna mesura hagin superat el límit permès. També volem que
s’informi de quines poblacions han estat descartades per mesures no permeses. En el
moment que una població entri una dada superior al llindar ja s’avisa i es passa a la
següent població

'''

#Delcaracio variables
llindar = int(input("Entra el llindar "))
nomPoble = input("Entra el nom del poble ")

MitjanaMax = -1
PobleMax = ""
MitjanaMin = llindar
PobleMin = ""

#Llegir pobles
while(nomPoble != '*'):
	comptadorMesura = 0;
	MitjanaActual = 0;
	mesura = int(input("Entra la mesura "));
	
	#Llegir mesures del poble
	while(mesura != -1 and mesura <= llindar):
		comptadorMesura = comptadorMesura +1; 
		MitjanaActual = MitjanaActual + mesura;
		
		mesura = int(input("Entra la seguent mesura "))
	
	#Calcul mitjana
	if(mesura == -1):
		MitjanaActual = MitjanaActual / comptadorMesura;
		#Actualitzar mitjanes si s'escau
		if(MitjanaActual > MitjanaMax): 
			MitjanaMax = MitjanaActual;
			PobleMax = nomPoble;
		if(MitjanaActual < MitjanaMin): 
			MitjanaMin = MitjanaActual;
			PobleMin = nomPoble;
			
			
	else: #Poble descartat
		print(f'El poble {nomPoble} te una dada superior al llindar {mesura}'); 
		MitjanaActual = -1; 

		
	nomPoble = input("Entra el nom del seguent poble ")

print(f'La poblacio amb millors valors es {PobleMin} amb una mitjana de {MitjanaMin}');
print(f'La poblacio amb pitjors valors es {PobleMax} amb una mitjana de {MitjanaMax}');		