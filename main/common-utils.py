#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[17]:


def convert_lat(value):
    toReturn = ""
    if value and value!=0:
        toReturn = value/((2**32)/360)
    return toReturn

