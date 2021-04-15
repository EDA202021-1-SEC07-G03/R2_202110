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
import tracemalloc
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

def getTime():
    return float(time.perf_counter()*1000)
def getMemory():
    return tracemalloc.take_snapshot()
def deltaMemory(start_memory, stop_memory):
    memory_diff = stop_memory.compare_to(start_memory, "filename")
    delta_memory = 0.0
    for stat in memory_diff:
        delta_memory = delta_memory + stat.size_diff
    delta_memory = delta_memory/1024.0
    return delta_memory
def contar_videos(catalog):
    suma=0
    keys=mp.keySet(catalog['countries'])
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        lt_pais=me.getValue(mp.get(catalog['countries'],key))
        suma+=lt.size(lt_pais)
    return suma
"""
Menu principal
"""
while True:
    printMenu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs[0]) == 1:
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #
        print("Inicializando Catálogo ....")
        catalog = controller.initCatalog()
        print("Cargando información de los archivos ....")
        answer = controller.loadData(catalog)
        #
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print('Paises:',mp.size(catalog['countries']))
        print('Videos cargados:',contar_videos(catalog))
        print('Categorias cargadas:',mp.size(catalog['category']))
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)
   
#REQUERIMIENTO 1
    elif int(inputs[0]) == 2:
        pais=(str(input('Digite el pais de su interes: ')))
        nombre_categoria=(str(input('Digite la categoria de su interes: ')))
        n= int(input('Indique la cantidad de videos que desea recibir: '))
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #
        sublist=controller.videos_pais_categoria(catalog,pais,nombre_categoria,n)
        keys=['trending_date', 'title','channel_title','publish_time','views','likes','dislikes']
        size=lt.size(sublist)
        if size==0:
            print('\nNo se han encontrado videos para la categoria',nombre_categoria,'en',pais+'\n')
        else:
            if size==1:
                print('\nSe encontro el siguiente video en',pais,'para la categoria',nombre_categoria+':\n')
            elif size>1:
                print('\nSe encontraron los siguientes',size,'videos en',pais,'para la categoria',nombre_categoria+':\n')
        for i in range(1,lt.size(sublist)+1):
            mapa=lt.getElement(sublist,i)
            print('*'*80)
            print('VIDEO',i)
            for key in keys:
                print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        #
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        
        print('-'*80)

#REQUERIMIENTO 2
    elif int(inputs[0]) == 3:
        pais=(str(input('Digite el pais de su interes: ')))
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #
        mapa=controller.videos_tendencia_pais(catalog,pais)[0]
        dias=controller.videos_tendencia_pais(catalog,pais)[1]
        keys=['title','channel_title','country']
        print('*'*80)
        print('VIDEO TENDENCIA EN',pais.upper())
        for key in keys:
            print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('dias_tendencia:',dias)
        #
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        
        print('-'*80)

#REQUERIMIENTO 3
    elif int(inputs[0]) == 4:
        nombre_categoria=(str(input('Digite la categoria de su interes: ')))
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #
        mapa=controller.videos_tendencia_categoria(catalog,nombre_categoria)[0]
        dias=controller.videos_tendencia_categoria(catalog,nombre_categoria)[1]
        keys=['title','channel_title','country','trending_date']
        print('*'*80)
        print('VIDEO TENDENCIA EN',nombre_categoria.upper())
        for key in keys:
            print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        print('dias_tendencia:',dias)
        #
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        
        print('-'*80)

#REQUERIMIENTO 4
    elif int(inputs[0]) == 5:
        pais=(str(input('Digite el pais de su interes: ')))
        tag=input('Digite el tag de su interes: ')
        n= int(input('Indique la cantidad de videos que desea recibir: '))
        tracemalloc.start()
        start_time = getTime()
        start_memory = getMemory()
        #
        sublist=controller.videos_pais_tag(catalog,pais,tag,n)
        size=lt.size(sublist)
        keys=['title','channel_title','publish_time','views','likes','dislikes','tags']
        if size==0:
            print('\nNo se han encontrado videos para el tag',tag,'en',pais+'\n')
        else:
            if size==1:
                print('\nSe encontro el siguiente video en',pais,'con el tag',tag+':\n')
            elif size>1:
                print('\nSe encontraron los siguientes',size,'videos en',pais,'con el tag',tag+':\n')
            for i in range(1,lt.size(sublist)+1):
                mapa=lt.getElement(sublist,i)
                print('*'*80)
                print('VIDEO',i)
                for key in keys:
                    if key=='tags':
                        tags=str(me.getValue(mp.get(mapa,key))).split('|')
                        tags=', '.join(tags)
                        print('tags:',tags)
                    else:
                        print(me.getKey(mp.get(mapa,key)),':',me.getValue(mp.get(mapa,key)))
        #
        stop_memory = getMemory()
        stop_time = getTime()
        tracemalloc.stop()
        delta_time = round(stop_time - start_time,2)
        delta_memory = round(deltaMemory(start_memory, stop_memory),2)
        print("Tiempo [ms]:",delta_time)
        print("Memoria [kB]:",delta_memory,)
        print('-'*80)
        
    else:
        sys.exit(0)
sys.exit(0)