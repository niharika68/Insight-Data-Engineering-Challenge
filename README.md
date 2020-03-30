# Insight-Data-Engineering-Challenge
This is the solution for my insight data engineering challenge

The problem refers to finding three things from the consumer complaints dataset:
1. Total number of complaints for a particular product and year pair (unique pair)
2. Total number companies receving atleast one compaint for that product and year pair. 
3. Highest Number of complaints in % of companies that recevie complaints for that product and year. 

I have used a dictionary of dictionary of dictionary i.e. a 3 layer dictionary to do the same. 

The outer has the key of the year, inner has of product and then of company associated with the certain count. 

Using this we find the final answer. 
