# -*- coding: utf-8 -*-
import json


student= {"101":{"class":'v',"name":'rohit',"roll no":7},
           "102":{"class":'v',"name":'david',"roll no":8},
           "103":{"class":'v',"name":'saniya',"roll no":9}}
print("student type:", type(student)) 
print("printing the json data")
print(json.dumps(student))
print("printing the json data in sorted form")
print(json.dumps(student, sort_keys= True)) #sort_keys=true sorts the data

#tuple to json         
tpl1='camera','lens','mirror'
print("type of tpl1", type(tpl1))
print("converting tuple into json")  #dumps convert python structure to json
jsontpl1=json.dumps(tpl1)
print("jsontpl1 type", type(jsontpl1))
print("jsontpl1", jsontpl1)

#reading json data
print("reading json into dict")
json_data = '{"101":{"class":"v","name":"rohit","roll no":7},"102":{"class":"v","name":"david","roll no":8},"103":{"class":"v","name":"saniya","roll no":9}}';
print(json.loads(json_data)) #loads cionverts json into python
