#!/usr/bin/env python
# coding: utf-8

# # Api
# ## https://restcountries.eu
# python-restcountries
# https://pypi.org/project/python-restcountries/

# In[ ]:


# Install
get_ipython().system('pip install python-restcountries')


# In[10]:


# From restcountries import RestCountryApi as rapi
from restcountries import RestCountryApiV2 as rapi

# Get Denmark info
country_list = rapi.get_countries_by_name('Denmark')


# In[14]:


# Print information
country = country_list[0]
print(country.name)
print(country.capital)
print(country.calling_codes)
print(country.population)
print(country.flag)
print(country.languages)


# In[ ]:




