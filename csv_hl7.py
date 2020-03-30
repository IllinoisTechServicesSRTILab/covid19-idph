#!/usr/bin/env python
# coding: utf-8

# In[1]:


#ashley hetrick, ahetrick@illinois.edu
#2020-03-30


# In[2]:


#import libraries
get_ipython().run_line_magic('pip', 'install hl7apy')
import csv
from hl7apy.core import Message


# In[3]:


#function definitions 
def make_hl7(filename):
    messages = []
    with open(filename,newline='',encoding='utf-8-sig') as f:
        reader = csv.reader(f, delimiter=',', quotechar='|')
        for row in reader:
            m = Message("ADT_A01",version='2.7')
            m.msh.msh_3 = row[0]
            m.pid.pid_3.pid_3_1 = row[1]
            m.pid.pid_3.pid_3_2 = row[2]
            m.pid.pid_3.pid_3_3 = row[3]
            m.pid.pid_3.pid_3_4 = row[4]
            m.pid.pid_5.pid_5_1 = row[5]
            m.pid.pid_5.pid_5_2 = row[6]
            m.pid.pid_5.pid_5_3 = row[7]
            messages.append(m)
    return messages


# In[4]:


def output_csv(hl7_object):
    with open('hl7_messages.csv', 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        for message in hl7_object:
            csvwriter.writerow([message.msh.to_er7() + message.pid.to_er7()])


# In[5]:


def main(filename):
    output_csv(make_hl7(filename))


# In[6]:


#call to main function
main('data/csv_to_hl7.csv')

