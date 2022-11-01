#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np


# In[2]:


import pandas as pd


# ### Through this game we randomly generate two numbers and ask users to guess them which on is greater ### 

# ### If user guess is correct, score increases. If user guess is in correct, game stops and final score is displayed ###

# In[78]:


def guess():
    a = np.random.randint(1000) # Randomly generating 2 numbers
    print(a)
    b = np.random.randint(1000)
    print(b)
    while a == b:
        b = np.random.randint(1000) 
        # To randomize numbers even if both randomly generated numbers are equal
    c = input("Which is bigger 'a' or 'b' ?").lower() # Actual guess entered by user
    if a > b and c == 'a':
        return True
    elif b > a and c == 'b':
        return True
    else:
        return False


# In[79]:


score = 0

d = True
while d == True:
    if guess() == True:
        score = score + 1
        print(f"Your Total Score is {score}")
    else:
        d = False
        print(f"You Lost! Your Final Score is{score}")
        


# In[ ]:





# In[ ]:




