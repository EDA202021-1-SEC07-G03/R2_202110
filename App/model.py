"""
 * Copyright 2020, Departamento de sistemas y Computación,
 * Universidad de Los Andes
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
 *
 * Contribuciones:
 *
 * Dario Correal - Version inicial
 """


import config as cf
from DISClib.ADT import list as lt
from DISClib.Algorithms.Sorting import shellsort as sa
assert cf
import time
from DISClib.ADT import map as mp
from DISClib.DataStructures import mapentry as me
from DISClib.Algorithms.Sorting import insertionsort as ins
from DISClib.Algorithms.Sorting import selectionsort as ses
from DISClib.Algorithms.Sorting import shellsort as shs
from DISClib.Algorithms.Sorting import quicksort as qck
from DISClib.Algorithms.Sorting import mergesort as mrg
import datetime

"""
Se define la estructura de un catálogo de videos. El catálogo tendrá dos listas, una para los videos, otra para las categorias de
los mismos.
"""

# Construccion de modelos
def newCatalog():
  
    catalog = {'videos':None,
               'category':None,
               }
    catalog['videos'] = mp.newMap(380000,maptype='PROBING',loadfactor=0.6,comparefunction=cmpVideosbyId)
    catalog['category'] = mp.newMap(50,maptype='PROBING',loadfactor=0.6)
    return catalog
    
# Funciones para creacion de datos
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    mp.put(catalog['category'], str(category['name']).strip(),str(category['id']))
def add_node(catalog,input_file):
        for video in input_file:
            node=mp.newMap(20,maptype='PROBING',loadfactor=0.6)
            for x in video:
                mp.put(node,x,video[x])
            mp.put(catalog['videos'],video['video_id'],node)
# Funciones de consulta
def videos_pais_categoria(catalog,pais,id,n):
    lista=lt.newList('ARRAYLIST')
    keys=mp.keySet(catalog['videos'])
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        valor_video=me.getValue(mp.get(catalog['videos'],key))
        if me.getValue(mp.get(valor_video,'country')).lower()==pais.lower() and me.getValue(mp.get(valor_video,'category_id'))==id:
            lt.addLast(lista,valor_video)
    mrg.sort(lista,cmpVideosbyViews)
    return lt.subList(lista,1,n)
    
# Funciones de comparacion
def cmpVideosbyViews(video1,video2):
    video1=me.getValue(mp.get(video1,'views'))
    video2=me.getValue(mp.get(video2,'views'))
    return(int(video1)>int(video2))

def cmpVideosbyLikes(video1,video2):
    return(int(video1["likes"])>int(video2["likes"]))

def cmpVideosbyId(id1, id2):
    id2=me.getKey(id2)
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1