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
    catalog = {'category_id':None,
               'category':None,
               'countries':None}
    catalog['category_id'] = mp.newMap(50,maptype='PROBING',loadfactor=0.6,comparefunction=cmpVideosbyId)
    catalog['category'] = mp.newMap(50,maptype='PROBING',loadfactor=0.6)
    catalog['countries']= mp.newMap(30,maptype='PROBING',loadfactor=0.6,comparefunction=cmpVideosbyId)
    return catalog
    
# Funciones para creacion de datos
def addCategory(catalog, category):
    if not(str(category['name']).strip()=='Comedy' and str(category['id'])=='34'):
        mp.put(catalog['category'], str(category['name']).strip(),str(category['id']))
def add_node(catalog,video):
    node=mp.newMap(20,maptype='PROBING',loadfactor=0.6)
    for key in video:
        mp.put(node,key,video[key])
    if mp.contains(catalog['category_id'],video['category_id'])==False:
        lista=lt.newList('ARRAY_LIST')
        lt.addFirst(lista,node)
        mp.put(catalog['category_id'],video['category_id'],lista)
    else:
        lista=me.getValue(mp.get(catalog['category_id'],video['category_id']))
        lt.addLast(lista,node)
        mp.put(catalog['category_id'],video['category_id'],lista)
def add_node_country(catalog,video):
    node=mp.newMap(20,maptype='PROBING',loadfactor=0.6)
    for key in video:
        mp.put(node,key,video[key])
    if mp.contains(catalog['countries'],video['country'])==False:
        lista=lt.newList('ARRAY_LIST')
        lt.addFirst(lista,node)
        mp.put(catalog['countries'],video['country'].lower(),lista)
    else:
        lista=me.getValue(mp.get(catalog['countries'],video['country'].lower()))
        lt.addLast(lista,node)
        mp.put(catalog['countries'],video['country'].lower(),lista)

def contador(lista,video_id):
    r=0
    for i in range(1,lt.size(lista)+1):
        mapa_video=lt.getElement(lista,i)
        id=me.getValue(mp.get(mapa_video,'video_id'))
        if id==video_id:
            r+=1
    return r
def dias_tendencia(lista):
    for i in range(1,lt.size(lista)+1):
        mapa_video=lt.getElement(lista,i)
        video_id=me.getValue(mp.get(mapa_video,'video_id'))
        numero=contador(lista,video_id)
        mp.put(mapa_video,'dias',numero) 

# Funciones de consulta

#REQUERIMIENTO 1
def videos_pais_categoria(catalog,pais,id,n):
    lista=lt.newList('ARRAYLIST')
    videos_pais=me.getValue(mp.get(catalog['countries'],pais.lower()))
    for i in range(1,lt.size(videos_pais)+1):
        mapa_interno=lt.getElement(videos_pais,i)
        category_id=me.getValue(mp.get(mapa_interno,'category_id'))
        if category_id==id:
            lt.addLast(lista,mapa_interno)
    mrg.sort(lista,cmpVideosbyViews)
    if lt.size(lista)<n:
        sublist=lista
    else:
        sublist=lt.subList(lista,1,n)
    return sublist

#REQUERIMIENTO 2
def videos_tendencia_pais(catalog,pais):
    mayor=0
    r=mp.newMap()
    videos_category=me.getValue(mp.get(catalog['countries'],pais.lower()))
    dias_tendencia(videos_category)
    for i in range(1,lt.size(videos_category)+1):
        mapa_interno=lt.getElement(videos_category,i)
        dias=me.getValue(mp.get(mapa_interno,'dias'))
        if dias>mayor:
            mayor=dias
            r=mapa_interno
    return r,mayor

#REQUERIMIENTO 3
def videos_tendencia_categoria(catalog,id):
    mayor=0
    r=mp.newMap()
    videos_pais=me.getValue(mp.get(catalog['category_id'],id))
    dias_tendencia(videos_pais)
    for i in range(1,lt.size(videos_pais)+1):
        mapa_interno=lt.getElement(videos_pais,i)
        dias=me.getValue(mp.get(mapa_interno,'dias'))
        if dias>mayor:
            mayor=dias
            r=mapa_interno
    return r,mayor

#REQUERIMIENTO 4
def videos_pais_tag(catalog,pais,tag,n):
    lista=lt.newList('ARRAYLIST')
    videos_pais=me.getValue(mp.get(catalog['countries'],pais.lower()))
    for i in range(1,lt.size(videos_pais)+1):
        mapa_interno=lt.getElement(videos_pais,i)
        tags=me.getValue(mp.get(mapa_interno,'tags'))
        if tag in tags:
            lt.addLast(lista,mapa_interno)
    mrg.sort(lista,cmpVideosbyLikes)
    if lt.size(lista)<n:
        sublist=lista
    else:
        sublist=lt.subList(lista,1,n)
    return sublist

# Funciones de comparacion
def cmpVideosbyViews(video1,video2):
    video1=me.getValue(mp.get(video1,'views'))
    video2=me.getValue(mp.get(video2,'views'))
    return(int(video1)>int(video2))

def cmpVideosbyLikes(video1,video2):
    video1=me.getValue(mp.get(video1,'likes'))
    video2=me.getValue(mp.get(video2,'likes'))
    return(int(video1)>int(video2))

def cmpVideosbyId(id1, id2):
    id2=me.getKey(id2)
    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1