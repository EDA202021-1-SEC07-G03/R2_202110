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
               'video_id': None,
               'trending_date': None,
               'title': None,
               'channel_title': None,
               'category_id': None,
               'publish_time': None,
               'tags': None,
               'views': None,
               'likes': None,
               'dislikes': None,
               'country': None}

 
    catalog['videos'] = lt.newList('SINGLE_LINKED')
    catalog['category'] = mp.newMap(50,
                                maptype='PROBING',
                                loadfactor=0.6)
    catalog['video_id'] = mp.newMap(380000,
                                maptype='PROBING',
                                loadfactor=0.6,
                                comparefunction=cmpVideosbyId)
    catalog['views'] = mp.newMap(380000,
                                maptype='PROBING',
                                loadfactor=0.6,
                                comparefunction=cmpVideosbyId)





    return catalog
    
# Funciones para creacion de datos
def addVideo(catalog, video):
    lt.addLast(catalog['videos'], video)

def addCategory(catalog, category):
    mp.put(catalog['category'], str(category['id']),str(category['name']))
    









    

# Funciones de consulta


# Funciones de comparacion
def cmpVideosbyViews(video1,video2):
    return(int(video1["views"])>int(video2["views"]))

def cmpVideosbyLikes(video1,video2):
    return(int(video1["likes"])>int(video2["likes"]))

def cmpVideosbyId(id1, id2):

    if (id1 == id2):
        return 0
    elif id1 > id2:
        return 1
    else:
        return -1