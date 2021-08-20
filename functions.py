import sys
import hashlib
import requests 
import json
import time

#global API key
API_KEY =  "Your key here"

#Class for functions
class Functions:
    
    #function to hash the file name using md5
    def hashFile(fileName):
                
        #read in 64kb chunks to preserve memory
        BUF_SIZE = 65536 
        
        md5 = hashlib.md5()
        
        with open(sys.argv[1], 'rb') as inFile:
            while True:
                fileData = inFile.read(BUF_SIZE)
                if not fileData:
                    break
                md5.update(fileData)
        
        #converts the result to a string using all uppercase 
        return md5.hexdigest().upper()
                
        
    #function to check if the file has already been uploaded and examined
    def hashLookup(hash):
        
        url = "https://api.metadefender.com/v4/hash/"+hash

        headers = {
            "apikey": API_KEY
        }
        
        response = requests.request("GET", url, headers=headers)

        #if found in cache sends the data to be displayed in console
        if(response.status_code == 200):    
            print("Found in cache")
            Functions.printData(response)
        #if not found main will direct to scanFile
        else:
            print("Uploading")      
            
    #function to upload and scan the file
    #retrieves the data_id and calls fetchFile with it
    def scanFile(fileName):
        
        url = "https://api.metadefender.com/v4/file"
        headers = {
            "apikey": API_KEY,
            "Content-Type": 'application/octet-stream'
        }
        
        file = open(fileName, 'rb')
                
        response = requests.request("POST", url, headers=headers, data=file)
                
        responseDict = response.json()
        Functions.fetchFile(responseDict['data_id'])
    
    #polls the file every 2 seconds checking the upload progress
    #once it's 100% it will call printData and print the scan results
    def fetchFile(dataID):
        url = "https://api.metadefender.com/v4/file/"+dataID
        headers = {
            "apikey": API_KEY,
            "x-file-metadata": "{x-file-metadata}"
        }

        response = requests.request("GET", url, headers=headers)

        fileDict = response.json()
        
        if(response.status_code == 200):

            #if progress is 100% inform the user and call printData
            if(fileDict['scan_results']['progress_percentage'] == 100):
                print("Scan Complete, progress: 100%")
                Functions.printData(response)
            #print current progress, wait 2 seconds, poll again
            else:
                progress = 0
                if(fileDict['scan_results']['progress_percentage']):
                    progress = fileDict['scan_results']['progress_percentage']
                print("Scanning, progress: " + str(progress) + "%")
                #print(response.text)
                time.sleep(2)
                Functions.fetchFile(dataID)
       
        #prints error code and message then exits
        else:
            print("Fetch File Error: ", response.status_code, ":", response.json()['error']['messages'][0])
            exit()

    #takes in a response and converts it to output
    def printData(response):
        
        responseDict = response.json()

        print("filename: " + sys.argv[1])

        #determining if the result of the scan is allowed or blocked        
        processInfoDict = responseDict['process_info']
        if(processInfoDict["result"] == 'Allowed'):
            print("overall_status: Clean")
        else:
            print("overall_status: Infected")
            
        #getting the scan details from scan results in the response and itemizing them to be looped through and displayed
        for key, value in responseDict["scan_results"]["scan_details"].items():
            print("engine: " + key)
            if(value['threat_found'] == ''):
                print("threat_found: Clean")
            else:
                print("threat_found: " + value['threat_found'])
            print("scan_result: " + str(value['scan_result_i']))
            print("def_time: " + value['def_time'])
            
        print("END")            
        exit() 
