import csv

def leerArchivo_PA(nombreArchivo):
    with open(nombreArchivo, 'r') as archivo:
        lector = csv.reader(archivo)
        firstline = next(lector)
        
        ''' Obtenga	todos los vestidos que	
            tiene	una	puntuación	>	0,	
            a	continuación, 
            e imprima	la calificación	promedio de	estos vestidos.
        '''
        suma = 0
        cont = 0
        print(f'{firstline[1]} {firstline[2]} {firstline[3]}')
        for linea in lector:
            if float(linea[3]) > 0:
                print(linea[0], linea[1], linea[2], linea[3])
                suma += float(linea[3])
                cont += 1  
        print(f'{firstline[1]} {firstline[2]} {firstline[3]}')
        print(f'Suma de los precios: {suma}')      
        print('El promedio de los precios es: %.2f' % (suma/cont))
        archivo.close()

def leerArchivo_PB():
    '''
        Basándose en la	columna	Recomendation,	imprima	el Dress_ID que	se	ha	recomendado (Recomendación	=	1).	
        Para  aquellos vestidos que	no	fueron recomendados (Recomendación = 0), 
        averigüe	cuántos	tenían	un	tipo	de	patrón	de  animales (animal pattern). 
    '''

    with open('./Dresses.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        firstline = next(lector)
        print(f'{firstline[0]} {firstline[4]}')
        cont = 0
        for linea in lector:
            if int(linea[-1]) == 1:
                print(linea[0], linea[4])
            if int(linea[-1]) == 0 and 'animal' in linea[-2]:
                cont += 1
        print(f'Cantidad de vestidos con patrón de animales que no fueron recomendados: {cont}')
        archivo.close()

def leerArchivo_PC():
    '''
        Imprima	toda la	información	para todos los
        vestidos de	verano	que	tengan	un	Style del tipo “sexy”
    '''

    with open('./Dresses.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        firstline = next(lector)
        print(firstline)
        for linea in lector:
            if 'sexy' in linea[1]:
                print(linea)
        archivo.close()

'''
	Utilizando	la	columna	Price,	cree	
    un	diccionario	que	contenga todos los Dress_ID para	
    cada	uno	de	los	 valores “Bajo”, “Alto”, “Promedio”	y “Medio”.	
    Para	cada	llave,	imprima	los	códigos	asociados y el número total	de códigos
    asociados	para	cada	una	de	las	llaves.
'''

def leerArchivo_PD():
    with open('./Dresses.csv', 'r') as archivo:
        lector = csv.reader(archivo)
        firstline = next(lector)
        print(firstline)
        dic = {
                'Bajo': [],
                'Alto': [], 
                'Promedio': [], 
                'Medio': []
            }
        for linea in lector:
            if linea[2] == 'Low':
                dic['Bajo'].append(linea[0])
            elif linea[2] == 'High':
                dic['Alto'].append(linea[0])
            elif linea[2] == 'Average':
                dic['Promedio'].append(linea[0])
            elif linea[2] == 'Medium':
                dic['Medio'].append(linea[0])
        for key, value in dic.items():
            print(f'{key}', end='>> ')
            print(f'Cantidad de códigos asociados: {len(value)}')
        archivo.close()


while op := input('Ingrese la opción a ejecutar (0 para terminar): '):
    if op.capitalize() == 'A':
        leerArchivo_PA('./Dresses.csv')
        print('____________________')
        print("Obtiene todos los vestidos que tiene	una	puntuación	> 0, a continuación,	imprima	la	calificación promedio de estos	vestidos.")
    elif op.capitalize() == 'B':
        leerArchivo_PB()
        print('____________________')
        print("""
	Basándose en la	columna	Recomendation,	imprima	el	Dress_ID que	se	ha	recomendado	(Recomendación = 1).	Para aquellos	vestidos	que	no	fueron	recomendados (Recomendación	=	0),	averigüe cuántos	tenían	un	tipo	de	patrón	de animales	(animal	pattern).
""")
    elif op.capitalize() == 'C':
        leerArchivo_PC()
        print('____________________')
        print("""
    Imprima	toda la	información	para todos	los	vestidos de	verano	que	tengan	un	Style del	tipo “sexy”
    """)
    elif op.capitalize() == 'D':
        leerArchivo_PD()
        print('____________________')
        print("""
    Utilizando	la	columna	Price,	cree un	diccionario	que	contenga todos	los	Dress_ID	para cada uno de los	valores"""
    )
    elif op.capitalize() == '0':
        break
    else:
        print('____________________\nOpción inválida')
        print('Para terminar el programa presione 0\n____________________\n')
