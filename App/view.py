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
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
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
    print("1- Cargar información en el catálogo")
    print("2- Videos tendencia por país y categoría")
    print("3- Video trending por país")
    print("4- Video trending por categoría")
    print("5- Videos con más likes por país y tag")
    print("6- Salir")
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        answer = controller.loadData(catalog)
        print('Videos cargados: ' + str(mp.size(catalog['videos'])))
        print('Categorias cargadas:',mp.size(catalog['category']))
        print('-'*80)
   

    elif int(inputs[0]) == 2:
        pais=(str(input('Digite el pais de su interes: ')))
        nombre_categoria=(str(input('Digite la categoria de su interes: ')))
        n= int(input('Indique la cantidad de videos que desea recibir: '))
        t1=process_time()
        sublist=controller.videos_pais_categoria(catalog,pais,nombre_categoria,n)
        t2=process_time()
        keys=['trending_date', 'title','channel_title','publish_time','views','likes','dislikes']
        for i in range(1,lt.size(sublist)+1):
            mapa=lt.getElement(sublist,i)
            print('*'*60)
            print('VIDEO',i)
            for key in keys:
                print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('tiempo de ejecucion:',t2-t1,'s---Memoria:',)
        print('-'*80)

    elif int(inputs[0]) == 3:
        pais=(str(input('Digite el pais de su interes: ')))
        mapa=controller.videos_tendencia_pais(catalog,pais)[0]
        dias=controller.videos_tendencia_pais(catalog,pais)[1]
        keys=['title','channel_title','country']
        print('*'*60)
        print('VIDEO TENDENCIA EN',pais.upper())
        for key in keys:
            print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('dias_tendencia:',dias)
        print('-'*80)

    elif int(inputs[0]) == 4:
        nombre_categoria=(str(input('Digite la categoria de su interes: ')))
        mapa=controller.videos_tendencia_pais(catalog,nombre_categoria)[0]
        dias=controller.videos_tendencia_categoria(catalog,nombre_categoria)[1]
        keys=['title','channel_title','country']
        print('*'*60)
        print('VIDEO TENDENCIA EN',nombre_categoria.upper())
        for key in keys:
            print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('dias_tendencia:',dias)
        print('-'*80)
    elif int(inputs[0]) == 5:
        pais=(str(input('Digite el pais de su interes: ')))
        tag=(str(input('Digite el tag de su interes: ')))
        n= int(input('Indique la cantidad de videos que desea recibir: '))
        sublist=controller.videos_pais_tag(catalog,pais,tag,n)
        keys=['title','channel_title','publish_time','views','likes','dislikes','tags']
        print(sublist)
        for i in range(1,lt.size(sublist)+1):
            mapa=lt.getElement(sublist,i)
            print('*'*60)
            print('VIDEO',i)
            for key in keys:
                if key=='tags':
                    tags=str(me.getValue(mp.get(mapa,key))).split('|')
                    tags=tags.join(', ')
                print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('-'*80)
    else:
        sys.exit(0)
sys.exit(0)