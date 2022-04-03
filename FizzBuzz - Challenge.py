#!/usr/bin/env python
# coding: utf-8

# ## FizzBuzz Coding Challenge:

# In[ ]:


for i in range(1,101):
    if (i % 3) == 0 or (i % 5 == 0):
        if i % (3*5) == 0 :
            print("FizzBuzz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print("Fizz")
    else:
        print(i)

