#Import the requests module

import requests, urllib.parse



#Import os module to interact with the operating system,create,remove or move folders in working directory.

import os,sys,base64



#Import HTTPBasicAuth for authentication to web services

from requests.auth import HTTPBasicAuth



#Get the Start time parameter input from the user in standard time format

start_time = input('Start Time:')



#Set the main url using the base url and data stream ID

main_url = "https://remotemanager.digi.com/ws/DataPoint/00000000-00000000-00409DFF-FF63DD73/xbee.serialIn/[00:13:A2:00:41:4F:7F:0F]!.json?order=desc&"



#Construct the complete url by parsing the main urland the user input arguments. Provide the start time parameter (in ISO8601 format) as a dictionary

url = main_url+urllib.parse.urlencode({'startTime':start_time})



#Make a get request to get the all the latest datapoints from startTime into a response object called resp
#Provide the authentication credentials for the device cloud 

resp = requests.get(url, auth=('aryaprasad.mec@gmail.com','Evtatva1992.'))



# Since we are dealing with json data use the built-in json decoder to get the data into a dictionary object called 'datastream'

datastream = resp.json()



#Open a new file with write permissions

file = open('Data_stream.txt','w')



#For each item in the datastream, get the data value

for each in datastream["items"]:

    data = each['data']

	#decode each datapoint from base64 to ascii format
	
    data_ascii = base64.b64decode(data)

	#Write the decoded data to the file
	
    file.write(str(data_ascii)+'\n')
    
	#Change file permissions to append datapoints to same file
	
    file = open ('Data_stream.txt','a')
    
    
