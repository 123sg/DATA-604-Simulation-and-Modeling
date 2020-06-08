#!/usr/bin/env python
# coding: utf-8

# In[1]:


# Configure Jupyter so figures appear in the notebook
get_ipython().run_line_magic('matplotlib', 'inline')

# Configure Jupyter to display the assigned value after an assignment
get_ipython().run_line_magic('config', "InteractiveShell.ast_node_interactivity='last_expr_or_assign'")

# import functions from the modsim library
from modsim import *

# set the random number generator
np.random.seed(7)

# If this cell runs successfully, it produces no output.


# In[2]:


bikeshare = State(olin=10, wellesley=2)


# In[3]:


bikeshare.olin


# In[4]:


bikeshare.wellesley


# In[5]:


bikeshare.olin -= 1


# In[6]:


bikeshare


# In[7]:



bikeshare.wellesley += 1
bikeshare


# In[8]:


def bike_to_wellesley():
    bikeshare.olin -= 1
    bikeshare.wellesley += 1


# In[9]:


bike_to_wellesley()
bikeshare


# In[10]:


bike_to_wellesley


# In[12]:


def bike_to_olin():
    bikeshare.wellesley -= 1
    bikeshare.olin += 1


# In[13]:


bike_to_olin()
bikeshare


# In[14]:


help(flip)


# In[15]:


flip(0.7)


# In[17]:


if flip(0.7):
    print('heads')


# In[18]:


if flip(0.7):
    print('heads')
else:
    print('tails')


# In[19]:


bikeshare = State(olin=10, wellesley=2)


# In[20]:


if flip(0.5):
    bike_to_wellesley()
    print('Moving a bike to Wellesley')

bikeshare


# In[21]:


if flip(0.4):
    bike_to_olin()
    print('Moving a bike to Olin')

bikeshare


# In[23]:


def step():
    if flip(0.5):
        bike_to_wellesley()
        print('Moving a bike to Wellesley')
        
    if flip(0.4):
        bike_to_olin()
        print('Moving a bike to Olin')


# In[24]:


step()
bikeshare


# In[25]:


def step(p1, p2):
    if flip(p1):
        bike_to_wellesley()
        print('Moving a bike to Wellesley')
        
    if flip(p2):
        bike_to_olin()
        print('Moving a bike to Olin')


# In[26]:


step(0.5, 0.4)
bikeshare


# In[27]:


def step(p1, p2):
    print(p1, p2)
    if flip(p1):
        bike_to_wellesley()
        
    if flip(p2):
        bike_to_olin()
        
step(0.3, 0.2)


# In[28]:


def step(p1, p2):
    if flip(p1):
        bike_to_wellesley()
    
    if flip(p2):
        bike_to_olin()


# In[29]:


bikeshare = State(olin=10, wellesley=2)


# In[30]:


for i in range(4):
    bike_to_wellesley()
    
bikeshare


# In[31]:


for i in range(4):
    step(0.3, 0.2)
    
bikeshare


# In[32]:


for i in range(60):
    step(0.3, 0.2)

bikeshare


# In[33]:


results = TimeSeries()


# In[34]:


results[0] = bikeshare.olin
results


# In[35]:


bikeshare = State(olin=10, wellesley=2)


# In[36]:


for i in range(10):
    step(0.3, 0.2)
    results[i] = bikeshare.olin


# In[37]:


results


# In[38]:


results.mean()


# In[39]:


results.describe()


# In[40]:


plot(results, label='Olin')

decorate(title='Olin-Wellesley Bikeshare',
         xlabel='Time step (min)', 
         ylabel='Number of bikes')

savefig('figs/chap02-fig01.pdf')


# In[ ]:


help(decorate)


# In[ ]:


help(savefig)


# In[41]:


def run_simulation(p1, p2, n):
    olin = TimeSeries()
    wellesley = TimeSeries()
    
    for i in range(n):
        step(p1, p2)
        olin[i] = bikeshare.olin
        wellesley[i] = bikeshare.wellesley
        
    plot(olin, label='Olin')
    plot(wellesley, label='Wellesley')
    decorate(title='Olin-Wellesley Bikeshare',
             xlabel='Time step (min)', 
             ylabel='Number of bikes')


# In[42]:


bikeshare = State(olin=10, wellesley=2)
run_simulation(0.3, 0.2, 60)


# In[43]:


help(decorate)


# In[44]:


source_code(flip)


# In[ ]:




