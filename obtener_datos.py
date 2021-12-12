#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Obtención de los datos


# In[ ]:


from urllib import request
import py7zr
import os


# In[ ]:


path1 = 'https://github.com/m-valenzuela-arce/Proceso-de-Ing-de-Caracteristicas/raw/main/Datos/Calificaciones-2212-21112021-enviar.7z'
path2 = 'https://github.com/m-valenzuela-arce/Proceso-de-Ing-de-Caracteristicas/raw/main/Datos/HISTORIAL-Calificaciones-2212-21112021-enviar.7z'


# In[ ]:


directory = os.getcwd()


# In[ ]:


remote_url1 = path1
remote_url2 = path2

local_file1 = 'datos1.7z'
local_file2 = 'datos2.7z'

request.urlretrieve(remote_url1, local_file1)
request.urlretrieve(remote_url2, local_file2)


# In[ ]:


with py7zr.SevenZipFile("datos1.7z", 'r') as archive
    archive.extractall(path=directory)
    
with py7zr.SevenZipFile("datos2.7z", 'r') as archive:
    archive.extractall(path=directory)

