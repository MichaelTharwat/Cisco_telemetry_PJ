#!/usr/bin/env python
# coding: utf-8

# In[1]:


from netmiko import ConnectHandler
import pandas as pd
import json
import csv


# In[2]:


E={}
node=pd.read_csv('nodes.csv')
all_int = pd.DataFrame()
final_index = pd.DataFrame()


# In[3]:


for i in range(len(node)):
    cisco1 = { 
        "device_type": "cisco_ios",
        "host": node['ip'][i],
        "username": "username",
        "password":"password" ,
        
    }
    command = "terminal length 0"
    command_1 = "show interface description"
    command_2 = "show snmp interface"
    with ConnectHandler(**cisco1) as net_connect:
        try:
            net_connect.send_command(command)
            output = net_connect.send_command(command_1)
            output_2 = net_connect.send_command(command_2)
        except:
            net_connect.send_command(command)
            output = net_connect.send_command(command_1)
            output_2 = net_connect.send_command(command_2)
    with open ('te.txt','w',encoding='utf-8') as file :
        file.write(output)
    with open ('te.txt','r') as file :
        stripped = (line.strip() for line in file)
        lines = (line.split(maxsplit=3) for line in stripped if line)
        with open ('t.csv','w') as outfile :
            writer=csv.writer(outfile)
            writer.writerows(lines)
    #save output in csv
    df=pd.read_csv('t.csv',skiprows=[0,1,3,4,5])
    
    #map interface name
    df['Interface']=df['Interface'].str.replace('BV','BVI')
    df['Interface']=df['Interface'].str.replace('Gi','GigabitEthernet')
    df['Interface']=df['Interface'].str.replace('Te','TenGigE')
    df['Interface']=df['Interface'].str.replace('TE','TenGigE')
    df['Interface']=df['Interface'].str.replace('BE','Bundle-Ether')
    df['Interface']=df['Interface'].str.replace('Be','Bundle-Ether')
    df['Interface']=df['Interface'].str.replace('PO','POS')
    df['Rhost']=node['node'][i]
    
    #add groups 
    group=pd.read_csv('group.csv')
    group.drop(['Description'],axis=1,inplace=True)
    new_df=pd.merge(df,group,how='left',on=['Interface','Rhost'])
    new_df=new_df.fillna("")
    all_int = all_int.append(new_df)
    #print(node['node'][i])
####################################### snmp index ####################################
    with open ('snmp.csv','w',encoding='utf-8') as file :
        file.write(output_2)
    snmp_df = pd.read_csv('snmp.csv',skiprows=1,delim_whitespace=True,header=None) 
    snmp_df.drop(snmp_df.columns[[0,1,3,4]], axis=1, inplace=True)
    snmp_df.columns=['Interface','index']
    snmp_df['Rhost']=node['node'][i]
    final_index = final_index.append(snmp_df)           
    #new_df.to_csv("{}.csv".format(node['node'][i]))
    D={"LEVEL1TAGS":{}}
    for j in range (len(new_df)):
        D[new_df['Interface'][j]]={"IFDESC":new_df['Description'][j],"GR_NAME":new_df['group'][j]}
        #D[new_df['Interface'][j]]={"IFDESC":new_df['Description'][j]}
    E[node['node'][i]]=D
    print(node['node'][i])
final_interfaces = pd.merge(all_int,final_index,how='left',on=['Interface','Rhost'])
final_interfaces.drop_duplicates(inplace=True)
final_interfaces.to_csv('all_interfaces.csv')

    


# In[4]:


with open ("ifdesc.json","w") as file:
    json.dump(E,file,indent=4)






