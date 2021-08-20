# Windows 

### Installation

Install python from the official website https://www.python.org/downloads/

Make sure to check 'add python to environment variables' on installation

If you forget you can rerun the installer and select it under 'modify installation'

In the powershell terminal within VSCode type the command:

pip install -r requirements.txt

Open the functions.py file

Replace 'your key here' for your API key in line 8 for the global API KEY 

### Operation

Open the powershell integrated terminal in the project folder

To use the program enter 

python opswat.py yourfilename.extension 

# Ubuntu

### Installation

Navigate to the folder containing the files downloaded from git

Open the functions.py file

Replace 'your key here' for your API key in line 8 for the global API KEY 

### Operation

Open the terminal and navigate to your file location or open the terminal in your file location

To use the program enter

python3 opswat.py yourfilename.extension 

# Common Errors 

FileNotFoundError: 

Path to the file or filename was entered incorrectly

IndexError:

filename not provided after opswat.py in the command prompt

##Ubuntu Specific

### Requests Error

The request package should already be installed on Ubuntu

If an error arrises from it you can enter 

sudo apt install python3-pip

this will install pip then you can enter

pip install -r requirements.txt 

to install the requirements 
