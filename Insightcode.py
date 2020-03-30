#!/usr/bin/env python
# coding: utf-8

# In[74]:


import csv


# In[75]:


#we will put everything from the input csv into a nested dictionary like with keys as follows- year, 
#product,comapany, count of complaints associated with that company
#store the input in a dictionary called new_data_dict
new_data_dict = {}
with open('input.csv', 'r') as file:
    my_reader = csv.reader(file, delimiter=",")
    for row in my_reader:
        k= new_data_dict.setdefault(row[0][-2:],{}).setdefault(row[1],{})
        if(k.get(row[7]) == None):
            k[row[7]]=1
        else:
            k[row[7]]=k.get(row[7])+1
        
        


# In[87]:


new_data_dict


# In[101]:


#remove header
del new_data_dict['ed']


# In[126]:


#store the calculated values in a new csv file
#i understand this is not the complete output
#however I intended to find the highest count of the company and divde it by the number of companies
#in ear year-product pair 
#print each year(outer key) and it's combination of product as a new row
#calculate company count/divided by the total companies per new_data_dict[year][product] and then store this value in the row
#do this for each row and point the output to an output.csv
#I wanted to iterate over the loop and somehow couldn't acheive that completely

with open('output.csv', 'w') as csv_file:
    csvwriter = csv.writer(csv_file, delimiter='\t')
    for key,val in new_data_dict.items():
        for k in new_data_dict:
            csvwriter.writerow([key, val, k])


# In[ ]:





# In[ ]:




