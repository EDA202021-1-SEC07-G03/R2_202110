"""
 * Copyright 2020, Departamento de sistemas y Computación, Universidad
 * de Los Andes
 *
 *
 * Desarrolado para el curso ISIS1225 - Estructuras de Datos y Algoritmos
 *
 *
 * This program is free software: you can redistribute it and/or modify
 * it under the terms of the GNU General Public License as published by
 * the Free Software Foundation, either version 3 of the License, or
 * (at your option) any later version.
 *
 * This program is distributed in the hope that it will be useful,
 * but WITHOUT ANY WARRANTY; without even the implied warranty of
 * MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
 * GNU General Public License for more details.
 *
 * You should have received a copy of the GNU General Public License
 * along withthis program.  If not, see <http://www.gnu.org/licenses/>.
 """

import config as cf
import sys
import controller
from DISClib.ADT import list as lt
assert cf
import time
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs


"""
La vista se encarga de la interacción con el usuario
Presenta el menu de opciones y por cada seleccion
se hace la solicitud al controlador para ejecutar la
operación solicitada
"""

def printMenu():
    print("Bienvenido")
    print("1- Inicializar catálogo")
    print("2- Cargar información en el catálogo")
    print("3- Videos con mas likes por categoría")

"""
Menu principal
"""




while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()

    elif int(inputs[0]) == 2:
        print("Cargando información de los archivos ....")
        
        answer = controller.loadData(catalog)
        print('Videos cargados: ' + str(lt.size(catalog['videos'])))
        #Primer video cargado
        print('Title: ' + lt.firstElement(catalog["videos"])['title'])
        print('Channel title: ' + lt.firstElement(catalog["videos"])['channel_title'])
        print('Trending date: ' + lt.firstElement(catalog["videos"])['trending_date'])
        print('Country: ' + lt.firstElement(catalog["videos"])['country'])
        print('Views: ' + lt.firstElement(catalog["videos"])['views'])
        print('Likes: ' +lt.firstElement(catalog["videos"])['likes'])
        print('Dislikes: ' +lt.firstElement(catalog["videos"])['dislikes'])



        #Categorias
        print(catalog['category']['table']['elements'])

        print("Tiempo [ms]: ", f"{answer[0]:.3f}", "  ||  ",  "Memoria [kB]: ", f"{answer[1]:.3f}")
   

    elif int(inputs[0]) == 3:
        pass
        
   

    else:
        sys.exit(0)
sys.exit(0)