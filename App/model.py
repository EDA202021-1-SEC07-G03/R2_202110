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
               'category':None}
    catalog['videos'] = mp.newMap(380000,maptype='PROBING',loadfactor=0.6,comparefunction=cmpVideosbyId)
    catalog['category'] = mp.newMap(50,maptype='PROBING',loadfactor=0.6)
    return catalog
    
# Funciones para creacion de datos
def addCategory(catalog, category):
    if not(str(category['name']).strip()=='Comedy' and str(category['id'])=='34'):
        mp.put(catalog['category'], str(category['name']).strip(),str(category['id']))
def add_node(catalog,video):
    node=mp.newMap(20,maptype='PROBING',loadfactor=0.6)
    for key in video:
        mp.put(node,key,video[key])
    if mp.contains(catalog['videos'],video['video_id'])==False:
        mp.put(catalog['videos'],video['video_id'],node)
    else:
        mapa_interno=me.getValue(mp.get(catalog['videos'],video['video_id']))
        actual=me.getValue(mp.get(mapa_interno,'trending_date'))
        nuevo=me.getValue(mp.get(node,'trending_date'))
        juntos=str(actual)+','+str(nuevo)
        mp.put(mapa_interno,'trending_date',juntos)

def dias_tendencia(mapa_interno):
    dates=str(me.getValue(mp.get(mapa_interno,'trending_date'))).split(',')
    dias=len(dates)
    return dias 

# Funciones de consulta

#REQUERIMIENTO 1
def videos_pais_categoria(catalog,pais,id,n):
    lista=lt.newList('ARRAYLIST')
    keys=mp.keySet(catalog['videos'])
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        mapa_interno=me.getValue(mp.get(catalog['videos'],key))
        country=me.getValue(mp.get(mapa_interno,'country'))
        category_id=me.getValue(mp.get(mapa_interno,'category_id'))
        if country.lower()==pais.lower() and category_id==id:
            lt.addLast(lista,mapa_interno)
    mrg.sort(lista,cmpVideosbyViews)
    if lt.size(lista)<n:
        sublist=lista
    else:
        sublist=lt.subList(lista,1,n)
    return sublist

#REQUERIMIENTO 2
def videos_tendencia_pais(catalog,pais):
    keys=mp.keySet(catalog['videos'])
    mayor=0
    r=mp.newMap()
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        mapa_interno=me.getValue(mp.get(catalog['videos'],key))
        dias=dias_tendencia(mapa_interno)
        country=me.getValue(mp.get(mapa_interno,'country'))
        if country.lower()==pais.lower() and dias>mayor:
            mayor=dias
            r=mapa_interno
    return r,mayor

#REQUERIMIENTO 3
def videos_tendencia_categoria(catalog,id):
    keys=mp.keySet(catalog['videos'])
    mayor=0
    r=mp.newMap()
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        mapa_interno=me.getValue(mp.get(catalog['videos'],key))
        dias=dias_tendencia(mapa_interno)
        category_id=me.getValue(mp.get(mapa_interno,'category_id'))
        if category_id==id and dias>mayor:
            mayor=dias
            r=mapa_interno
    return r,mayor

#REQUERIMIENTO 4
def videos_pais_tag(catalog,pais,tag,n):
    lista=lt.newList('ARRAYLIST')
    keys=mp.keySet(catalog['videos'])
    for i in range(1,lt.size(keys)+1):
        key=lt.getElement(keys,i)
        mapa_interno=me.getValue(mp.get(catalog['videos'],key))
        country=me.getValue(mp.get(mapa_interno,'country'))
        tags=me.getValue(mp.get(mapa_interno,'tags'))
        if country.lower()==pais.lower() and tag in tags:
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