''' 
 
 1 - Tenim dos fitxer "Compost.txt" i "Reaccions.txt" 
	on el compost.txt te el seguent format.
	
		clau 			Valor
	FormulaOrganica   nom comu 
		CH4				meta
	
	Fitxer "reaccions:" 
	
	FromulaOrganica gr_compost   gC02alliberats   gH20alliberada
		C2H2 			100g		 230g				70g 	

2- Llegir el fitxer compost i crear el diccionari apropiat 
3- L'usuari ha d'introduir els grams que vol reaccionar 
4- Cal trobat quin es el compost que genera menys CO2 
	amb els grams introduits per l'usuari
'''

##Part 1:
def LlegirFitxerIPassarLlista(nomFitxer): 
	##Llegira un fitxer i passara el seu contingut a una llista
	llista = []; 
	fitxer = None; 
	try: 
		fitxer = open(nomFitxer, "r"); 
	except:
		print("Ei que el fitxer no existeix"); 
	
	
	for linia in fitxer: 
		contingut = linia.split('\n'); ## contingut = [linia1 ,""]
		llista.append(contingut[0]); 
		
	return llista; ##llista [linia 1 , linia2, linia3, ...]
		
		
def CrearDiccionariCompostos(nomFitxer): 
	contigutFitxer = LlegirFitxerIPassarLlista(nomFitxer); 
	diccionari = {}
	for linia in contigutFitxer: 
		##linia = "C2H2 patata"
		contingut = linia.split();
		clau = contingut[0];
		valor = contingut[1];
		diccionari[clau] = valor; 
	return diccionari; 
	
##Part 2 
'''
L'usuari ha d'introduir els grams que vol reaccionar. 
Fer funcio DemanarGrams() que retornara els grams entrat per l'usuari. 
'''

def DemanarGrams(): 
	return int(input("Entra els grams a reaccionar\n")); 

##Part3 
'''
Diccionari Reaccions 

Diccionari reaccions: 
	clau 		valors 
	grams 		[gramsCo2 , gramsH2O]

Diccionari reaccionsCompost
	clau 					valor 
Compost Organic 		diccionari de reaccions
	C2H6						{100: [330, 65], 50: [40, 23]}
'''
##funcio LlegirFitxerIPassarLlista() --> llegir fitxer 
##funcio CrearDiccionariReaccionsCompost
##funcio ActualitzarDiccionariReaccions

def ActualitzarDiccionariReaccions(diccionariReaccions, llistaGrams): 
	##llistaGrams: ["100", "233", "43"];
	if( diccionariReaccions == None): 
		diccionariReaccions = {};
	clau = int(llistaGrams[0]); 
	valor = [int(llistaGrams[1]) , int(llistaGrams[2])];
	diccionariReaccions[clau] = valor; 
	
def ActualitzarDiccionariReaccionsCompost(diccionariReaccioCompost, informacio): 
## informacio = ["C2H6 100 534 23"]
	contingut = informacio.split(); ## contingut = ["C2H6", "100" , "534", "23"]
	clau = contingut[0]; 
	diccionari = diccionariReaccioCompost[clau]; 
	if(len(diccionari) == 0): 
		diccionariReaccioCompost[clau] = ActualitzarDiccionariReaccions(None, contingut[1:]);
	else: 
		diccionariReaccioCompost[clau] = ActualitzarDiccionariReaccions(diccionari, contingut[1:]);


DiccionariComposts = CrearDiccionariCompostos("composts.txt"); 
DiccionariReaccions = {}; 
reaccions = LlegirFitxerIPassarLlista("reaccions.txt"); 
for reaccio in reaccions: 
	ActualitzarDiccionariReaccionsCompost(DiccionariReaccions, reaccio); 
	## C6H6 100 338,46 69,23
	
	
grams = DemanarGrams(); 

minReactiu = ""; 
minQuantitat = 9999999; 
for compost, reaccio in DiccionariReaccions.items(): 
	if(grams in reaccio): 
		gramsC0 = reacio[grams][0];
		if(gramsC0 < minQuantitat): 
			minQuantitat = gramsC0; 
			minReactiu = compost; 
			
print(f'El millor reactiu es {minReactiu} amb {minQuantitatç}'); 