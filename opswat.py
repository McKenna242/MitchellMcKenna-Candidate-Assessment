import sys
from functions import Functions

def main():

    #grabbing the filename
    fileName = sys.argv[1]
    #hashing the file
    hashNum = (Functions.hashFile(fileName))
    #checking if the file exists
    Functions.hashLookup(hashNum)
    #loading the file if it doesn't exist
    Functions.scanFile(fileName)

main()
