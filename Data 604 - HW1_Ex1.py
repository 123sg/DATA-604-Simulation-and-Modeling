#!/usr/bin/env python
# coding: utf-8

# In[1]:


try:
    import pint
except ImportError:
    get_ipython().system('pip install pint')
    import pint


# In[2]:


try:
    from modsim import *
except ImportError:
    get_ipython().system('pip install modsimpy')
    from modsim import *


# In[3]:


get_ipython().system('python --version')


# In[4]:


get_ipython().system('jupyter-notebook --version')


# In[5]:


# Configure Jupyter so figures appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Configure Jupyter to display the assigned value after an assignment
get_ipython().run_line_magic('config', "InteractiveShell.ast_node_interactivity='last_expr_or_assign'")


# In[6]:


meter = UNITS.meter


# In[7]:


second = UNITS.second


# In[8]:


a = 9.8 * meter / second**2


# In[9]:


t = 4 * second


# In[10]:


a * t**2 / 2


# In[12]:


h = 381 * meter


# In[13]:


t = sqrt(2 * h / a)


# In[14]:


v = a * t


# In[16]:


h = 381 * meter


# In[17]:


t = sqrt(2 * h / a)


# In[18]:


v = a * t


# In[20]:


mile = UNITS.mile
hour = UNITS.hour


# In[21]:


v.to(mile/hour)


# In[22]:


foot = UNITS.foot


# In[23]:


pole_height = 10 * foot


# In[24]:


pole_height + h


# In[25]:


h + pole_height


# In[29]:


vReach = 18 * UNITS.meters / UNITS.second


# In[30]:


tReach = vReach / a


# In[31]:


dFall = a * tReach**2 / 2


# In[32]:


tRemaining = (h - dFall) / vReach


# In[33]:


tTotal = tReach + tRemaining


# In[ ]:




