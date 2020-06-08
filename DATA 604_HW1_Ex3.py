#!/usr/bin/env python
# coding: utf-8

# In[4]:


get_ipython().run_line_magic('matplotlib', 'inline')

# Configure Jupyter to display the assigned value after an assignment
get_ipython().run_line_magic('config', "InteractiveShell.ast_node_interactivity='last_expr_or_assign'")

# import functions from the modsim library
from modsim import *

# set the random number generator
np.random.seed(7)


# In[1]:


def step(state, p1, p2):
    """Simulate one minute of time.
    
    state: bikeshare State object
    p1: probability of an Olin->Wellesley customer arrival
    p2: probability of a Wellesley->Olin customer arrival
    """
    if flip(p1):
        bike_to_wellesley(state)
    
    if flip(p2):
        bike_to_olin(state)
        
def bike_to_wellesley(state):
    """Move one bike from Olin to Wellesley.
    
    state: bikeshare State object
    """
    state.olin -= 1
    state.wellesley += 1
    
def bike_to_olin(state):
    """Move one bike from Wellesley to Olin.
    
    state: bikeshare State object
    """
    state.wellesley -= 1
    state.olin += 1
    
def decorate_bikeshare():
    """Add a title and label the axes."""
    decorate(title='Olin-Wellesley Bikeshare',
             xlabel='Time step (min)', 
             ylabel='Number of bikes')


# In[2]:


def run_simulation(state, p1, p2, num_steps):
    """Simulate the given number of time steps.
    
    state: State object
    p1: probability of an Olin->Wellesley customer arrival
    p2: probability of a Wellesley->Olin customer arrival
    num_steps: number of time steps
    """
    results = TimeSeries()    
    for i in range(num_steps):
        step(state, p1, p2)
        results[i] = state.olin
        
    plot(results, label='Olin')


# In[5]:


bikeshare1 = State(olin=10, wellesley=2)


# In[6]:


bikeshare2 = State(olin=2, wellesley=10)


# In[7]:


bike_to_olin(bikeshare1)


# In[8]:


bike_to_wellesley(bikeshare2)


# In[9]:


bikeshare1


# In[10]:


bikeshare2


# In[11]:


bikeshare = State(olin=10, wellesley=2)
run_simulation(bikeshare, 0.4, 0.2, 60)
decorate_bikeshare()


# In[12]:


def bike_to_wellesley(state):
    """Move one bike from Olin to Wellesley.
    
    state: bikeshare State object
    """
    if state.olin == 0:
        return
    state.olin -= 1
    state.wellesley += 1
    
def bike_to_olin(state):
    """Move one bike from Wellesley to Olin.
    
    state: bikeshare State object
    """
    if state.wellesley == 0:
        return
    state.wellesley -= 1
    state.olin += 1


# In[13]:


bikeshare = State(olin=10, wellesley=2)
run_simulation(bikeshare, 0.4, 0.2, 60)
decorate_bikeshare()


# In[14]:


x = 5


# In[15]:


x == 5


# In[16]:


if x == 5:
    print('yes, x is 5')


# In[17]:


bikeshare = State(olin=10, wellesley=2, 
                  olin_empty=0, wellesley_empty=0)


# In[18]:


def bike_to_wellesley(state):
    """Move one bike from Olin to Wellesley.
    
    state: bikeshare State object
    """
    if state.olin == 0:
        state.olin_empty += 1
        return
    state.olin -= 1
    state.wellesley += 1
    
def bike_to_olin(state):
    """Move one bike from Wellesley to Olin.
    
    state: bikeshare State object
    """
    if state.wellesley == 0:
        state.wellesley_empty += 1
        return
    state.wellesley -= 1
    state.olin += 1


# In[19]:


run_simulation(bikeshare, 0.4, 0.2, 60)
decorate_bikeshare()


# In[20]:


bikeshare.olin_empty


# In[21]:


bikeshare.wellesley_empty


# In[22]:


bikeshare = State(olin=10, wellesley=2, 
                  olin_empty=0, wellesley_empty=0,
                  clock=0)


# In[25]:


#Excercise
def step(state, p1, p2):
    state.clock += 1
    if flip(p1):
        bike_to_wellesley(state)
    
    if flip(p2):
        bike_to_olin(state)


# In[26]:


run_simulation(bikeshare, 0.4, 0.2, 60)
decorate_bikeshare()


# In[27]:


bikeshare


# In[28]:


bikeshare = State(olin=10, wellesley=2, 
                  olin_empty=0, wellesley_empty=0,
                  clock=0, t_first_empty=-1)


# In[29]:


def step(state, p1, p2):
    state.clock += 1
    
    if flip(p1):
        bike_to_wellesley(state)
    
    if flip(p2):
        bike_to_olin(state)
        
    if state.t_first_empty != -1:
        return
    
    if state.olin_empty + state.wellesley_empty > 0:
        state.t_first_empty = state.clock


# In[30]:


run_simulation(bikeshare, 0.4, 0.2, 60)
decorate_bikeshare()


# In[31]:


bikeshare


# In[ ]:




